# 🔄 Merge Sort Algorithm

## 📋 Overview

This folder contains a clean and efficient implementation of **Merge Sort**, a classic divide-and-conquer sorting algorithm. Developed by John von Neumann in 1945, Merge Sort works by recursively dividing the array into halves, sorting each half, and then merging the sorted halves back together.

**Key strengths**:
- Guaranteed O(n log n) time complexity in all cases
- Stable sorting (preserves order of equal elements)
- Excellent for large datasets and linked lists
- Naturally parallelizable

## 📊 Time & Space Complexity

| Case          | Time Complexity      | Notes                                      |
|---------------|----------------------|--------------------------------------------|
| Best Case     | O(n log n)           | Always divides evenly                      |
| Average Case  | O(n log n)           | Consistent performance                     |
| Worst Case    | O(n log n)           | No degradation                             |
| Space Complexity | O(n)              | Requires temporary array for merging        |

## 🎯 Algorithm Characteristics

- **Type**: Comparison Sort / Divide-and-Conquer
- **Stability**: ✅ Stable
- **In-place**: ❌ No (requires O(n) extra space)
- **Adaptive**: ❌ Not adaptive (same cost regardless of input order)
