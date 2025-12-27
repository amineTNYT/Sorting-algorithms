def shell_sort(arr):
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


# Utility function to print array
def print_array(arr):
    print(" ".join(map(str, arr)))

 
if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3] 

    shell_sort(arr)
    print_array(arr)
