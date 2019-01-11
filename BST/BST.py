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

	def inOrder(self):
		if not self.isEmpty():
			self._inorder_(self.root)
	def _inorder_(self,node):
		if not node is None:
			self._inorder_(node.left)
			print(node.data)
			self._inorder_(node.right)
	def level_order(self):
		import FlexiQueue
		l=[]
		if not self.isEmpty():
			q=FlexiQueue.FlexiQueue()
			q.enqueue(self.root)
			for i in range(q.length()):
				if not q.isEmpty():
					current=q.dequeue()
					l.append(current.data)
					if not current.left is None:
						q.enqueue(current.left)
					if not current.right is None:
						q.enqueue(current.right)
			return l
	def preOrder(self):
		if not self.isEmpty():
			self._preOrder_(self.root)
	
	def _preOrder_(self,node):
		if not node is None:
			print(node.data)
			self._preOrder_(node.left)
			self._preOrder_(node.right)
	def postOrder(self):
		if not self.isEmpty():
			self._postOrder_(self.root)
	def _postOrder_(self,node):
		if not node is None:
			self._postOrder_(node.left)
			self._postOrder_(node.right)
			print(node.data)
	
	def delete_node(self,key):
		if not self.isEmpty():
			self.root=self._delete_(self.root,key)
		
	def _delete_(self,node,key):
		if node is None:
			return node
		elif key<node.data:
			node.left=self._delete_(node.left,key)
		elif key>node.data:
			node.right=self._delete_(node.right,key)
		elif(node.left and node.right):
			temp=self.minValue(node.right)
			node.data=temp
			node.right=self._delete_(node.right,key)
		else:
			if node.left is None:
				node=node.right
			else:
				node=node.left
			self.count-=1
		return node
	
	def minValue(self,node):
		if node.left is None:
			return node
		else:
			return self.minValue(node.left)
	
	def height(self):
		if not self.isEmpty():
			return self._height_(self.root)
	
	def _height_(self,node):
		if node is None:
			return 0
		else:
			return max(self._height_(node.left), self._height_(node.right))+1

	def desc(self):
		if not self.isEmpty():
			self._desc_(self.root)
	def _desc_(self,node):
		if not node is None:
			self._desc_(node.right)
			print(node.data)
			self._desc_(node.left)

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
	
	def findMin(self):
		if not self.isEmpty():
			return self._findMin_(self.root)
	def _findMin_(self,node):
		current = node 
		while(current.left is not None): 
			current = current.left 
		return current.data
	def findMax(self):
		if not self.isEmpty():
			return self._findMax_(self.root)
	def _findMax_(self,node):
		current = node 
		while(current.right is not None):
			current = current.right
		return current.data
	def lefttree(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.lefttree(node.left)+self.lefttree(node.right))

	def righttree(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.righttree(node.left)+self.righttree(node.right))

	def treecount(self):
		if not self.isEmpty():
			node=self.root
			a=self.lefttree(node.left)
			b=self.righttree(node.right)
			return (a,b)