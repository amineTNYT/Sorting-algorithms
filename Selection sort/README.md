# 🎯 Selection Sort Algorithm

## 📋 Overview

This folder contains an implementation of **Selection Sort**, a straightforward
comparison-based algorithm. It divides the array into a sorted region at the
front and an unsorted region behind it, then repeatedly finds the smallest
element in the unsorted region and swaps it into place.

## 🔍 How Selection Sort Works

1. Treat position 0 as the start of the unsorted region
2. Scan the entire unsorted region to find its minimum element
3. Swap that minimum with the element at the front of the unsorted region
4. Shrink the unsorted region by one and repeat

After the i-th pass, the first i elements are in their final sorted positions
and are never touched again.

**Key characteristic**: Selection Sort performs exactly **n-1 swaps**, the
fewest of any quadratic sorting algorithm. That makes it worth considering in
the narrow case where writes are far more expensive than reads — such as
flash memory, where every write wears the hardware. Insertion Sort is the
better choice in essentially every other situation.

Note that the number of *comparisons* is always ~n²/2 regardless of input.
Selection Sort cannot detect that its input is already sorted, which is why it
has no O(n) best case the way Bubble and Insertion Sort do.

## 📊 Time & Space Complexity

| Case | Time Complexity | Notes |
|---|---|---|
| Best Case | O(n²) | No early exit — the full scan always runs |
| Average Case | O(n²) | Randomly ordered data |
| Worst Case | O(n²) | Same cost as every other case |
| Space Complexity | O(1) | In-place, only an index variable |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort
- **Stability**: ❌ Not stable (long-range swaps can reorder equal elements)
- **In-place**: ✅ Yes (requires only O(1) extra memory)
- **Adaptive**: ❌ No (identical cost on sorted and reverse-sorted input)
- **Writes**: ✅ Only n-1 swaps, the minimum among quadratic sorts

## 📁 Files

- [`selection_sort.py`](./selection_sort.py) — implementation with commentary
- [`selection_sort.html`](./selection_sort.html) — interactive animation showing each pass hunting for the smallest remaining value, open it in any browser
