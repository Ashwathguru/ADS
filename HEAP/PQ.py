class priorityQueue:
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
		if j > 0 and self.data[j][2] > self.data[parent][2]:
			self._swap(j,parent)
			self._upheap(parent)
		elif j > 0 and self.data[j][2] == self.data[parent][2]:
			if self.data[j][1] < self.data[parent][1]:
				self._swap(j,parent)
				self._upheap(parent)
	def _downheap(self,j,size):
		if self._left_child(j) < size:
			left = self._left_child(j)
			bigchild = left
			if self._right_child(j) < size:
				right = self._right_child(j)
				if self.data[right][2] > self.data[left][2]:
					bigchild = right
				elif self.data[right][2] == self.data[left][2]:
					if self.data[right][1] < self.data[left][1]:
						bigchild = right

			if self.data[bigchild][2] > self.data[j][2]:
				self._swap(bigchild,j)
				self._downheap(bigchild,size)
			elif self.data[bigchild][2] == self.data[j][2]:
				if self.data[bigchild][1] < self.data[j][1]:
					self._swap(bigchild,j)
					self._downheap(bigchild,size)
	def _buildheap(self):
		start = (self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())
	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)

	def descOrder(self):
		length=self.length()
		for i in range(self.length()-1, -1, -1):
			self._swap(0,i)
			self._downheap(0,i)
	def waitingTime(self):
		waitingTime=[]
		TaT=[]
		for i in range(0,self.length()):
			if i is 0:
				wt = 0
				waitingTime.append(wt)
				tat = self.data[i-1][3]
				TaT.append(tat)
				
			else:
				wt = TaT[i-1] - self.data[i][2] + 1
				waitingTime.append(wt)
				tat = waitingTime[i] + self.data[i][3]
				TaT.append(tat)
		return waitingTime, TaT
	def chkDeadline(self,tat):
		print(tat)
		l1=[]
		for i in range(0,self.length()):
			if self.data[i][4] < tat[i]:
				l1.append(self.data[i][0])
		return l1