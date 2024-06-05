# ProdOfArray.py
'''
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    result_left = [1] * n
    result_right = [1] * n
    answer = [1] * n

    # calculate products from left
    print(result_left)
    for i in range(1, n):
        result_left[i] = nums[i-1] * result_left[i-1]
    
    print(result_left)
    
    print(result_right)
    # calculate products from right
    for i in range(n-2, -1, -1):
        result_right[i] = nums[i+1] * result_right[i+1]
    print(result_right)
    
    # calculate the final answer: product array
    for i in range(n):
        answer[i] = result_left[i] * result_right[i]

    return answer
'''
def productExceptSelf(nums):
    result = [1] * len(nums)        
    for i in range(1, len(nums)):
        result[i] = nums[i-1] * result[i-1]
    right_prod = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= right_prod
        right_prod *= nums[i] 
    print(right_prod)
    return result

nums = [2,3,5,4]
print(nums)
print(productExceptSelf(nums))