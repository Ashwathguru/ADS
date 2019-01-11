#HEAP
'''1. Build maximum heap with required methods. It should support the behaviors like adding
element, getting maximum element, extracting maximum element, count number of elements
and to check the method to test the heap order property.

2. Modify Q2 to sort the input in ascending order.

3. Build priority queue to handle real time tasks. Tasks can arrive at time. The attributes of tasks
are task-id, priority, arrival time, execution time and deadline. Compute waiting time,
turnaround time for each job. Check whether jobs are completed within the deadline specified.
It is treated that 10 is maximum priority and 1 is least priority.

4. An airport is developing a computer simulation of air-traffic control that handles events such as
landings and takeoffs. Each event has a time stamp that denotes the time when the event will
occur with additional information like, plane number, takeoff or landing. The simulation
program needs to efficiently perform the following two fundamental operations: 1. Insert an
event with a given time stamp, aircraft number, takeoff / landing (add a future event). 2. Extract
the event with smallest time stamp (that is, determine the next event to process). Design and
implement suitable data structures that work efficiently in terms of time.'''


############################################################################################################3

'''1. Build maximum heap with required methods. It should support the behaviors like adding
element, getting maximum element, extracting maximum element, count number of elements
and to check the method to test the heap order property.'''

class MaxHeap:
	def __init__(self,mylist=[]):
		self.data=mylist
		self._buildheap()
	def isEmpty(self):
		return self.data==0
	def length(self):
		return len(self.data)
	def _parent(self,j):
		return(j-1)//2
	def _left_child(self,j):
		return(2*j+1)
	def _right_child(self,j):
		return(2*j+2)
	def _swap(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
	def _upheap(self,j):
		parent=self._parent(j)
		if j>0 and self.data[j]>self.data[parent]:
			self._swap(j,parent)
			self._upheap(parent)
	def _downheap(self,j,size):
		#size=len(self.data)
		if self._left_child(j)<size:
			left=self._left_child(j)
			largechild=left
			if self._right_child(j)<size:
				right=self._right_child(j)
				if self.data[right]>self.data[left]:
					largechild=right
			if self.data[largechild]>self.data[j]:
				self._swap(largechild,j)
				self._downheap(largechild,size)
	def _buildheap(self):
		start=(self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())
	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)
	def printlist(self):
		print(self.data)
	def get_Max(self):
		return self.data[0]
	def extract_max(self):
		self._swap(0,len(self.data)-1)
		max=self.data.pop()
		#self._downheap(0,self.length())
		self._buildheap()
		return max
	def maxHeap_sort(self):
		length=self.length()
		for i in range(length-1,-1,-1):
			self._swap(0,i)
			self._downheap(0,i)
		print(self.data)
		self._buildheap()

	def test_heap_order(self):
		for i in range(0,self.length()-1):
			if self.data[position]<self.data[self._parent(position)]:
				self.heapOrder(position-1)
			else:
				return False
		return True
