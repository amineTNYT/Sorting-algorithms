# 🫧 Bubble Sort Algorithm

## 📋 Overview

This repository contains an optimized implementation of the classic Bubble Sort algorithm in Python. Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order.

## ⚡ Optimizations Implemented

This version includes several key optimizations over the naive implementation:

1. **Early Termination**: The algorithm stops early if no swaps occur in a complete pass, indicating the array is already sorted.
2. **Reduced Pass Boundary**: Each pass ignores the already-sorted elements at the end of the array, reducing unnecessary comparisons.
3. **Swapped Flag**: A boolean flag tracks whether any swaps occurred during each pass, enabling early exit for sorted or nearly-sorted arrays.

## 📊 Time & Space Complexity

| Case          | Time Complexity | Notes                                      |
|---------------|-----------------|--------------------------------------------|
| Best Case     | O(n)            | When array is already sorted (early termination) |
| Average Case  | O(n²)           | For randomly ordered data                  |
| Worst Case    | O(n²)           | When array is reverse sorted               |
| Space Complexity | O(1)         | In-place sorting algorithm                 |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort
- **Stability**: ✅ Stable (preserves order of equal elements)
- **In-place**: ✅ Yes (requires only O(1) extra memory)
- **Adaptive**: ✅ Yes (faster on partially sorted data)

## 📝 Code
[bubble code](https://github.com/amineTNYT/Sorting-algorithms/blob/main/Bubble%20sort/Bubble%20Code.py)
