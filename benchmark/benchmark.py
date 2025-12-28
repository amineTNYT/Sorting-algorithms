import time
import random
import matplotlib.pyplot as plt
import os

# ==================== IMPLÉMENTATIONS DES ALGORITHMES DE TRI ====================

def bubble_sort(arr):
    """Bubble Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    """Insertion Sort - O(n²) best for sorted lists,array etc"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    """Selection Sort - O(n²)"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    """Merge Sort - O(n log n), stable"""
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
    """Quick Sort - O(n log n)  in-place"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shell_sort(arr):
    """Shell Sort - a better  implimantationof insertion sort"""
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
    """Utilise la fonction native sorted() de Python qui implémente TimSort"""
    return sorted(arr)

# ==================== DICTIONNAIRE DES ALGORITHMES À TESTER ====================

algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Shell Sort": shell_sort,
    "Tim Sort (Python built-in)": tim_sort,
}

# ==================== PARAMETERS OF THE BENCHMARK ====================

sizes = [100, 500, 1000, 2500, 5000, 10000, 20000]  # augmente jusqu'à 20k pour voir les différences
repeats = 5  # nombre de runs par taille pour moyenne fiable

results = {name: [] for name in algorithms.keys()}

print("🚀 Démarrage du benchmark des algorithmes de tri...\n")

for size in sizes:
    print(f"Test en cours avec {size} éléments...")
    for name, func in algorithms.items():
        total_time = 0.0
        for _ in range(repeats):
            # Données aléatoires
            data = [random.randint(0, size * 3) for _ in range(size)]
            data_copy = data.copy()

            start_time = time.perf_counter()
            func(data_copy)  # on trie une copie
            total_time += time.perf_counter() - start_time

        avg_time = total_time / repeats
        results[name].append(avg_time)
        print(f"   {name}: {avg_time:.6f} secondes")

# ==================== GÉNÉRATION DU GRAPHIQUE ====================

plt.figure(figsize=(12, 8))

for name, times in results.items():
    plt.plot(sizes, times, label=name, marker='o', linewidth=2)

plt.title("Comparaison des performances des algorithmes de tri", fontsize=16)
plt.xlabel("Taille de la liste (n)", fontsize=12)
plt.ylabel("Temps moyen d'exécution (secondes)", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, alpha=0.3)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()

# Création du dossier results et sauvegarde
output_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "performance_chart.png")

plt.savefig(output_path)
plt.close()
print("\n✅ Benchmark completed!")
print(f"📊 Graph saved here: {output_path}")
print(" Add this graph to your main README for maximum impact!")
