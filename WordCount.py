from collections import Counter
from collections import OrderedDict


n= int(input())
l = []
result = OrderedDict()
for _ in range(n):
    l.append(input())

result = Counter(l)

print(len(result))

for val in result.values():
    print(val, end=" ")