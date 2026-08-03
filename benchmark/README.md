# Sorting Algorithms Benchmark

This folder contains a script that compares the **real-world performance** of
every sorting algorithm in this repository.

The goal: see the actual gap between theoretical complexity (O(n²), O(n log n))
and measured execution time on real data.

## 🚀 Running It

### Requirements

- Python 3.10 or higher
- One external library, `matplotlib`, for the chart

```bash
pip install -r ../requirements.txt
```

### Execution

```bash
git clone https://github.com/amineTNYT/Sorting-algorithms.git
cd Sorting-algorithms
python benchmark/benchmark.py
```

The chart is written to `benchmark/results/sorting_performance.png`, and a
summary table is printed to the terminal.

## ⚙️ Options

| Flag | Default | Purpose |
|---|---|---|
| `--sizes` | `100 250 500 1000 2000 4000` | Input sizes to test |
| `--repeats` | `3` | Timed runs per size, averaged |
| `--max-quadratic-size` | `2000` | Skip O(n²) algorithms above this size |
| `--seed` | `20260803` | Random seed, for reproducible runs |
| `--include-builtin` | off | Add Python's `sorted()` as a reference line |
| `--output` | `results/sorting_performance.png` | Chart destination |

```bash
# Quick run
python benchmark/benchmark.py --sizes 100 500 1000 --repeats 2

# Push the O(n log n) algorithms harder
python benchmark/benchmark.py --sizes 5000 20000 50000 --max-quadratic-size 0
```

## 📐 How the Measurements Are Kept Honest

Benchmarks are easy to get wrong. Four deliberate choices here:

**The algorithms are imported, not copied.** Every implementation is loaded from
its own folder through [`algorithms.py`](../algorithms.py). The benchmark
carries no second copy that could drift out of sync, so what it measures is
exactly the code in these folders.

**Every algorithm sees identical input.** The datasets for a given size are
generated once and reused across all eleven algorithms. Generating fresh random
data per algorithm would compare them on different problems and quietly add
noise to every number.

**`sorted()` is excluded by default.** Python's built-in is TimSort written in
C. Charting it beside pure-Python loops measures the C/Python boundary, not the
algorithms — it typically looks 20-1000× faster for reasons that have nothing to
do with algorithmic merit. Pass `--include-builtin` to add it as an explicitly
labelled reference line.

**Quadratic algorithms are capped.** Bubble, Insertion, and Selection Sort stop
at `--max-quadratic-size` (2,000 by default). Running Bubble Sort at n=20,000 in
pure Python takes hours and teaches you nothing you cannot already read off the
curve.

## 📊 Reading the Chart

Both axes are logarithmic, which turns each complexity class into a straight
line with its own slope:

- **O(n²)** algorithms rise at roughly twice the slope of the O(n log n) ones
- **O(n log n)** algorithms cluster together in a tight band
- **Linear-time** sorts (Counting, Radix) sit flattest of all

Correctness is verified after every single timed run, so a chart only gets
produced if all eleven algorithms sorted every dataset correctly.
