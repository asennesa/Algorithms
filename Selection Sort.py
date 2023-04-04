def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
  
  
my_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(my_array)
print(sorted_array)

# The space complexity of the Selection Sort algorithm is O(1) because the algorithm sorts the array in place without using any additional data structures.
# The time complexity of the Selection Sort algorithm is O(n^2), where n is the number of elements in the input array.
