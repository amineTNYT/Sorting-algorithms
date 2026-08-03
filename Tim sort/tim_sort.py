"""TimSort - a hybrid of Insertion Sort and Merge Sort.

This is a teaching implementation of the algorithm CPython uses internally for
`sorted()` and `list.sort()`. It finds naturally ordered "runs" in the data,
extends short ones with insertion sort, and merges them together.

MIN_RUN_THRESHOLD is 32 here to keep the demo readable; CPython uses 64, which
yields a minimum run length between 32 and 64.
"""

MIN_RUN_THRESHOLD = 32


def calcMinRun(n: int) -> int:
    """Return the minimum run length for an array of n elements.

    Shifts n right until it is below the threshold, rounding up if any bit was
    shifted out, so that the number of runs is close to a power of two.
    """
    r = 0
    while n >= MIN_RUN_THRESHOLD:
        r |= n & 1
        n >>= 1
    return n + r


def insertionSort(arr: list, left: int, right: int) -> None:
    """Sort the inclusive range arr[left..right] in place."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr: list, l: int, m: int, r: int) -> None:
    """Merge the sorted ranges arr[l..m] and arr[m+1..r] in place."""
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def findRun(arr: list, start: int, n: int) -> int:
    """Return the end index of the natural run beginning at `start`.

    A descending run is reversed in place so that every run this returns is
    ascending. Reversing rather than sorting is what keeps TimSort stable.
    """
    end = start + 1
    if end == n:
        return end

    if arr[end] < arr[start]:
        # Descending run - walk it out, then flip it
        while end < n and arr[end] < arr[end - 1]:
            end += 1
        arr[start:end] = reversed(arr[start:end])
    else:
        # Ascending run
        while end < n and arr[end] >= arr[end - 1]:
            end += 1

    return end


def timSort(arr: list) -> None:
    """Sort `arr` in place. O(n) on already-sorted input, O(n log n) otherwise."""
    n = len(arr)
    minRun = calcMinRun(n)
    runs = []

    i = 0
    while i < n:
        runEnd = findRun(arr, i, n)
        runLen = runEnd - i

        # Pad a short run up to minRun with insertion sort
        if runLen < minRun:
            end = min(i + minRun, n)
            insertionSort(arr, i, end - 1)
            runEnd = end

        runs.append((i, runEnd))
        i = runEnd

        # Collapse the run stack while the top run is at least as long as the
        # one beneath it, keeping merges balanced
        while len(runs) > 1:
            l1, r1 = runs[-2]
            l2, r2 = runs[-1]
            len1, len2 = r1 - l1, r2 - l2
            if len1 <= len2:
                merge(arr, l1, r1 - 1, r2 - 1)
                runs.pop()
                runs[-1] = (l1, r2)
            else:
                break

    # Merge whatever runs are left into one
    while len(runs) > 1:
        l1, r1 = runs[-2]
        l2, r2 = runs[-1]
        merge(arr, l1, r1 - 1, r2 - 1)
        runs.pop()
        runs[-1] = (l1, r2)


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 10, 1, 3, 2]

    print("Original array: ", end="")
    printArray(arr)

    timSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
