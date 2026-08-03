# 🔢 Radix Sort Algorithm

## 📋 Overview

This folder contains an implementation of **Radix Sort**, a
**non-comparison** algorithm that sorts integers by processing them one digit at
a time. It solves [Counting Sort](../Counting%20sort)'s biggest weakness: where
Counting Sort needs memory proportional to the *range* of values, Radix Sort
needs only enough for a single digit — 10 counters in base 10, no matter how
large the numbers get.

## 🔍 How Radix Sort Works

This is the **LSD** (least significant digit) variant:

1. Sort the whole array by the ones digit, using a stable Counting Sort
2. Sort it again by the tens digit
3. Continue through every digit position of the largest number

The magic is in **stability**. When the pass over the tens digit encounters two
numbers with the same tens digit, it preserves the order established by the
previous pass — which had already sorted them by their ones digit. Each pass
therefore builds on the last, and after the final digit the array is fully
sorted.

If the per-digit sort were not stable, the whole approach would collapse.

Negative numbers need care, since digit extraction assumes non-negative values.
This implementation splits them out, sorts their magnitudes, and lays them back
down reversed.

## 📊 Time & Space Complexity

| Case | Complexity | Notes |
|---|---|---|
| Best Case | O(d × (n + b)) | d = digit count, b = base (10 here) |
| Average Case | O(d × (n + b)) | Independent of input order |
| Worst Case | O(d × (n + b)) | Determined by the largest value's digit count |
| Space Complexity | O(n + b) | Output array plus b counters |

Since d is effectively constant for fixed-width integers, this is often quoted
as linear time — but the constant factor hidden in d is real, and Radix Sort
frequently loses to a good Quick Sort on modest inputs.

## 🎯 Algorithm Characteristics

- **Type**: Non-comparison / Distribution Sort
- **Stability**: ✅ Stable (and it depends on this to work at all)
- **In-place**: ❌ No (needs an output array per pass)
- **Adaptive**: ❌ No

## 📁 Files

- [`radix_sort.py`](./radix_sort.py) — implementation with commentary
- [`radix_sort.html`](./radix_sort.html) — interactive animation showing one digit pass at a time, open it in any browser
