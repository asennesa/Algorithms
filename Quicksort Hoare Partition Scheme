def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[(lo + hi) // 2]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        
        
# Define the array to be sorted
arr = [3, 7, 2, 9, 1, 8, 4, 5, 6]

# Sort the array using quicksort
quicksort(arr, 0, len(arr) - 1)

# Print the sorted array
print(arr)


# The time complexity of the quicksort algorithm using Hoare partition scheme is O(n log n) in the average and best case, and O(n^2) in the worst case.
# In terms of space complexity, the algorithm uses O(log n).
