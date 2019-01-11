class FlexiQueue:
	default_capacity=2
	def __init__(self):
		self.data=[None]*FlexiQueue.default_capacity
		self.front=0
		self.size=0
	def isEmpty(self):
		return self.size==0
	def length(self):
		return self.size
	def capacity(self):
		return len(self.data)
	def first(self):
		if not self.isEmpty():
			return self.data[self.front]
	def dequeue(self):
		if not self.isEmpty():
			element=self.data[self.front]
			self.data[self.front]=None
			self.front=(self.front+1)%len(self.data)
			self.size-=1
			return element
	def enqueue(self,ele):
		if self.size==len(self.data):
			self.resize(2*len(self.data))
		new_pos=(self.front+self.size)%len(self.data)
		self.data[new_pos]=ele
		self.size+=1
	def resize(self,cap):
		old=self.data
		walk=self.front
		self.data=[None]*cap
		for k in range(len(old)):
			self.data[k]=old[walk]
			walk=(walk+1)
		self.front=0
	
	def rotate(self):
		f=self.data[self.front]
		new_pos=(self.front+self.size)%len(self.data)
		self.data[self.front]=None
		self.data[new_pos]=f
		self.front=(self.front+1)%len(self.data)