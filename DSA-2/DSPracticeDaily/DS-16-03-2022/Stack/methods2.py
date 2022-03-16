from collections import deque


class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, data):
		self.container.append(data)
		
	def display(self):
		print(self.container)

	def pop(self):
		self.container.pop()
	
	def peek(self):
		return self.container[-1]
	
	def size(self):
		return len(self.container)

	def is_empty(self):
		return len(self.container) == 0 

s = Stack()
s.push(33)
s.push(32)
s.push(22)
s.push(90)
s.display()
print(s.size())
print(s.is_empty())
s.pop()
s.pop()
s.peek()
s.display()