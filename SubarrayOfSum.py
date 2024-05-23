# SubarrayOfSum.py
# Find Subarray with given sum

def subArraySum(arr,len_arr, val):
    cur_sum = arr[0]
    start = 0
    if cur_sum == val:
        print(f"Sum found at index 0")
        return

    for i in range(1,len_arr):
        cur_sum += arr[i]
        if cur_sum > val:
            cur_sum -= arr[start]
            start += 1
        if cur_sum == val:
            print(f"Sum found at {start} to {i} index")
            return
    print("Sum not found")




if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23]
    len_arr = len(arr)
    val = 23
    subArraySum(arr, len_arr, val)

    arr1 = [8,2,4,0,6,9,1,2]
    val1 = 18
    len_arr1 = len(arr1)
    subArraySum(arr1, len_arr1, val1)