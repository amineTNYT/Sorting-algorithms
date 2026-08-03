"""Counting Sort - tally how often each value occurs, then rebuild the array.

This is not a comparison sort: it never compares two elements against each
other, which is how it beats the O(n log n) lower bound. The trade-off is that
it only works on integers and costs O(k) memory, where k is the spread between
the smallest and largest value. Sorting [1, 1000000] would allocate a million
counters, so this is only a good fit when the range is narrow.
"""


def countingSort(arr: list) -> None:
    """Sort a list of integers in place. O(n + k) time and O(n + k) space."""
    if not arr:
        return

    minVal = min(arr)
    maxVal = max(arr)
    rangeSize = maxVal - minVal + 1

    # counts[v - minVal] holds how many times v appears. The offset lets this
    # handle negative numbers without a separate code path.
    counts = [0] * rangeSize
    for value in arr:
        counts[value - minVal] += 1

    # Turn counts into running totals, so counts[i] becomes the index just past
    # where the last copy of that value belongs
    for i in range(1, rangeSize):
        counts[i] += counts[i - 1]

    # Walk the input backwards and place each element at its computed index.
    # Going backwards is what keeps equal elements in their original order.
    output = [0] * len(arr)
    for value in reversed(arr):
        counts[value - minVal] -= 1
        output[counts[value - minVal]] = value

    arr[:] = output


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]

    print("Original array: ", end="")
    printArray(arr)

    countingSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
