"""Heap Sort - build a max-heap, then repeatedly extract the largest element."""


def heapify(arr: list, n: int, i: int) -> None:
    """Restore the max-heap property at index i, considering only arr[0..n-1].

    Assumes both children of i are already valid heaps.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # If a child was bigger, swap it up and keep sinking the old value
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr: list) -> None:
    """Sort `arr` in place. Always O(n log n), with O(1) extra space."""
    n = len(arr)

    # Build a max-heap. Leaves are already valid heaps, so start at the last
    # internal node and work backwards.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Swap the root (the largest remaining value) to the end of the unsorted
    # region, shrink that region by one, and repair the heap.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    print("Original array: ", end="")
    printArray(arr)

    heapSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
