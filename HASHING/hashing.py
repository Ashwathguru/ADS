import numpy as np
class openhash:
	table_size = 11
	class Node:
		def __init__(self,ssd,name):
			self.ssid = ssd
			self.name = name
			self.next = None
	def __init__(self):
		self.hashtable = []
		self.p = 13
		self.a = np.random.randint(1,self.p)
		self.b = np.random.randint(0,self.p)
		self._initialize_hashtable()
	def _initialize_hashtable(self):
		self.hashtable = [None]*openhash.table_size
		print(len(self.hashtable))

	def _hash_number(self,element):
		hashcode = 0
		for ch in str(element):
			hashcode = hashcode << 5
			hashcode = hashcode+ord(ch)
		return hashcode

	def _compress(self,number):
		return(((self.a*number+self.b)%self.p)%openhash.table_size)
	
	def _hash_(self,element):
		number = self._hash_number(element)
		#print("hash value",number)

		hashcode = self._compress(number)
		print("compress",hashcode)
		
		return hashcode

	def is_member(self,element):
		bucket = self._hash_(element)
		

		cur = self.hashtable[bucket]
		while(cur!=None):
			if cur.name == element:
				return True
			else:
				cur = cur.next
		return False

	def add_number(self,element,name):
		if not self.is_member(element):
			bucket = self._hash_(element)
			new_node = self.Node(element,name)
			new_node.next = self.hashtable[bucket]
			self.hashtable[bucket] = new_node


	def delete_data(self,element):
		bucket = self._hash(element)
		if self.hashtable[bucket]!=None:
			if self.hashtable[bucket].ssid == element:
				self.hashtable[bucket] = self.hashtable[bucket].next
			else:
				cur = self.hashtable[bucket]
				while cur.next!=None:
					if cur.next.ssid==element:
						cur.next = cur.next.next
					else:
						cur = cur.next



	def display(self,element):
		bucket = self._hash_(element)
		cur = self.hashtable[bucket]
		#print(cur)
		while(cur!=None):
			if cur.ssid == element:
				#print(cur.name)
				print(cur.name)
				cur = cur.next


			else:
				cur = cur.next
	def displayv2(self):
		for ch in range(len(self.hashtable)):
			cur = self.hashtable[ch]
			while(cur!=None):
				print(cur.name)
				cur = cur.next
			

		


if __name__ == '__main__':
	hashobj = openhash()
	hashobj.add_number("123","dheemanth")
	hashobj.add_number("456","uday")
	#hashobj.add_number(789,"pradeep")
	hashobj.add_number("123","dasda")
	hashobj.display("123")




					













