"""Benchmark every sorting implementation in this repository.

Design notes, because the numbers are easy to get wrong:

* The algorithms are imported from their own folders via `algorithms.py`. This
  script does not carry its own copies, so what it measures is exactly what the
  folders contain.
* Every algorithm sees the *same* input lists at a given size. Timing each one
  on freshly generated random data would compare them on different problems.
* Python's built-in `sorted()` is excluded by default. It is TimSort written in
  C, so charting it beside pure-Python loops says nothing about the algorithms
  and everything about the language boundary. Pass --include-builtin to add it
  as an explicitly labelled reference line.
* The O(n^2) algorithms stop at --max-quadratic-size. Running Bubble Sort at
  n=20000 in pure Python takes hours and tells you nothing new.

Usage:
    python benchmark/benchmark.py
    python benchmark/benchmark.py --sizes 100 500 1000 --repeats 3
    python benchmark/benchmark.py --include-builtin
"""

import argparse
import random
import sys
import time
from pathlib import Path

# Make the repository root importable when run as `python benchmark/benchmark.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from algorithms import loadAlgorithms  # noqa: E402

DEFAULT_SIZES = (100, 250, 500, 1000, 2000, 4000)
DEFAULT_REPEATS = 3
DEFAULT_MAX_QUADRATIC_SIZE = 2000
DEFAULT_SEED = 20260803
VALUE_SPREAD = 3  # random values range over 0 .. size * VALUE_SPREAD


def parseArgs() -> argparse.Namespace:
    """Read benchmark parameters from the command line."""
    parser = argparse.ArgumentParser(
        description="Compare the runtime of every sorting algorithm in this repo.",
    )
    parser.add_argument(
        "--sizes", type=int, nargs="+", default=list(DEFAULT_SIZES),
        help=f"input sizes to test (default: {' '.join(map(str, DEFAULT_SIZES))})",
    )
    parser.add_argument(
        "--repeats", type=int, default=DEFAULT_REPEATS,
        help=f"timed runs per size, averaged (default: {DEFAULT_REPEATS})",
    )
    parser.add_argument(
        "--max-quadratic-size", type=int, default=DEFAULT_MAX_QUADRATIC_SIZE,
        help=(
            "skip O(n^2) algorithms above this size "
            f"(default: {DEFAULT_MAX_QUADRATIC_SIZE})"
        ),
    )
    parser.add_argument(
        "--seed", type=int, default=DEFAULT_SEED,
        help=f"random seed, for reproducible runs (default: {DEFAULT_SEED})",
    )
    parser.add_argument(
        "--include-builtin", action="store_true",
        help="add Python's built-in sorted() as a C-implemented reference line",
    )
    parser.add_argument(
        "--output", type=Path, default=None,
        help="chart destination (default: benchmark/results/sorting_performance.png)",
    )
    return parser.parse_args()


def buildDatasets(rng: random.Random, size: int, repeats: int) -> list[list[int]]:
    """Create `repeats` random lists of `size` integers, reused by every algorithm."""
    return [
        [rng.randint(0, size * VALUE_SPREAD) for _ in range(size)]
        for _ in range(repeats)
    ]


def timeAlgorithm(sortFunction, datasets: list[list[int]], label: str) -> float:
    """Return the average seconds `sortFunction` takes over `datasets`.

    Raises ValueError if the algorithm produces an incorrectly sorted result.
    """
    totalSeconds = 0.0

    for dataset in datasets:
        working = list(dataset)

        start = time.perf_counter()
        sortFunction(working)
        totalSeconds += time.perf_counter() - start

        # Checked explicitly rather than with `assert`, which `python -O` strips
        if working != sorted(dataset):
            raise ValueError(f"{label} returned an incorrectly sorted result")

    return totalSeconds / len(datasets)


def runBenchmark(args: argparse.Namespace) -> dict[str, dict[int, float]]:
    """Time every algorithm at every requested size."""
    algorithms = loadAlgorithms()

    if args.include_builtin:
        algorithms = list(algorithms) + [(_BuiltinSpec(), _builtinSort)]

    rng = random.Random(args.seed)
    results: dict[str, dict[int, float]] = {spec.name: {} for spec, _ in algorithms}

    for size in args.sizes:
        print(f"Input size: {size}")
        datasets = buildDatasets(rng, size, args.repeats)

        for spec, sortFunction in algorithms:
            if spec.isQuadratic and size > args.max_quadratic_size:
                print(f"  {spec.name:<16} skipped (above --max-quadratic-size)")
                continue

            averageSeconds = timeAlgorithm(sortFunction, datasets, spec.name)
            results[spec.name][size] = averageSeconds
            print(f"  {spec.name:<16} {averageSeconds:.6f} s")

        print()

    return results


class _BuiltinSpec:
    """Minimal stand-in so sorted() flows through the same code path."""

    name = "Built-in sorted() [C]"
    isQuadratic = False
    isIntegerOnly = False


def _builtinSort(arr: list) -> None:
    """Sort in place using Python's own C TimSort, for reference only."""
    arr.sort()


def printSummary(results: dict[str, dict[int, float]], sizes: list[int]) -> None:
    """Print a table of average times, in milliseconds."""
    nameWidth = max(len(name) for name in results)
    header = f"{'Algorithm':<{nameWidth}}" + "".join(f"{size:>12}" for size in sizes)

    print("Average time in milliseconds")
    print(header)
    print("-" * len(header))

    for name, timings in results.items():
        row = f"{name:<{nameWidth}}"
        for size in sizes:
            row += f"{timings[size] * 1000:>12.3f}" if size in timings else f"{'-':>12}"
        print(row)

    print()


def renderChart(
    results: dict[str, dict[int, float]],
    outputPath: Path,
) -> bool:
    """Save a log-log chart of the results. Returns False if matplotlib is absent."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print(
            "matplotlib is not installed, so no chart was written.\n"
            "Install it with:  pip install -r requirements.txt",
            file=sys.stderr,
        )
        return False

    plt.figure(figsize=(12, 8))

    for name, timings in results.items():
        if not timings:
            continue
        measuredSizes = sorted(timings)
        plt.plot(
            measuredSizes,
            [timings[size] for size in measuredSizes],
            marker="o",
            linewidth=2,
            label=name,
        )

    plt.title("Sorting Algorithms Performance Comparison", fontsize=16)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Average Execution Time (seconds)", fontsize=12)
    plt.legend(loc="upper left")
    plt.grid(True, alpha=0.3)

    # Log-log axes turn each complexity class into a straight line of its own slope
    plt.xscale("log")
    plt.yscale("log")
    plt.tight_layout()

    outputPath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outputPath)
    plt.close()
    return True


def main() -> int:
    args = parseArgs()

    if args.repeats < 1:
        print("--repeats must be at least 1", file=sys.stderr)
        return 1
    if any(size < 0 for size in args.sizes):
        print("--sizes must not be negative", file=sys.stderr)
        return 1

    args.sizes = sorted(set(args.sizes))
    outputPath = args.output or (
        Path(__file__).resolve().parent / "results" / "sorting_performance.png"
    )

    print("Starting sorting algorithms benchmark")
    print(f"  sizes:   {args.sizes}")
    print(f"  repeats: {args.repeats}")
    print(f"  seed:    {args.seed}\n")

    try:
        results = runBenchmark(args)
    except ValueError as error:
        print(f"Benchmark aborted: {error}", file=sys.stderr)
        return 1

    printSummary(results, args.sizes)

    if renderChart(results, outputPath):
        print(f"Chart saved to: {outputPath}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
