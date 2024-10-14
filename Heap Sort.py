def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Input handling
given_element = list(map(int, input("Enter the elements separated by spaces: ").split()))

print(f"Given array: {given_element}")

# Sorting and output
heap_sort(given_element)
print(f"Sorted Array: {given_element}")
