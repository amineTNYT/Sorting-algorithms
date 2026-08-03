# 🔢 Counting Sort Algorithm

## 📋 Overview

This folder contains an implementation of **Counting Sort**, a
**non-comparison** sorting algorithm for integers. Instead of comparing
elements against each other, it counts how many times each value occurs and
uses those tallies to place every element directly at its final index.

Because it never compares two elements, it is not bound by the Ω(n log n) lower
limit that applies to all comparison sorts.

## 🔍 How Counting Sort Works

1. Find the minimum and maximum values to determine the range **k**
2. Count occurrences of each value into a tally array
3. Convert the tallies into running totals, so each entry says where that
   value's block ends in the output
4. Walk the input **backwards**, placing each element at its computed index and
   decrementing the total

Step 4 goes backwards on purpose: that is what makes the sort stable. Walking
forwards would reverse the relative order of equal elements.

The implementation offsets by the minimum value, so negative numbers work
without a separate code path.

## 📊 Time & Space Complexity

| Case | Complexity | Notes |
|---|---|---|
| Best Case | O(n + k) | k is the range of values |
| Average Case | O(n + k) | Independent of input order |
| Worst Case | O(n + k) | No degradation |
| Space Complexity | O(n + k) | Tally array plus output array |

## ⚠️ Limitations

- **Integers only** — the values are used directly as array indices
- **Range matters more than count** — sorting `[1, 1000000]` allocates a million
  counters to sort two elements. Counting Sort is only a good fit when k is
  comparable to n.

## 🎯 Algorithm Characteristics

- **Type**: Non-comparison / Distribution Sort
- **Stability**: ✅ Stable (thanks to the backwards placement pass)
- **In-place**: ❌ No (needs a separate output array)
- **Adaptive**: ❌ No

## 📁 Files

- [`counting_sort.py`](./counting_sort.py) — implementation with commentary
- [`counting_sort.html`](./counting_sort.html) — interactive animation showing the tally being built and read back, open it in any browser

> Counting Sort is also the engine inside [Radix Sort](../Radix%20sort), which
> applies it to one digit at a time to handle large value ranges efficiently.
