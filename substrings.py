# substrings.py

s = input()

s_len = len(s)


for i in range(s_len + 1):
    for j in range(i+1, s_len+1):
        print(s[i:j])
    