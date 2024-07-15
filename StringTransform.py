"""
There is a string of length N made only of letters "a". Whenever there are two identical adjacent letters (e.g. "aa"), 
they can be transformed into a single letter that is the next letter of the alphabet. 
For example, "aa" can be transformed into "b" and "ee" into "f". However, "zz" cannot be further transformed.
What is the alphabetically largest string that can be obtained fror the initial string?

1. Given N = 11, the function should return "dba". The initial string
"aaaaaaaaaaa" can be transformed in the following manner:
"aaaaaaaaaaa" → "bbbbba" → "ccba" → "dba".
2. Given N = 1, the function should return "a". The initial string "a" cannot
be transformed in any way.
3. Given N = 67108876, the function should return "zzdc".
"""


class StringTransform:
    
    def stringTransform(self, n):
        string = 'a' * n
        result = ""
        curr_ch = 'a'

        while n > 0:

            rem = n % 2
            if rem == 1:
                result = curr_ch + result
            if curr_ch == 'z':
                result = n * 'z' + result
                break
            curr_ch = chr(ord(curr_ch) + 1) 
            n //=2

        return result
    
s = StringTransform()
print(s.stringTransform(11))
print(s.stringTransform(1))
print(s.stringTransform(67108876))


