"[2,7,1,-3,8,9] find the max absolute diff b/w two elements , Write unit tests for the same"

def maxAbsDifference(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements.")
    
    min_val = float('INF')
    max_val = -float('INF')

    for val in arr:
        if min_val > val:
            min_val = val
        
        if max_val < val:
            max_val = val

    return abs(max_val - min_val)

#arr = [2,7,1,-3,8,9]
arr = [-5, 0, 5]
arr = [-10, -20, -30, -40, -50]
arr = [1, -1]
arr = [1]
print("Max abs difference: ", maxAbsDifference(arr))