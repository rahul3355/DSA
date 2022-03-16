from collections import deque

class Queue:
	def __init__(self):
		self.buffer = deque()

	def enqueue(self, data):
		self.buffer.appendleft(data)
	
	def dequeue(self):
		self.buffer.pop()
		
	def is_empty(self):
		return len(self.buffer) == 0
		
	def size(self):
		return len(self.buffer)
	
	def display(self):
		print(self.buffer)

q = Queue()
q.enqueue(33)
q.enqueue(22)
q.enqueue(56)
q.display()
print(q.size())
print(q.is_empty())
q.dequeue()
q.dequeue()
q.display()