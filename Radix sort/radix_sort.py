"""Radix Sort - sort integers one digit at a time, least significant first.

Each pass is a counting sort on a single digit. Because counting sort is
stable, the ordering established by earlier (less significant) digits survives
later passes, and after the final pass the whole array is sorted.
"""

BASE = 10


def countingSortByDigit(arr: list, exp: int) -> None:
    """Stable-sort `arr` in place by the digit selected by `exp` (1, 10, 100...)."""
    n = len(arr)
    counts = [0] * BASE

    for value in arr:
        digit = (value // exp) % BASE
        counts[digit] += 1

    # Running totals give each digit its end position in the output
    for i in range(1, BASE):
        counts[i] += counts[i - 1]

    # Walk backwards to preserve the order of equal digits (stability)
    output = [0] * n
    for value in reversed(arr):
        digit = (value // exp) % BASE
        counts[digit] -= 1
        output[counts[digit]] = value

    arr[:] = output


def radixSort(arr: list) -> None:
    """Sort a list of integers in place. O(d * (n + b)) for d digits in base b."""
    if not arr:
        return

    # Digit extraction assumes non-negative values, so split the array, sort
    # the magnitudes of the negatives, and lay them back down reversed.
    negatives = [-value for value in arr if value < 0]
    positives = [value for value in arr if value >= 0]

    for part in (negatives, positives):
        if part:
            maxVal = max(part)
            exp = 1
            while maxVal // exp > 0:
                countingSortByDigit(part, exp)
                exp *= BASE

    arr[:] = [-value for value in reversed(negatives)] + positives


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    print("Original array: ", end="")
    printArray(arr)

    radixSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
