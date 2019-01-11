#Design a Binary Search Tree data structure in Python. It should have methods to add new element, search any element, find the height of tree, number of terminal nodes and traversal which takes through in ascending order.
class BST:
	class _TreeNode:
		def __init__(self,ele):
			self.data=ele
			self.left=None
			self.right=None
	def __init__(self):
		self.root=None
		self.count=0

	def add_node(self,ele):
		current = parent = self.root
		while current is not None and current.data != ele:
			#current=parent
			parent = current
			if ele < current.data:
				current = current.left
			elif ele > current.data:
				current = current.right
		if current is None:
			new_node = self._TreeNode(ele)
			if parent is None:
				self.root = new_node
			elif ele < parent.data:
				parent.left = new_node
			elif ele > parent.data:
				parent.right = new_node
			self.count += 1
	def node_count(self):
		return self.count
	def isEmpty(self):
		return self.count==0
	
	def Lookup(self,key):
		if not self.isEmpty():
			current=self.root
			while(current!=None):
				if key<current.data:
					current=current.left
				elif key>current.data:
					current=current.right
				else:
					break
			
			if current==None:
				return False
			else:
				return True
	def height(self):
		if not self.isEmpty():
			return self._height_(self.root)
	def _height_(self,node):
		if node is None:
			return 0
		else:
			return max(self._height_(node.left), self._height_(node.right))+1
	def terminalNodes(self):
		if not self.isEmpty():
			return self._terminalNodes_(self.root)
	def _terminalNodes_(self,node): 
		if node is None:
			return 0 
		if(node.left is None and node.right is None): 
			return 1 
		else: 
			return self._terminalNodes_(node.left) + self._terminalNodes_(node.right)
	def inOrder(self):
		if not self.isEmpty():
			self._inorder_(self.root)
	def _inorder_(self,node):
		if not node is None:
			self._inorder_(node.left)
			print(node.data)
			self._inorder_(node.right)

BST=BST()
BST.add_node(10)
BST.add_node(15)
BST.add_node(20)
BST.add_node(26)
BST.add_node(59)
BST.add_node(66)
BST.add_node(32)
BST.add_node(78)
BST.add_node(90)

print("SEARCH RESULT: ",BST.Lookup(10))
print("SEARCH RESULT: ",BST.Lookup(100))

print("HEIGHT: ",BST.height())

print("TERMINAL NODES: ",BST.terminalNodes())
print("ASCENDING ORDER")
BST.inOrder()


