if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maxOfArr = max(arr)
    filteredArr = [x for x in arr if x != maxOfArr]
    print(max(filteredArr))