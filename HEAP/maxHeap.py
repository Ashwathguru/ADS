#1. Build maximum heap with required methods. It should support the behaviors like adding element, getting maximum element, extracting maximum element, count number of elements and to check the method to test the heap order property.
class Max_Heap:
	def __init__(self,mylist=[]):
		self.data = mylist
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
		if j > 0 and self.data[j] > self.data[parent]:
			self._swap(j,parent)
			self._upheap(parent)
	def _downheap(self,j,size):
		if self._left_child(j) < size:
			left = self._left_child(j)
			bigchild = left
			if self._right_child(j) < size:
				right = self._right_child(j)
				if self.data[right] > self.data[left]:
					bigchild = right
			if self.data[bigchild] > self.data[j]:
				self._swap(bigchild,j)
				self._downheap(bigchild,size)
	def _buildheap(self):
		start = (self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())
	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)
	def extracting_max(self):
		self._swap(0,self.length()-1)
		max_value = self.data.pop()
		self._downheap(0,self.length()-1)
		return max_value
	def heapOrder(self,position):
		if self.data[position] < self.data[self._parent(position)]:
			self.heapOrder(position-1)
		else:
			return False

	def ascOrder(self):
		length=self.length()
		for i in range(self.length()-1, -1, -1):
			self._swap(0,i)
			# self._downheap(0,length-2)
			self._downheap(0,i)





l1=[10,4,3,2,6,7]
# l1=[1,2,3,4,5]
h=Max_Heap(l1)
print(h.data)
h.heapOrder(h.length()-1)
h.ascOrder()
print(h.data)





	


