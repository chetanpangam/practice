# hexcolor.py

import re
pattern = r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\S'

N= int(input())
valid_codes = []

while N > 0:
    line = input()
    result = re.findall(pattern, line)

    if len(result)>0:
        for j in result:
            valid_codes.append(j[1:])

    N -= 1

print("\n".join(valid_codes))

print("================")

