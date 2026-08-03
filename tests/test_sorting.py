"""Correctness tests shared by every sorting implementation in the repository.

Each algorithm is loaded from its own folder through `algorithms.py`, so these
tests cover the code readers actually see - not a separate copy.
"""

import random
from functools import total_ordering

import pytest

from algorithms import loadAlgorithms

# (spec, function) pairs, plus matching ids so failures name the algorithm
ALL_ALGORITHMS = loadAlgorithms()
ALL_IDS = [spec.name for spec, _ in ALL_ALGORITHMS]

COMPARISON_ALGORITHMS = loadAlgorithms(includeIntegerOnly=False)
COMPARISON_IDS = [spec.name for spec, _ in COMPARISON_ALGORITHMS]

# Algorithms this repository documents as preserving the order of equal elements
STABLE_ALGORITHMS = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Tim Sort"]

EDGE_CASES = [
    pytest.param([], id="empty"),
    pytest.param([1], id="single"),
    pytest.param([2, 1], id="pair-reversed"),
    pytest.param([1, 2], id="pair-sorted"),
    pytest.param([7, 7, 7, 7], id="all-equal"),
    pytest.param(list(range(64)), id="already-sorted"),
    pytest.param(list(range(64))[::-1], id="reverse-sorted"),
    pytest.param([0, -1, 5, -9, 3, -3], id="negatives"),
    pytest.param([4, 2, 4, 1, 2, 4], id="duplicates"),
]


@total_ordering
class Item:
    """Orders only on `key`, so `tag` can reveal whether a sort was stable."""

    def __init__(self, key: int, tag: int) -> None:
        self.key = key
        self.tag = tag

    def __lt__(self, other: "Item") -> bool:
        return self.key < other.key

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Item) and self.key == other.key

    def __repr__(self) -> str:
        return f"Item({self.key}, {self.tag})"


@pytest.mark.parametrize("data", EDGE_CASES)
@pytest.mark.parametrize("spec,sortFunction", ALL_ALGORITHMS, ids=ALL_IDS)
def testSortsEdgeCases(spec, sortFunction, data: list) -> None:
    actual = list(data)
    sortFunction(actual)
    assert actual == sorted(data)


@pytest.mark.parametrize("spec,sortFunction", ALL_ALGORITHMS, ids=ALL_IDS)
def testSortsRandomIntegers(spec, sortFunction) -> None:
    rng = random.Random(20260803)
    for _ in range(200):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 80))]
        actual = list(data)
        sortFunction(actual)
        assert actual == sorted(data), f"{spec.name} failed on {data}"


@pytest.mark.parametrize("spec,sortFunction", ALL_ALGORITHMS, ids=ALL_IDS)
def testSortsInPlaceWithoutLosingElements(spec, sortFunction) -> None:
    """The caller's own list object must hold the result, with nothing dropped."""
    data = [5, 3, 9, 1, 5, 3]
    actual = data
    sortFunction(actual)

    assert actual is data, f"{spec.name} did not sort in place"
    assert sorted(actual) == sorted([5, 3, 9, 1, 5, 3])


@pytest.mark.parametrize("spec,sortFunction", COMPARISON_ALGORITHMS, ids=COMPARISON_IDS)
def testSortsFloats(spec, sortFunction) -> None:
    """Comparison sorts and Bucket Sort must handle non-integer input."""
    rng = random.Random(11)
    data = [rng.uniform(-100.0, 100.0) for _ in range(60)]
    actual = list(data)
    sortFunction(actual)
    assert actual == sorted(data)


@pytest.mark.parametrize(
    "spec,sortFunction",
    [pair for pair in ALL_ALGORITHMS if pair[0].name in STABLE_ALGORITHMS],
    ids=[name for name in ALL_IDS if name in STABLE_ALGORITHMS],
)
def testStableSortsPreserveOrderOfEqualElements(spec, sortFunction) -> None:
    # Three groups of equal keys, each tagged with its original position
    data = [Item(key, tag) for tag, key in enumerate([2, 1, 2, 1, 3, 2, 1])]
    sortFunction(data)

    assert [item.key for item in data] == [1, 1, 1, 2, 2, 2, 3]
    # Within each key group the tags must still ascend
    assert [item.tag for item in data] == [1, 3, 6, 0, 2, 5, 4]


@pytest.mark.parametrize("spec,sortFunction", ALL_ALGORITHMS, ids=ALL_IDS)
def testHandlesSortedInputWithoutRecursionError(spec, sortFunction) -> None:
    """Regression test: Quick Sort with a fixed pivot blew the stack here.

    A last-element pivot recurses once per element on already-sorted input,
    raising RecursionError from roughly 1,500 elements upward.
    """
    if spec.isQuadratic:
        pytest.skip("O(n^2) algorithms are too slow at this size")

    size = 5000
    data = list(range(size))
    sortFunction(data)
    assert data == list(range(size))
