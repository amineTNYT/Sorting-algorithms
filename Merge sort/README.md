# 🔀 Merge Sort Algorithm

## 📋 Overview

This folder contains a clean and efficient implementation of **Merge Sort**, a
classic divide-and-conquer sorting algorithm. Developed by John von Neumann in
1945, Merge Sort works by recursively dividing the array into halves, sorting
each half, and then merging the sorted halves back together.

**Key strengths**:
- Guaranteed O(n log n) time complexity in all cases
- Stable sorting (preserves order of equal elements)
- Excellent for large datasets and linked lists
- Naturally parallelizable

## 🔍 How Merge Sort Works

1. If the range holds 0 or 1 elements, it is already sorted — stop
2. Split the range at its midpoint
3. Recursively sort the left half, then the right half
4. Merge the two sorted halves by repeatedly taking the smaller front element

Step 4 is where the work happens: merging two sorted lists of combined length n
costs exactly n comparisons at most, and the recursion is log n levels deep.

The merge compares with `<=` rather than `<`. That single character is what
makes the sort stable — on a tie, the element from the left half is taken
first, preserving the original order.

## 📊 Time & Space Complexity

| Case | Time Complexity | Notes |
|---|---|---|
| Best Case | O(n log n) | Always divides evenly |
| Average Case | O(n log n) | Consistent performance |
| Worst Case | O(n log n) | No degradation |
| Space Complexity | O(n) | Requires temporary arrays for merging |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort / Divide-and-Conquer
- **Stability**: ✅ Stable
- **In-place**: ❌ No (requires O(n) extra space)
- **Adaptive**: ❌ Not adaptive (same cost regardless of input order)

## 📁 Files

- [`merge_sort.py`](./merge_sort.py) — implementation with commentary
- [`merge_sort.html`](./merge_sort.html) — interactive animation showing the
  divide and merge phases, open it in any browser
