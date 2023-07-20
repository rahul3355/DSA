# Heap

import heapq

minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0])

while len(minHeap):
	print(heapq.heappop(minHeap))



print("Max Heap")
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

print(-1 * maxHeap[0])
while len(maxHeap):
	print(-1 * heapq.heappop(maxHeap))



print("\nBuild Heap from List")
arr = [2,1,8,4,50]
heapq.heapify(arr)

while arr:
	print(heapq.heappop(arr))