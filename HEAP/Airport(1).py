class Min_Heap:
	def __init__(self,mylist=[]):
		self.data=[]
		self.data.append(mylist)
		self._buildheap()
	def isEmpty(self):
		return self.length()==0
	def length(self):
		return len(self.data)
	def _parent(self,j):
		return (j-1)//2
	def _left_child(self,j):
		return (2*j+1)
	def _right_child(self,j):
		return (2*j+2)
	def _swap(self,i,j):
		self.data[i], self.data[j] = self.data[j], self.data[i]
	def _upheap(self,j):
		parent = self._parent(j)
		if j > 0 and self.data[j][0] < self.data[parent][0]:
			self._swap(j,parent)
			self._upheap(parent)
	def _downheap(self,j,size):
		if self._left_child(j) < size:
			left = self._left_child(j)
			smallchild = left
			if self._right_child(j) < size:
				right = self._right_child(j)
				if self.data[right][0] < self.data[left][0]:
					smallchild = right
			if self.data[smallchild][0] < self.data[j][0]:
				self._swap(smallchild,j)
				self._downheap(smallchild,size)
	def _buildheap(self):
		start = (self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())
	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)
	def extracting_min(self):
		self._swap(0,self.length()-1)
		min_value = self.data.pop()
		self._downheap(0,self.length()-1)
		return min_value