# ⚡ Quick Sort Algorithm

## 📋 Overview

This repository contains a clean and efficient implementation of **QuickSort**, one of the fastest and most widely used comparison-based sorting algorithms. Developed by Tony Hoare in 1959, QuickSort is a divide-and-conquer algorithm that works by selecting a "pivot" element and partitioning the array around it, then recursively sorting the subarrays.

**Key strengths**:
- Excellent average-case performance: O(n log n)
- In-place sorting (minimal extra memory)
- Highly efficient for large datasets
- Cache-efficient due to locality of reference

## 📊 Time & Space Complexity

| Case          | Time Complexity      | Notes                                      |
|---------------|----------------------|--------------------------------------------|
| Best Case     | O(n log n)           | Balanced partitions (randomized pivot helps) |
| Average Case  | O(n log n)           | Random or typical data                     |
| Worst Case    | O(n²)                | Already sorted/reverse + poor pivot choice  |
| Space Complexity | O(log n)          | Recursion stack (can be O(n) in worst case) |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort / Divide-and-Conquer
- **Stability**: ❌ Not stable (equal elements may change order)
- **In-place**: ✅ Yes (only O(log n) extra space for recursion)
- **Adaptive**: Partially (randomized version reduces worst-case risk)
