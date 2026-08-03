# Sorting Algorithms

Eleven classic sorting algorithms implemented in Python, explained with
step-by-step commentary and interactive visualizations.

Every algorithm lives in its own folder containing:

- A Python script with the full implementation and detailed comments.
- A `README.md` with complexity analysis and the algorithm's characteristics.
- A self-contained HTML animation you can open straight in a browser.

A [landing page](index.html) links everything together, and the
[benchmark](./benchmark) measures how the implementations actually perform
against each other.

## List of Sorting Algorithms

| Algorithm | Folder | Worst Case | Space | Stable | In-Place | Visualization |
|---|---|---|---|---|---|---|
| Bubble Sort | [Bubble sort](./Bubble%20sort) | O(n²) | O(1) | Yes | Yes | [Yes](./Bubble%20sort/bubble_sort.html) |
| Insertion Sort | [Insertion sort](./Insertion%20sort) | O(n²) | O(1) | Yes | Yes | [Yes](./Insertion%20sort/insertion_sort.html) |
| Selection Sort | [Selection sort](./Selection%20sort) | O(n²) | O(1) | No | Yes | [Yes](./Selection%20sort/selection_sort.html) |
| Shell Sort | [Shell sort](./Shell%20sort) | O(n²) | O(1) | No | Yes | [Yes](./Shell%20sort/shell_sort.html) |
| Merge Sort | [Merge sort](./Merge%20sort) | O(n log n) | O(n) | Yes | No | [Yes](./Merge%20sort/merge_sort.html) |
| Quick Sort | [Quick sort](./Quick%20sort) | O(n²) | O(log n) | No | Yes | [Yes](./Quick%20sort/quick_sort.html) |
| Heap Sort | [Heap sort](./Heap%20sort) | O(n log n) | O(1) | No | Yes | [Yes](./Heap%20sort/heap_sort.html) |
| Tim Sort | [Tim sort](./Tim%20sort) | O(n log n) | O(n) | Yes | No | [Yes](./Tim%20sort/tim_sort.html) |
| Counting Sort | [Counting sort](./Counting%20sort) | O(n + k) | O(n + k) | Yes | No | [Yes](./Counting%20sort/counting_sort.html) |
| Radix Sort | [Radix sort](./Radix%20sort) | O(d(n + b)) | O(n + b) | Yes | No | [Yes](./Radix%20sort/radix_sort.html) |
| Bucket Sort | [Bucket sort](./Bucket%20sort) | O(n²) | O(n + k) | Yes | No | [Yes](./Bucket%20sort/bucket_sort.html) |

Where the complexity depends on a parameter: **k** is the range of values,
**d** the number of digits, **b** the numeric base.

> **On Shell Sort's worst case:** this repository uses Shell's original halving
> gap sequence, whose worst case is O(n²). Better sequences (Ciura, Sedgewick)
> reach O(n^4/3) or better, at the cost of readability.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/amineTNYT/Sorting-algorithms.git
   cd Sorting-algorithms
   ```

2. Run any algorithm directly — each script has a small demo built in:

   ```bash
   python "Bubble sort/bubble_sort.py"
   python "Merge sort/merge_sort.py"
   ```

3. Or import one into your own code. Every algorithm sorts a list **in place**
   and returns `None`:

   ```python
   from algorithms import loadAlgorithms

   for spec, sort in loadAlgorithms():
       data = [5, 2, 9, 1, 7]
       sort(data)
       print(f"{spec.name}: {data}")
   ```

   `algorithms.py` exists because the folder names contain spaces, which a plain
   `import` statement cannot handle. It loads each implementation by path and is
   what the benchmark and the tests both use — so they measure and verify the
   exact code in these folders, never a second copy.

4. Open the visualizations in a browser — they are self-contained HTML files
   with no build step and no dependencies:

   ```bash
   start "Bubble sort/bubble_sort.html"     # Windows
   open "Bubble sort/bubble_sort.html"      # macOS
   ```

## Benchmarking

The [`benchmark`](./benchmark) folder compares real execution time across all
eleven algorithms on identical input.

```bash
pip install -r requirements.txt
python benchmark/benchmark.py
```

The O(n²) algorithms are skipped above 2,000 elements by default, so a full run
takes about a minute rather than several hours. See the
[benchmark README](./benchmark/README.md) for the available options.

## Tests

Every implementation is checked against the same suite — edge cases, randomized
input, float handling, stability, and deep-recursion safety:

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Time & Space Complexity (Quick Guide)

**Time complexity** describes how running time grows as the input size (**n**)
increases.

- **Best case** — the most favourable input, for example already sorted data
- **Average case** — typical or random input
- **Worst case** — the most unfavourable input

**Space complexity** describes how much additional memory an algorithm needs
beyond the input itself.

Two further properties matter as much as complexity in practice:

- **Stable** — equal elements keep their original relative order. This matters
  when sorting records by one field after already sorting by another.
- **In-place** — the algorithm needs only O(1) or O(log n) extra memory rather
  than a second copy of the data.

## Project Structure

```
Sorting-algorithms/
├── index.html            Landing page linking every algorithm
├── algorithms.py         Registry that loads each implementation by path
├── requirements.txt      Dependencies for the benchmark and tests
├── assets/               Shared styling and animation engine for the pages
├── <Algorithm> sort/     One folder per algorithm
│   ├── <algorithm>_sort.py
│   ├── <algorithm>_sort.html
│   └── README.md
├── benchmark/            Performance comparison and chart
└── tests/                Shared correctness suite
```

**Conventions:** files are lowercase with underscores (`bubble_sort.py`);
functions are camelCase (`bubbleSort`).

## License

[MIT](LICENSE) © Amine Benabdallah
