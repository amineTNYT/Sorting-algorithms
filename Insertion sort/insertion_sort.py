"""Insertion Sort - grow a sorted prefix by inserting each element into place."""


def insertionSort(arr: list) -> None:
    """Sort `arr` in place. O(n) on already-sorted input, O(n^2) otherwise."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift every element greater than key one position to the right,
        # opening a slot for key inside the sorted prefix arr[0..i-1]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    print("Original array: ", end="")
    printArray(arr)

    insertionSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
