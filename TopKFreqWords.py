"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.


Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
"""
import heapq

def topKFrequent(words, k):
    result = []
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_list = sorted(word_count.items(), key=lambda x:(-x[1], x[0]))
    print(sorted_list)

    
    for i in range(k):
        result.append(sorted_list[i][0])


    return result

words = ["i","love","leetcode","i","love","coding"]
k = 2

print("result: ", topKFrequent(words, k))