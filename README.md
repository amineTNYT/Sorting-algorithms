# Sorting-algorithms

All sorting algorithms in Python explained with code and interactive visualizations.

This repository provides clear, well-commented Python implementations of the most common sorting algorithms. Each algorithm has its own dedicated folder containing:

- A Python script with the complete implementation and detailed step-by-step comments.
- An HTML file (`index.html`) that visually demonstrates how the algorithm works (using simple animations, step-by-step illustrations, or interactive elements powered by HTML/CSS/JavaScript).

## List of Sorting Algorithms

| Algorithm       | Folder Link                          | Time Complexity (Worst) | Stable | In-Place |
|-----------------|--------------------------------------|--------------------------|--------|----------|
| Bubble Sort     | [Bubble sort](./Bubble%20sort)       | O(n²)                   | Yes    | Yes      |
| Insertion Sort  | [Insertion sort](./Insertion%20sort) | O(n²)                   | Yes    | Yes      |
| Selection Sort  | [Selection sort](./Selection%20sort) | O(n²)                   | No     | Yes      |
| Merge Sort      | [Merge sort](./Merge%20sort)         | O(n log n)              | Yes    | No       |
| Quick Sort      | [Quick sort](./Quick%20sort)         | O(n²)                   | No     | Yes      |
| Shell Sort      | [Shell sort](./Shell%20sort)         | O(n log² n) or better   | No     | Yes      |
| Tim Sort        | [Tim sort](./Tim%20sort)             | O(n log n)              | Yes    | No       |

## 📊 Benchmarking

Feel free to benchmark and experiment with the different sorting algorithms provided in this repository.

The `benchmark` folder contains scripts for comparing algorithm performance on various input sizes and data distributions.

👉 [Go to the benchmark folder](https://github.com/amineTNYT/Sorting-algorithms/tree/main/benchmark)

## 📈 Time & Space Complexity (Quick Guide)

**Time Complexity** describes how the running time of an algorithm grows as the input size (**n**) increases.

- **Best Case**: The most favorable input (e.g. already sorted data)
- **Average Case**: Typical or random input
- **Worst Case**: The most unfavorable input

**Space Complexity** describes how much additional memory an algorithm uses beyond the input data.

These concepts help compare algorithms and choose the most suitable one based on performance and memory constraints.


## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/amineTNYT/Sorting-algorithms.git
   cd Sorting-algorithms
