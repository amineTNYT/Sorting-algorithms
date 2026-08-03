# ⏱️ TimSort Algorithm

## 📋 Overview

This folder contains a Python implementation of **TimSort**, a stable hybrid
sorting algorithm that combines **Insertion Sort** and **Merge Sort**.

TimSort is the default sorting algorithm used by Python (`sorted()` and
`list.sort()`), designed by Tim Peters in 2002 and since adopted by Java,
Android, and V8. It is optimized for real-world data, which is very often
already partially ordered.

## 🔍 How TimSort Works

1. **Find a run** — scan forward for a stretch that is already ascending or
   descending. Descending runs are reversed in place (reversing rather than
   sorting is what preserves stability).
2. **Extend short runs** — if a run is shorter than `minRun`, extend it to that
   length with Insertion Sort, which is very fast on nearly ordered data.
3. **Merge runs** — push each run on a stack and merge adjacent runs whenever
   the size invariant demands it, keeping merges balanced.

This is why TimSort hits O(n) on sorted input: the entire array is one run, and
there is nothing to merge.

> **Note on `minRun`:** this implementation uses a threshold of 32 to keep the
> demo readable, giving a minimum run length between 16 and 32. CPython uses 64,
> which yields runs between 32 and 64.

## 📊 Time & Space Complexity

| Case | Complexity | Notes |
|---|---|---|
| Best Case | O(n) | Already sorted data — one run, no merging |
| Average Case | O(n log n) | Partially sorted data |
| Worst Case | O(n log n) | Random data |
| Space Complexity | O(n) | Temporary memory for merging |

## 🎯 Characteristics

- **Type**: Hybrid (Insertion + Merge)
- **Stability**: ✅ Stable
- **Adaptive**: ✅ Yes (exploits existing runs)
- **In-place**: ❌ No (uses extra memory)

## 📁 Files

- [`tim_sort.py`](./tim_sort.py) — implementation with commentary
- [`tim_sort.html`](./tim_sort.html) — interactive animation showing run detection and merging, open it in any browser

> Python's built-in `sorted()` is this same algorithm implemented in C. It will
> be far faster than any pure-Python version, including this one — that gap
> measures the language boundary, not the algorithm.
