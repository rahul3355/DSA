from collections import deque

class Queue:

	def __init__(self):
		self.buffer = deque()

	def enqueue(self, val):
		self.buffer.appendleft(val)

	def dequeue(self):
		self.buffer.pop()

	def is_empty(self):
		return len(self.buffer) == 0

	def size(self):
		return len(self.buffer)
		

pq = Queue()

pq.enqueue(34)
pq.enqueue(114)
pq.enqueue(564)
pq.enqueue(2344)

print(pq.buffer)

pq.dequeue()

print(pq.is_empty())

print(pq.size())

print(pq.buffer)