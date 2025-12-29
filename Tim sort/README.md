# ⏱️ TimSort Algorithm

This folder contains a Python implementation of **TimSort**, a stable hybrid sorting algorithm that combines **Insertion Sort** and **Merge Sort**.

TimSort is the default sorting algorithm used by Python (`sorted()` and `list.sort()`), optimized for real-world and partially sorted data.

## 📊 Time & Space Complexity

| Case              | Complexity     | Notes                          |
|-------------------|----------------|--------------------------------|
| Best Case         | O(n)           | Already sorted data            |
| Average Case      | O(n log n)     | Partially sorted data          |
| Worst Case        | O(n log n)     | Random data                    |
| Space Complexity  | O(n)           | Temporary memory for merging   |

## 🎯 Characteristics

- **Type**: Hybrid (Insertion + Merge)
- **Stability**: ✅ Stable
- **Adaptive**: ✅ Yes
- **In-place**: ❌ No (uses extra memory)
