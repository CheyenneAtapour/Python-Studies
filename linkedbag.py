class LinkedBag:
	def __init__(self):
		self.items = {}

	def insert(self, e):
		if e in self.items:
			self.items[e].append(e)
		else:
			self.items[e] = [e]

	def remove(self, e):
		if e in self.items:
			self.items[e].pop()
			if len(self.items[e]) == 0:
				self.items.pop(e)

	def print(self):
		for (k, v) in self.items.items():
			s = str(k) + ": "
			for val in v:
				s += str(val) + ", "
			s = s.rstrip(' ,')
			print(s)


x = LinkedBag()
x.insert(2)
x.insert(2)
x.insert(3)

x.print()
