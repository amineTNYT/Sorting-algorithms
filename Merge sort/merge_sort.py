"""Merge Sort - divide the array in half, sort each half, then merge them."""


def merge(arr: list, left: int, mid: int, right: int) -> None:
    """Merge the sorted halves arr[left..mid] and arr[mid+1..right] in place."""
    n1 = mid - left + 1
    n2 = right - mid

    # Copy both halves into temporary arrays
    leftHalf = arr[left:mid + 1]
    rightHalf = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Repeatedly take the smaller front element of the two halves.
    # Using <= (not <) is what makes this sort stable.
    while i < n1 and j < n2:
        if leftHalf[i] <= rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1
        k += 1

    # Copy whatever remains of the left half
    while i < n1:
        arr[k] = leftHalf[i]
        i += 1
        k += 1

    # Copy whatever remains of the right half
    while j < n2:
        arr[k] = rightHalf[j]
        j += 1
        k += 1


def mergeSort(arr: list, left: int = 0, right: int | None = None) -> None:
    """Sort arr[left..right] in place. Always O(n log n).

    `right` is inclusive and defaults to the last index, so both
    mergeSort(arr) and mergeSort(arr, 0, len(arr) - 1) work.
    """
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [38, 27, 43, 10]

    print("Original array: ", end="")
    printArray(arr)

    mergeSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
