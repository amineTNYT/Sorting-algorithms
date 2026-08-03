"""Bubble Sort - repeatedly swap adjacent elements that are out of order."""


def bubbleSort(arr: list) -> None:
    """Sort `arr` in place. O(n) on already-sorted input, O(n^2) otherwise."""
    n = len(arr)
    for i in range(n):

        # Track whether this pass changed anything
        swapped = False

        # The last i elements are already in their final position
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # A pass with no swaps means the array is already sorted
        if not swapped:
            break


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", end="")
    printArray(arr)

    bubbleSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
