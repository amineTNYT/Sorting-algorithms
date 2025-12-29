import random
import time
import os
import matplotlib.pyplot as plt

# ============================================================
# SORTING ALGORITHM IMPLEMENTATIONS
# ============================================================

def bubble_sort(arr):
    """Bubble Sort - O(n²) - In-place"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """Insertion Sort - O(n²) - Efficient for nearly sorted lists"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """Selection Sort - O(n²) - In-place"""
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr):
    """Merge Sort - O(n log n) - Stable - Returns new list"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """Quick Sort - O(n log n) average - NOT in-place (functional version)"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def shell_sort(arr):
    """Shell Sort - Improved Insertion Sort using simple gap sequence"""
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def tim_sort(arr):
    """Python built-in TimSort (C-optimized)"""
    return sorted(arr)


# ============================================================
# ALGORITHMS DICTIONARY
# ============================================================

algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Shell Sort": shell_sort,
    "Tim Sort (Python Built-in)": tim_sort,
}

# ============================================================
# BENCHMARK PARAMETERS
# ============================================================

sizes = [100, 500, 1000, 2500, 5000, 10000, 20000]
repeats = 5

results = {name: [] for name in algorithms}

print("🚀 Starting sorting algorithms benchmark...\n")

# ============================================================
# BENCHMARK EXECUTION
# ============================================================

for size in sizes:
    print(f"Testing with list size: {size}")

    for algorithm_name, algorithm_function in algorithms.items():
        total_time = 0.0

        for _ in range(repeats):
            # Generate base data ONCE per run
            base_data = [random.randint(0, size * 3) for _ in range(size)]
            data_copy = base_data.copy()

            start_time = time.perf_counter()
            result = algorithm_function(data_copy)
            elapsed = time.perf_counter() - start_time
            total_time += elapsed

            # Handle algorithms that return a new list
            if result is not None:
                data_copy[:] = result

            # Verify correctness
            assert data_copy == sorted(base_data), f"{algorithm_name} failed!"

        average_time = total_time / repeats
        results[algorithm_name].append(average_time)

        print(f"  {algorithm_name}: {average_time:.6f} seconds")

    print()

# ============================================================
# GRAPH GENERATION
# ============================================================

plt.figure(figsize=(12, 8))

for algorithm_name, times in results.items():
    plt.plot(sizes, times, marker='o', linewidth=2, label=algorithm_name)

plt.title("Sorting Algorithms Performance Comparison", fontsize=16)
plt.xlabel("Input Size (n)", fontsize=12)
plt.ylabel("Average Execution Time (seconds)", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, alpha=0.3)

# Log-log scale for complexity visualization
plt.xscale("log")
plt.yscale("log")

plt.tight_layout()

# ============================================================
# SAVE RESULTS
# ============================================================

base_directory = os.path.dirname(__file__) if "__file__" in globals() else os.getcwd()
output_directory = os.path.join(base_directory, "results")
os.makedirs(output_directory, exist_ok=True)

output_path = os.path.join(output_directory, "sorting_performance.png")
plt.savefig(output_path)
plt.close()

print("✅ Benchmark completed successfully!")
print(f"📊 Graph saved at: {output_path}")
print("💡 Tip: Add this graph to your main README for strong visual impact.")
