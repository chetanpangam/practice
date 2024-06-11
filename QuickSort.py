def partition(arr, low, high):
    pivot = arr[high]

    pointer = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            pointer += 1
            (arr[pointer], arr[i]) = (arr[i], arr[pointer])
        
    (arr[pointer + 1], arr[high]) = (arr[high], arr[pointer + 1])

    return pointer + 1


def quicksort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr = [4, 2 , 5, 1, 1, 3]
print("Unsorted Array")
print(arr)
quicksort(arr, 0 , len(arr) - 1)
print('Sorted Array in Ascending Order:')
print(arr)