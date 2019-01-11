class Slist:
	max_count=10
	class _Node:
		def __init__(self,ele):
			self.data=[]
			self.data.append(ele)
			self.next=None
	def __init__(self):
		self.head=None
		self.tail=None
		self.count=0
		self.data=[]
	def isEmpty(self):
		return self.count==0
	def addFirst(self,val):
		new_node=self._Node(val)
		if not self.isEmpty():
			new_node.next=self.head
			self.head=new_node
		else:
			self.head=new_node
		self.count+=1
	def addLast(self,val,l_no):
		current=self.head
		if not self.isEmpty():
			for i in range(0,int(val)-7):
				current=current.next
			if len(current.data)==11:
				print("No slot empty")
			else:
				for i in range(1,11):
					if not i in current.data:
						current.data.append(i)
						id=str(l_no)+' '+val+' '+str(i)
						print(id)
						return id
	def delFirst(self):
		if not self.isEmpty():
			self.head=self.head.next
			if self.head==None:
				self.tail=None
			self.count-=1
	def delLast(self,hr,tbl):
		print(tbl)
		current=self.head
		if not self.isEmpty():
			for i in range(0,int(hr)-7):
				current=current.next
			print("Table in data")
			if int(tbl) in current.data:
				print(tbl)
				current.data.pop(int(tbl))
	def show1(self,hr):
		current=self.head
		for i in range(0,int(hr)-7):
			current=current.next
		print("The 2-seater tables booked are:")
		for i in range(1,len(current.data)):
			if i != 0:
				print("2T-"+str(i)+"\n")
		print("The 2-seater tables free are:")
		for i in range(1,11):
			if i not in current.data and i!=0:
				print("2T-"+str(i)+"\n")
	def show2(self,hr):
		current=self.head
		for i in range(0,int(hr)-7):
			current=current.next
		print("The 4-seater tables booked are:")
		for i in range(1,len(current.data)):
			if i != 0:
				# print("The tables booked are:")
				print("4T-"+str(i)+"\n")
		print("The 4-seater tables free are:")
		for i in range(1,11):
			if i not in current.data and i!=0:
				print("4T-"+str(i)+"\n")
	def show3(self,hr):
		current=self.head
		for i in range(0,int(hr)-7):
			current=current.next
		print("The 6-seater tables booked are:")
		for i in range(1,len(current.data)):
			if i != 0:
				# print("The tables booked are:")
				print("6T-"+str(i)+"\n")
		print("The 6-seater tables free are:")
		for i in range(1,11):
			if i not in current.data and i!=0:
				print("6T-"+str(i)+"\n")

l1_2seater=Slist()
for i in range(0,16):
	l1_2seater.addFirst(None)
l2_4seater=Slist()
for i in range(0,16):
	l2_4seater.addFirst(None)
l3_6seater=Slist()
for i in range(0,16):
	l3_6seater.addFirst(None)


reservation=''
while reservation!='exit':
	reservation=input("Enter the reservation required in the format <persons> <start_time> and to cancel as cancel <id> which is returned after the reservation is made and <show> <hour_slot> to see the tables booked\n")

	if not reservation.split(' ')[0].isalpha():
		id=[]
		count=reservation.split(' ')[0]
		count=int(count)
		while count!=0:
			if count==1:
				id1=l1_2seater.addLast(reservation.split(' ')[1],1)
				# id=id.append(id1)
				count=count-1
			elif count==2:
				if l1_2seater.count == 10:
					id2=l2_4seater.addLast(reservation.split(' ')[1],2)
					# id=id.append(id2)
					count=count-2
				else:
					id2=l1_2seater.addLast(reservation.split(' ')[1],1)
					# id=id.append(id2)
					count=count-2
			elif count<=4:
				l2_4seater.addLast(reservation.split(' ')[1],2)
				id3=count=count-4
				# id=id.append(id3)
			elif count<=6:
				id4=l3_6seater.addLast(reservation.split(' ')[1],3)
				count=count-6
				id=id.append(id4)
			elif count>6:
				id4=l3_6seater.addLast(reservation.split(' ')[1],3)
				count=count-6
				# id=id.append(id4)
	elif reservation.split(' ')[0]=='cancel':
		l_ele=reservation.split(' ')
		print(l_ele[0])
		print("*********")
		print(l_ele[1])
		# list2=list1[i]
		# l_ele=list2.split(' ')
		if l_ele[1]=='1':
			l1_2seater.delLast(l_ele[2], l_ele[3])
		elif l_ele[1]=='2':
			print(l_ele[0])
			l2_4seater.delLast(l_ele[2], l_ele[3])
		elif l_ele[1]=='3':
			l2_6seater.delLast(l_ele[2], l_ele[3])
	elif reservation.split(' ')[0]=='show':
		l1_2seater.show1(reservation.split(' ')[1])
		l2_4seater.show2(reservation.split(' ')[1])
		l3_6seater.show3(reservation.split(' ')[1])
exit()



















