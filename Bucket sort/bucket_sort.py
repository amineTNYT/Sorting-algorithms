"""Bucket Sort - scatter values into ordered buckets, sort each, concatenate.

Fast when the input is spread evenly across its range: each bucket stays small,
so the per-bucket insertion sort barely costs anything. Heavily skewed input
piles everything into one bucket and degrades to O(n^2).
"""


def insertionSort(bucket: list) -> None:
    """Sort a single bucket in place; buckets are expected to be small."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucketSort(arr: list) -> None:
    """Sort a list of numbers in place. O(n + k) average, O(n^2) worst case."""
    n = len(arr)
    if n <= 1:
        return

    minVal = min(arr)
    maxVal = max(arr)

    # Every value is identical, so there is nothing to order
    if minVal == maxVal:
        return

    # Use n buckets and map each value to one by its position in the range.
    # Scaling by (n - 1) / span keeps maxVal inside the last bucket.
    buckets = [[] for _ in range(n)]
    span = maxVal - minVal
    for value in arr:
        index = int((value - minVal) * (n - 1) / span)
        buckets[index].append(value)

    # Buckets are already in ascending order relative to each other, so sorting
    # each one and concatenating gives the fully sorted array
    result = []
    for bucket in buckets:
        insertionSort(bucket)
        result.extend(bucket)

    arr[:] = result


def printArray(arr: list) -> None:
    """Print the array on a single space-separated line."""
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]

    print("Original array: ", end="")
    printArray(arr)

    bucketSort(arr)

    print("Sorted array:   ", end="")
    printArray(arr)
