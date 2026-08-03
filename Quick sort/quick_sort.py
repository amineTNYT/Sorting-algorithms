"""Quick Sort - partition around a pivot, then sort each side recursively.

Uses Lomuto partitioning with a randomly chosen pivot. The randomisation is
what keeps sorted and reverse-sorted input from degenerating into O(n^2) time
and n-deep recursion; with a fixed last-element pivot, sorting an already
sorted list of a few thousand items raises RecursionError.
"""

import random


def swap(arr: list, i: int, j: int) -> None:
    """Exchange the elements at positions i and j."""
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: list, low: int, high: int) -> int:
    """Partition arr[low..high] around a pivot and return the pivot's index.

    Every element left of the returned index is smaller than the pivot, and
    every element right of it is greater than or equal to the pivot.
    """
    # Pick a random pivot and park it at the end, where Lomuto expects it
    swap(arr, random.randint(low, high), high)
    pivot = arr[high]

    # i tracks the right position of the pivot found so far. Elements from
    # low to i are smaller than the pivot after every iteration.
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move the pivot just after the smaller elements and report its position
    swap(arr, i + 1, high)
    return i + 1


def quickSort(arr: list, low: int = 0, high: int | None = None) -> None:
    """Sort arr[low..high] in place. O(n log n) on average.

    `high` is inclusive and defaults to the last index, so both
    quickSort(arr) and quickSort(arr, 0, len(arr) - 1) work.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:

        # pi is the final resting index of the pivot
        pi = partition(arr, low, high)

        # The pivot is already in place, so recurse on each side of it
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]

    print("Original array: ", end="")
    printArray(arr)

    quickSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
