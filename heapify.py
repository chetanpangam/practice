import heapq
 
n = 2
# initializing list
li = [5, 5, 7, 5, 9, 7, 1, 3]
# li = [1,1,1,2,2,3]

result = []
myDict = {}
myList = []
for val in li:
    myDict[val] = myDict.get(val, 0) + 1
 
# using heapify to convert list into heap
heapq.heapify(myList)
 
# using heappush() to push elements into heap
# pushes 4

for k, v in myDict.items():
    heapq.heappush(myList, (v,k))
 
# printing modified heap
print("The modified heap after push is : ", end="")
print(list(myList))
l = list(myList)

for k, v in enumerate(l):
    if k >= len(l) - n:
        result.append(v[1])

print(result)    


