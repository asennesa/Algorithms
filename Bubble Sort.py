# Here's an implementation of the Bubble Sort algorithm in Python:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])
    
# In this implementation, arr is the array to be sorted. The bubble_sort function takes this array as its argument and modifies it in place.
# The algorithm works by comparing adjacent elements in the array and swapping them if they are in the wrong order. This process is repeated until the array is sorted.
# The outer loop of the algorithm runs n times, where n is the length of the array. The inner loop compares adjacent elements in the array and swaps them if necessary.
# After each pass through the array, the largest element "bubbles up" to the end of the array, so the inner loop only needs to iterate over the remaining unsorted elements.
# Once the sorting is complete, the sorted array is printed using a simple for loop.

# The space complexity of bubble sort is O(1), meaning that it uses a constant amount of additional memory to sort an array of n elements.
# The time complexity of bubble sort is O(n^2), meaning that it takes a quadratic amount of time to sort an array of n elements.
