def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort the elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Pivot is chosen as the last element
    pivot = arr[high]
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Input handling
given_element = list(map(int, input("Enter the elements separated by spaces: ").split()))

print(f"Given array: {given_element}")

# Sorting and output
quick_sort(given_element, 0, len(given_element) - 1)
print(f"Sorted Array: {given_element}")
