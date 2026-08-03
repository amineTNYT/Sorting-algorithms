# 🪣 Bucket Sort Algorithm

## 📋 Overview

This folder contains an implementation of **Bucket Sort**, a distribution
algorithm that scatters values into a number of ordered buckets, sorts each
bucket individually, then concatenates them.

Unlike [Counting Sort](../Counting%20sort) and [Radix Sort](../Radix%20sort),
Bucket Sort is not restricted to integers — it works on any numeric data,
which makes it a natural fit for uniformly distributed floats.

## 🔍 How Bucket Sort Works

1. Create n empty buckets
2. Map each value to a bucket by its position within the overall range
3. Sort each bucket (this implementation uses Insertion Sort, which is ideal
   because buckets are expected to be small)
4. Concatenate the buckets in order

Because the buckets are already ordered relative to each other, step 4 needs no
merging — a simple concatenation produces the sorted array.

## ⚖️ The Distribution Assumption

Bucket Sort's performance rests entirely on how evenly the data spreads:

- **Uniformly distributed data** — every bucket holds about one element, each
  insertion sort is trivial, and the total cost is O(n)
- **Heavily skewed data** — most values land in one bucket, that bucket's
  insertion sort becomes O(n²), and the algorithm degrades to quadratic

This is the same shape of risk Quick Sort has with pivot choice: excellent
typical behaviour, poor pathological behaviour.

## 📊 Time & Space Complexity

| Case | Complexity | Notes |
|---|---|---|
| Best Case | O(n + k) | Values spread evenly across k buckets |
| Average Case | O(n + k) | Assumes a uniform distribution |
| Worst Case | O(n²) | All values land in one bucket |
| Space Complexity | O(n + k) | The buckets themselves |

## 🎯 Algorithm Characteristics

- **Type**: Distribution Sort
- **Stability**: ✅ Stable (insertion sort within buckets preserves order)
- **In-place**: ❌ No (buckets need their own memory)
- **Adaptive**: ❌ No

## 📁 Files

- [`bucket_sort.py`](./bucket_sort.py) — implementation with commentary
- [`bucket_sort.html`](./bucket_sort.html) — interactive animation showing the scatter, sort and gather phases, open it in any browser
