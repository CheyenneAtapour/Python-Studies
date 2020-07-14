# the following code reverses a linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def reverse (node):
	if (node == None or node.next == None):
		return node
	node1 = reverse(node.next)
	node.next.next = node
	node.next = None
	return node1