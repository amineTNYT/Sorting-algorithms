# 🔄 Insertion Sort Algorithm

## 📋 Overview

This repository contains a simple and efficient implementation of **Insertion Sort**, one of the most basic comparison-based sorting algorithms. It works by building a sorted portion of the array one element at a time, inserting each new element into its correct position among the already-sorted elements.

**Key strengths**:
- Extremely efficient on small or nearly sorted arrays
- Adaptive: O(n) time when input is already sorted
- Stable sorting
- In-place with minimal overhead
- Online: can sort a list as it receives elements

## 📊 Time & Space Complexity

| Case          | Time Complexity      | Notes                                      |
|---------------|----------------------|--------------------------------------------|
| Best Case     | O(n)                 | Already sorted (only n-1 comparisons)       |
| Average Case  | O(n²)                | Randomly ordered data                      |
| Worst Case    | O(n²)                | Reverse sorted                             |
| Space Complexity | O(1)              | Truly in-place (only a few variables)      |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort
- **Stability**: ✅ Stable (preserves order of equal elements)
- **In-place**: ✅ Yes (O(1) extra space)
- **Adaptive**: ✅ Highly adaptive (fast on partially sorted data)
- **Online**: ✅ Can sort as elements arrive



