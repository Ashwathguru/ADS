#linkedlist

class slist:
	class _Node:
		def __init__(self,ele):
			self.data=ele
			self.next=None
	def __init__(self):
		self.head=None
		self.tail=None
		self.count=0
	
	def isEmpty(self):
		return self.count==0
	
	def addFirst(self,ele):
		new_node=self._Node(val)
		if not self.isEmpty():
			new_node.next=self.head
			self.head=new_node
		else:
			self.head=self.tail=new_node
		self.count+=1
	def addLast(self,val):
		new_node=self._Node(val)
		if not self.isEmpty():
			self.tail.next=new_node
			self.tail=new_node
		else:
			self.head=self.tail=new_node
		self.count+=1

	def delFirst(self):
		if not self.isEmpty():
			self.head=self.head.next
		if self.head==None:
			self.tail=None
	def delLast(self):
		if not self.isEmpty():
			if self.head==self.tail:
				self.head=self.tail=None
		else:
			tail=self.tail
			cur=self.head
		while cur.next!=tail:
			cur=cur.next
		self.tail=cur
		cur.next=None
		self.count-=1

