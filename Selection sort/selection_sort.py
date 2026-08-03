"""Selection Sort - repeatedly move the smallest remaining element into place."""


def selectionSort(arr: list) -> None:
    """Sort `arr` in place. Always O(n^2), regardless of input order."""
    n = len(arr)
    for i in range(n - 1):

        # Assume the current position holds the minimum element
        minIdx = i

        # Scan the unsorted portion for the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[minIdx]:
                minIdx = j

        # Move that minimum to its final position
        arr[i], arr[minIdx] = arr[minIdx], arr[i]


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Original array: ", end="")
    printArray(arr)

    selectionSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
