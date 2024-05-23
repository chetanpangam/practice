# set_remove.py

def operation(s, op_name, val=None):
    print(op_name, val)
    if op_name =="remove" and val in s:
        s.remove(val)
    elif op_name == "discard":
        s.discard(val)
    elif "pop":
        s.pop()
            
n = 9
s = {1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9}
N = 3
key = None
for i in range(N):
    op, *val = input().split(" ")
    if val:
        key=int(val[0])
    operation(s, op, key)

print(sum(s))