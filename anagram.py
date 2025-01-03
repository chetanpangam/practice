'''
Write a program to check if two strings are anagrams of each other.? - listen-silent, hear-hire, bored-robed.
'''
def isAnagram_1(s1, s2):
    if len(s1) != len(s2):
        return False
    
    counter = [0] * 26

    for i in range(len(s1)):
        counter[ord(s1[i].lower()) - 97] += 1
        counter[ord(s2[i].lower()) - 97] -= 1
    
    if any(counter):
        return False
    return True


def isAnagram(s1, s2):
    check = [0] * 26

    for val in s1:
        check[ord(val) - 97] += 1
    
    for val1 in s2:
        check[ord(val1) - 97] -= 1
    
    if any(check):
        return False
    
    return True


s1 = "hear"
s2 = "hire"

print(isAnagram(s1,s2))
print(isAnagram_1(s1,s2))

str1 = "Listen"
str2 = "Silent"
print(isAnagram(str1,str2))
print(isAnagram_1(str1,str2))