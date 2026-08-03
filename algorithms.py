"""Central registry of every sorting implementation in this repository.

The algorithm folders have spaces in their names ("Bubble sort"), so they can
not be reached with a normal `import` statement. This module loads each file by
path instead and exposes them through one uniform interface, so the benchmark
and the test suite both exercise the exact same code a reader sees in the
folders rather than a second copy.

Every registered function sorts a list in place and returns None:

    from algorithms import loadAlgorithms

    for spec, sort in loadAlgorithms():
        data = [3, 1, 2]
        sort(data)
"""

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class AlgorithmSpec:
    """Static description of one sorting implementation."""

    name: str
    path: str
    functionName: str
    isQuadratic: bool = False
    isIntegerOnly: bool = False


# Ordered roughly from simplest to most involved.
SPECS: tuple[AlgorithmSpec, ...] = (
    AlgorithmSpec("Bubble Sort", "Bubble sort/bubble_sort.py", "bubbleSort", isQuadratic=True),
    AlgorithmSpec("Insertion Sort", "Insertion sort/insertion_sort.py", "insertionSort", isQuadratic=True),
    AlgorithmSpec("Selection Sort", "Selection sort/selection_sort.py", "selectionSort", isQuadratic=True),
    AlgorithmSpec("Shell Sort", "Shell sort/shell_sort.py", "shellSort"),
    AlgorithmSpec("Merge Sort", "Merge sort/merge_sort.py", "mergeSort"),
    AlgorithmSpec("Quick Sort", "Quick sort/quick_sort.py", "quickSort"),
    AlgorithmSpec("Heap Sort", "Heap sort/heap_sort.py", "heapSort"),
    AlgorithmSpec("Tim Sort", "Tim sort/tim_sort.py", "timSort"),
    AlgorithmSpec("Counting Sort", "Counting sort/counting_sort.py", "countingSort", isIntegerOnly=True),
    AlgorithmSpec("Radix Sort", "Radix sort/radix_sort.py", "radixSort", isIntegerOnly=True),
    AlgorithmSpec("Bucket Sort", "Bucket sort/bucket_sort.py", "bucketSort"),
)


def _loadFunction(spec: AlgorithmSpec) -> Callable[[list], None]:
    """Import the module at `spec.path` and return its sorting function."""
    fullPath = REPO_ROOT / spec.path
    if not fullPath.exists():
        raise FileNotFoundError(f"{spec.name}: no implementation at {fullPath}")

    # Namespace the module so that same-named helpers in different files
    # (several define their own insertionSort) do not overwrite each other.
    moduleName = f"sortingAlgorithms.{fullPath.stem}"

    loaderSpec = importlib.util.spec_from_file_location(moduleName, fullPath)
    if loaderSpec is None or loaderSpec.loader is None:
        raise ImportError(f"{spec.name}: could not load {fullPath}")

    module = importlib.util.module_from_spec(loaderSpec)
    sys.modules[moduleName] = module
    loaderSpec.loader.exec_module(module)

    try:
        return getattr(module, spec.functionName)
    except AttributeError as error:
        raise AttributeError(
            f"{spec.name}: {fullPath.name} defines no function "
            f"named {spec.functionName!r}"
        ) from error


def loadAlgorithms(
    includeIntegerOnly: bool = True,
    includeQuadratic: bool = True,
) -> list[tuple[AlgorithmSpec, Callable[[list], None]]]:
    """Load every registered algorithm as a (spec, function) pair.

    Set `includeIntegerOnly` to False to skip Counting and Radix sort, which
    can not handle floats. Set `includeQuadratic` to False to skip the O(n^2)
    algorithms when benchmarking large inputs.
    """
    selected = [
        spec
        for spec in SPECS
        if (includeIntegerOnly or not spec.isIntegerOnly)
        and (includeQuadratic or not spec.isQuadratic)
    ]
    return [(spec, _loadFunction(spec)) for spec in selected]


if __name__ == "__main__":
    print(f"Registered algorithms ({len(SPECS)}):\n")
    for spec, sortFunction in loadAlgorithms():
        sample = [5, 2, 9, 1, 7, 3]
        sortFunction(sample)
        status = "ok" if sample == sorted(sample) else "FAILED"
        print(f"  {spec.name:<16} {spec.functionName:<16} {status}")
