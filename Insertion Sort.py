def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
        
arr = [5, 2, 8, 3, 1, 6, 9, 7, 4]

insertion_sort(arr)

print("Sorted array:", arr)



# The time complexity of the Insertion Sort algorithm is O(n^2), where n is the number of elements in the array.
# However, it is efficient for small input sizes and performs well on partially sorted arrays.

# It virtually splits the array into a sorted and an unsorted subarray.
# Initially, the sorted subarray consists of a single element — the first element — and the rest of the elements form the unsorted subarray. 
# Then, we iterate over the unsorted subarray elements, remove them from the unsorted subarray, and place them at the correct position in the sorted subarray.
# We repeat this until no element remains in the unsorted subarray, and we get the sorted array.
