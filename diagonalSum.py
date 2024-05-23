# diagonalSum.py
n = 4
m = 3
right_inclined_digsum = [0]*(n+m-1)
left_inclined_digsum = [0]*(n+m-1)
# Function for diagonal sum
 
 
def diagonal_sum(arr, right_inclined_digsum, left_inclined_digsum, n, x, y):
    # To make it compatible with 0 based indexing
    a = (n-x)+y-1
    b = x+y
    summ = right_inclined_digsum[b]+left_inclined_digsum[a]-arr[x][y]
    return summ
# Precomputaion function
 
 
def precompute(n, m, arr, right_inclined_digsum, left_inclined_digsum):
    # To cover all diagonals of (/) type
    for i in range(n):
        for j in range(m):
            right_inclined_digsum[i+j] += arr[i][j]
    # To cover all diagonals of (\) type
    for i in range(n-1, -1, -1):
        for j in range(0, m):
            left_inclined_digsum[n-1-i+j] += arr[i][j]
    # precomputaion done
 
 
def solve(arr, Q, query):
    # Function for precomputation
    precompute(n, m, arr, right_inclined_digsum, left_inclined_digsum)
    # Iterator for these coordinates
    x, y = query[0]
    print(diagonal_sum(arr, right_inclined_digsum,
                           left_inclined_digsum, n, x, y))
 
 
# Drivers code
if __name__ == "__main__":
    arr = [[1, 2, 2, 1], [2, 4, 2, 4], [2, 2, 3, 1]]
    Q = 3
    # Defining coordinates for each query
    print(arr)
    query = []
    query.append([2, 2])
    # Function call
    print(query)
    solve(arr, Q, query)