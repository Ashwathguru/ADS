#  4. An airport is developing a computer simulation of air-traffic control that handles events such as landings and takeoffs. Each
#event has a time stamp that denotes the time when the event will occur with additional information like, plane number, takeoff or
#landing. The simulation program needs to efficiently perform the following two fundamental operations: 1. Insert an event with a
#given time stamp, aircraft number, takeoff / landing (add a future event).  2. Extract the event with smallest time stamp (that is,
#determine the next event to process). Design and implement suitable data structures that work efficiently in terms of time.

class Min_Heap:
	def __init__(self,mylist=[]):
		self.data=[]
		self.data.append(mylist)#1st ele = timestamp, 2nd ele = aircraft no, 3rd ele = takeoff/landing
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
l1 = [20191208121100, 1003, 'takeoff']
a = Min_Heap(l1)
a.heap_add([20191208101100, 1002, 'takeoff'])
a.heap_add([20191208101130, 1001, 'landing'])
a.heap_add([20191208100030, 1000, 'landing'])
print(a.data)

event = a.extracting_min()
print(event)
print("The aircraft with id ", event[1] ," has an event of " + event[2] + " at " , event[0])
