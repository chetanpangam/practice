def getStrings(word):
    vowels = 'aeiou'
    strings = []
    i = 0
    while i < len(word):
        if word[i] not in vowels:
            i +=1
            continue
        else:
            j = i
            while j < len(word) and word[j] in vowels:
                j += 1
            
            if j-i >= 5:
                strings.append(word[i:j])
                
            i = j

    return strings

def countVowelSubstrings(word: str) -> int:
    strings = getStrings(word)
    print(strings)
    result = 0
    for s in strings:
        n = len(s)
        char_map = dict()
        start = end = 0
        while end < n and start < n:
            
            if s[end] not in char_map:
                char_map[s[end]] = 1
            else:
                char_map[s[end]] += 1
            
            if len(char_map) < 5:
                end += 1
            else:
                while len(char_map) >= 5 and start < end:
                    result += (n - end)
                    #print(result)
                    char_map[s[start]] -= 1

                    if char_map[s[start]] == 0:
                        del char_map[s[start]]
                    start += 1
                end +=1
            
        
    return result
            
#print(getStrings('ughspuuoaaaoieiuiaoiuee'))
print(countVowelSubstrings("ughspuuoaaaoieiuiaoiuee"))