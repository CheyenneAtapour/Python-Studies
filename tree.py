class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


x = Tree(2)
x.right = Tree(3)
x.left = Tree(1)

def dfs(t: Tree):
	print(t.data)
	if t.left == None:
		return
	if t.right == None:
		return
	dfs(t.left)
	dfs(t.right)
	
dfs(x)