# 🌳 Heap Sort Algorithm

## 📋 Overview

This folder contains an implementation of **Heap Sort**, which uses a binary
heap data structure to sort an array in place. Invented by J. W. J. Williams in
1964, it is the rare algorithm that offers Merge Sort's guaranteed O(n log n)
worst case *and* Quick Sort's O(1) memory usage.

## 🔍 How Heap Sort Works

A **max-heap** is a complete binary tree where every parent is at least as large
as its children — so the largest element is always at the root. The tree is
stored directly in the array: for the node at index `i`, its children live at
`2i + 1` and `2i + 2`.

1. **Build the heap** — starting from the last internal node and working
   backwards, sink each element into place. Leaves are already valid heaps, so
   the loop starts at `n // 2 - 1`.
2. **Extract repeatedly** — swap the root (the maximum) with the last element of
   the unsorted region, shrink that region by one, and restore the heap
   property at the root.

After n-1 extractions the array is sorted, and no extra memory was needed.

## 📊 Time & Space Complexity

| Case | Time Complexity | Notes |
|---|---|---|
| Best Case | O(n log n) | No shortcut for sorted input |
| Average Case | O(n log n) | Consistent |
| Worst Case | O(n log n) | Never degrades, unlike Quick Sort |
| Space Complexity | O(1) | Truly in-place |

Building the heap is O(n), not O(n log n) — a result that surprises most people
the first time they see the proof. The n-1 extractions dominate at O(n log n).

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort / Selection-based
- **Stability**: ❌ Not stable (heap operations move equal elements past each other)
- **In-place**: ✅ Yes (O(1) extra memory)
- **Adaptive**: ❌ No (identical cost on sorted input)

## 💡 When to Use It

Heap Sort is the safe choice when you need a hard worst-case guarantee *and*
constant memory — for example in embedded or real-time systems. In practice
Quick Sort is usually faster on random data because Heap Sort's memory access
pattern jumps around the array and defeats the CPU cache.

## 📁 Files

- [`heap_sort.py`](./heap_sort.py) — implementation with commentary
- [`heap_sort.html`](./heap_sort.html) — interactive animation showing the heap being built and drained, open it in any browser
