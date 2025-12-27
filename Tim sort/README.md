
# ⏱️ TimSort Algorithm

## 📋 Overview

This repository contains a Python implementation of **TimSort**, the hybrid stable sorting algorithm developed by Tim Peters in 2002. TimSort combines the strengths of **Insertion Sort** (for small runs) and **Merge Sort** (for merging runs efficiently). It is the default sorting algorithm in Python (`list.sort()` and `sorted()`) and Java (for objects), known for excellent performance on real-world data that often contains partially sorted sections ("natural runs").

**Key strengths**:
- Adaptive: O(n) best case on already-sorted data
- Stable: Preserves order of equal elements
- O(n log n) worst/average case
- Efficient on partially sorted or real-world datasets

## ⚡ Key Features & Optimizations in This Implementation

- **Natural run detection**: Identifies ascending/descending runs and reverses descending ones
- **Dynamic minRun calculation**: Uses the official CPython method (range ~32–64) for balanced merges
- **Strict run enforcement**: Extends short runs with Insertion Sort
- **Efficient merging**: Bottom-up merge with a simple stack-based approach
- **In-place sorting** with temporary storage only during merges

## 📊 Time & Space Complexity

| Case          | Time Complexity      | Notes                                      |
|---------------|----------------------|--------------------------------------------|
| Best Case     | O(n)                 | Already sorted (detects one large run)     |
| Average Case  | O(n log n)           | Real-world data with partial order         |
| Worst Case    | O(n log n)           | Random data                                |
| Space Complexity | O(n)              | Temporary array for merging (can be optimized to O(n/2) in advanced versions) |

## 🎯 Algorithm Characteristics

- **Type**: Hybrid (Insertion + Merge)
- **Stability**: ✅ Stable
- **In-place**: Partially (O(n) extra space)
- **Adaptive**: ✅ Highly adaptive to existing order
