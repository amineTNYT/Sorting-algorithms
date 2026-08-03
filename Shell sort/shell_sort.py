"""Shell Sort - insertion sort applied over progressively smaller gaps.

Uses Shell's original halving gap sequence (n/2, n/4, ... 1). It is the easiest
sequence to follow, but it is also the reason this implementation has an O(n^2)
worst case; sequences such as Ciura's or Sedgewick's do better at the cost of
readability.
"""


def shellSort(arr: list) -> None:
    """Sort `arr` in place using the halving gap sequence."""
    n = len(arr)

    gap = n // 2
    while gap > 0:

        # Perform a "gapped" insertion sort for this gap size
        for i in range(gap, n):

            # Current element to be placed correctly
            temp = arr[i]
            j = i

            # Shift earlier elements that are greater than temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Place temp in its correct position
            arr[j] = temp

        # Reduce the gap
        gap //= 2


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]

    print("Original array: ", end="")
    printArray(arr)

    shellSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
