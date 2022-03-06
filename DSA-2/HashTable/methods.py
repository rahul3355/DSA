class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(self.MAX)]

	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val
	
	def __getitem__(self, key):
		h = self.get_hash(key)
		return self.arr[h]
	
	def _delitem__(self, key):
		h = self.get_hash(key)
		self.arr[h] = None

t = HashTable()
t['march 6'] = 130
t['march 7'] = 444
t['dec 3'] = 1333
t['iiii'] = 1
print(t.arr)