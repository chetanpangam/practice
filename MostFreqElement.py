"""
Given a list nums return the most frequently occuring element
Input: nums = [1,1,1,2,2,3]
output : 1
"""


def findMostFreq(nums):
    counter_map = {}
    max_freq = -float("INF")
    result = 0
    for num in nums:
        counter_map[num] = counter_map.get(num, 0) + 1

    for k, v in counter_map.items():
        if max_freq < v:
            max_freq = v
            result = k
    
    return result


nums = [1,1,1,2,2,2,2,3]
print("Most frequent value: ", findMostFreq(nums))