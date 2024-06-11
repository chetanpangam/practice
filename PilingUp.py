from collections import deque

T = int(input())
input_list = []
for _ in range(T):
    tmp = input()
    dq = deque(map(int, input().split()))
    l = dq.popleft()
    r = dq.pop()
    while dq:
        print(f'l = {l}')
        print(f'r = {r}')
        if l <= r:
            r = dq.pop()
        elif r <= l:
            l = dq.popleft()
        else:
            break
    if len(dq) == 0:
        print("Yes")
    else:
        print("No")    