# heapoperations.py

import heapq

minHeap = []

heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap,1)
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,7)

print(minHeap)

while len(minHeap):
	print(heapq.heappop(minHeap))


arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
print(arr)

while len(arr):
	print(heapq.heappop(arr))

print("++++++++++++++++++")
maxHeap = []
heapq.heappush(maxHeap, 3*-1)
heapq.heappush(maxHeap, 2*-1)
heapq.heappush(maxHeap, 4*-1)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))