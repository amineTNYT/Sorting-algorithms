# 🐚 Shell Sort Algorithm

## 📋 Overview

This folder contains an implementation of Shell Sort, an efficient generalization of Insertion Sort that sorts elements far apart first and progressively reduces the gap between elements being compared. Developed by Donald Shell in 1959, it's one of the oldest non-trivial sorting algorithms that significantly outperforms basic O(n²) algorithms.

## 🔍 How Shell Sort Works

Shell Sort works by breaking the original list into smaller sublists which are then sorted using Insertion Sort. The unique aspect is that these sublists consist of elements a certain "gap" apart.

**The Process:**

1. Start with a large gap (typically half the array length)
2. Sort sublists of elements spaced by this gap using Insertion Sort
3. Reduce the gap and repeat
4. Continue until gap becomes 1 (standard Insertion Sort on the nearly sorted array)


## 📊 Time Complexity

| Case          | Time Complexity      | Notes                          |
|---------------|----------------------|--------------------------------|
| Best Case     | O(n log n)           | Depends on gap sequence        |
| Average Case  | O(n log² n) or O(n^{3/2}) | Varies with gap sequence   |
| Worst Case    | O(n²)                | With poor gap sequence         |
| Space Complexity | O(1)              | In-place sorting algorithm     |

## 🎯 Key Features

- **Type**: Comparison Sort
- **Stability**: ❌ Not stable (may change order of equal elements)
- **In-place**: ✅ Yes (requires only O(1) extra memory)
- **Adaptive**: ✅ Yes (performance depends on initial order)
- **Gap Sequences**: Performance heavily depends on the chosen gap sequence
