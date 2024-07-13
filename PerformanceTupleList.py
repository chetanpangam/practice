import time

t = tuple(range(1,100000000))
l = list(range(1,100000000))


t1= time.time()
for i in t:
    continue
t2 = time.time()

print(t2-t1)

print("=============================")
l1= time.time()
for i in l:
    continue
l2 = time.time()

print(l2-l1)