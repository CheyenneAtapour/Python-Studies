class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
from collections import defaultdict

def lca(root, v1, v2):
  #Enter your code here
  dict = defaultdict(list)
  dict[root.info].append(root)
  found1 = False
  found2 = False
  l = [root]
  while len(l) > 0 and (not found1 or not found2):
    temp = l.pop(0) # put the kids in the dictionary
    if temp.info == v1:
        found1 = True
    elif temp.info == v2:
        found2 = True
    if not temp.right == None:
        l.append(temp.right) # BFS
        temp2 = dict[temp.info].copy() # store the path to this node
        temp2.append(temp.right)
        dict[temp.right.info] = temp2 # put path to this node in dictionary
    if not temp.left == None:
        l.append(temp.left)
        temp2 = dict[temp.info].copy()
        temp2.append(temp.left)
        dict[temp.left.info] = temp2
  # we now have all the paths to each node
  temp = dict[v1]
  dict2 = {}
  for x in range(len(temp)):
    dict2[temp[x]] = temp[x]
  temp = dict[v2]
  temp.reverse()
  for x in range(len(temp)):
    if temp[x] in dict2:
        return temp[x]
  return None
  

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
