# ⚡ Quick Sort Algorithm

## 📋 Overview

This folder contains a clean and efficient implementation of **QuickSort**, one
of the fastest and most widely used comparison-based sorting algorithms.
Developed by Tony Hoare in 1959, QuickSort is a divide-and-conquer algorithm
that works by selecting a "pivot" element and partitioning the array around it,
then recursively sorting the subarrays.

**Key strengths**:
- Excellent average-case performance: O(n log n)
- In-place sorting (minimal extra memory)
- Highly efficient for large datasets
- Cache-efficient due to locality of reference

## 🎲 On the Pivot

This implementation uses **Lomuto partitioning with a randomly chosen pivot**.
The randomization matters more than it might appear:

With a fixed last-element pivot, sorted or reverse-sorted input produces the
worst possible partition every single time — one side gets n-1 elements and the
other gets none. That is both O(n²) time *and* n-deep recursion, so in Python
it raises `RecursionError` on an already-sorted list of roughly 1,500 elements
or more. Choosing the pivot at random makes that case vanishingly unlikely
regardless of how the input is ordered.

The trade-off is that the algorithm is no longer deterministic: two runs on the
same input may perform different swaps, though both produce the same sorted
result.

## 📊 Time & Space Complexity

| Case | Time Complexity | Notes |
|---|---|---|
| Best Case | O(n log n) | Balanced partitions |
| Average Case | O(n log n) | Random or typical data |
| Worst Case | O(n²) | Repeatedly unbalanced partitions (very unlikely with a random pivot) |
| Space Complexity | O(log n) | Recursion stack (O(n) in the worst case) |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort / Divide-and-Conquer
- **Stability**: ❌ Not stable (equal elements may change order)
- **In-place**: ✅ Yes (only O(log n) extra space for recursion)
- **Adaptive**: ❌ No (does not exploit existing order)

## 📁 Files

- [`quick_sort.py`](./quick_sort.py) — implementation with commentary
- [`quick_sort.html`](./quick_sort.html) — interactive animation showing pivot selection and partitioning, open it in any browser
