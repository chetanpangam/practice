s=input()
l=[]
for i in s:
    if not l:
        l.append(i)
    else:
        if(l[-1])==i:
            l.pop()
        else: 
            l.append(i) 

if not l: 
    print("empty string")
else: 
    print(''.join(l))

