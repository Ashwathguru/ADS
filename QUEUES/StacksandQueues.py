#1.Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T,
#so that that elements that starts at the top of S is the first to be inserted into T,
#and element at the bottom of S ends up at the top of T.
import LimitedStack
import FlexiQueue
def transfer():
	print("1.Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T")
	S=LimitedStack.LimitedStack()
	T=LimitedStack.LimitedStack()
	data=[1,2,3,4,5]
	for i in range(len(data)):
		S.stackPush(data.pop())
	print("Stack S:",S.data)
	for j in range(S.stackLength()):
		#print(S.stackPop())
		T.stackPush(S.stackPop())
	print("Stack T:",T.data)

#transfer()

def list_rev():
	print("#2.Implement a function that reverses a list of elements by pushing them onto a stack in one order and write them back to the list in reversed order.")
	#s=[x for x in input("Enter the element of stack: ").split(',')]
	s=[1,2,3,4,5]
	print("Input List:",s)
	temp=list(reversed(s))
	s=[]
	#print(s)
	stk=LimitedStack.LimitedStack()
	#print(len(s))
	for i in range(len(temp)):
		#print(s.pop())
		stk.stackPush(temp.pop())
	#print(stk.data)
	for i in range(stk.stackLength()):
		#print(stk.stackPop())
		s.append(stk.stackPop())
	print("Output List:",s)
	return s
#list_rev()

def stk_limit_10():
	print("#3.Modify ArrayStack implementation so that the stack’s capacity is limited to maxlen elements. If push is called when the stack is at full capacity, throw a Full exception.")
	stk=LimitedStack.LimitedStack()
	#stk.resizeStack(15)
	for i in range(1,17):
		stk.stackPush(i)
	print("Input Stack: ",stk.data)

#stk_limit_10()

def temp_stcks():
	print("#4.Implement a transfer function and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reverse order.")
	stk=LimitedStack.LimitedStack()
	temp_stk=LimitedStack.LimitedStack()
	temp_stk_2=LimitedStack.LimitedStack()
	for i in range(1,10):
		stk.stackPush(i)
	print("Input Stack: ",stk.data)
	for j in range(stk.stackLength()):
		temp_stk.stackPush(stk.stackPop())
	for k in range(temp_stk.stackLength()):
		temp_stk_2.stackPush(temp_stk.stackPop())
	for l in range(temp_stk_2.stackLength()):
		stk.stackPush(temp_stk_2.stackPop())
	print("Output Stack: ",stk.data)

#temp_stcks()


def evaluateExp(str1):
	print("#5.HTML generally allows optional attributes to be expressed as part of an opening tag. The general form used is <name attribute1 = “value1” attribute2 = “value2”>. Write function that checks whether tags or matched properly, even when an opening tag may include one or more attributes.")
	stk=LimitedStack.LimitedStack()
	stk.resizeStack(100)
	righty='}]>)'
	lefty='{[<('
	for ch in str1:
		if ch in lefty:
			#print(ch)
			stk.stackPush(ch)
		else:
			if ch in righty:
				#print(ch)
				if stk.isStackEmpty():
					ParanthesisError = Exception()
					raise ParanthesisError
					return False
				if righty.index(ch)!=lefty.index(stk.stackPop()):
					ParanthesisError = Exception()
					raise ParanthesisError
					return False
	if not stk.isStackEmpty():
		#print("aa")
		ParanthesisError = Exception()
		raise ParanthesisError
	return stk.isStackEmpty

#evaluateExp("<html><head>Ashwath is studying</head></html>")

'''def evalHTMLtags(str1):
	stk=LimitedStack.LimitedStack()
	start=str1.index('<')
	while start !=-1:
		end=str1.index('>',start+1)
		if end ==-1:
			return False
		tok=str1[start+1:end]
		if not tok.startswith('/'):
			stk.stackPush(tok)
		else:
			if stk.isStackEmpty():
				return False
			if tok[1:]!=stk.stackPop():
				return False
	start=str1.index('<',end+1)
	return stk.isStackEmpty()

evalHTMLtags("<html><head> Ashwath is studying</head></html>")'''

def three_stcks():
	print("6.Suppose you have three nonempty stacks R, S and T. Describe a sequence of operations that results in S storing all elements originally in T below of S’s original elements, with both sets of those elements in their original configuration. For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].")
	R=LimitedStack.LimitedStack()
	S=LimitedStack.LimitedStack()
	T=LimitedStack.LimitedStack()

	R.stackPush(1)
	R.stackPush(2)
	R.stackPush(3)
	S.stackPush(4)
	S.stackPush(5)
	T.stackPush(6)
	T.stackPush(7)
	T.stackPush(8)
	T.stackPush(9)

	print("Input R:",R.viewStack())
	print("Input S:",S.viewStack())
	print("Input T:",T.viewStack())

	lenofr=R.stackLength()

	for i in range(S.stackLength()):
		R.stackPush(S.stackPop())
	for j in range(T.stackLength()):
		R.stackPush(T.stackPop())
	
	lenofrpush=R.stackLength()
	
	while(lenofr!=lenofrpush):
		S.stackPush(R.stackPop())
		lenofrpush-=1
	
	print("Output R:",R.viewStack())
	print("Output S:",S.viewStack())
	print("Output T:",T.viewStack())

#three_stcks()


#print("#7.Design a stack using a single queue as an instance variable, and only constant additional local memory within the method bodies.")
import FlexiQueue
import LimitedStack
class stack:
	def __init__(self):
		self.data=FlexiQueue.FlexiQueue()
		#self.size=0
	def isEmpty(self):
		return self.data.isEmpty()==1
	def push(self,ele):
		self.data.enqueue(ele)
		#print(self.data.length(),ele)
		#print(ele)
		#self.size+=1
	def pop(self):
		i=1
		#print(self.data.length())
		while i<self.data.length():
			#print(self.data.first())
			#print("aa",i)
			self.data.enqueue(self.data.dequeue())
			i+=1
		return(self.data.dequeue())


'''q=stack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())'''

#print("#8.Design a queue using two stacks as instance variables, such that all queue operations execute in amortized O(1) time.")
import FlexiQueue
import LimitedStack
class Queue:
	def __init__(self):
		self.data1=LimitedStack.LimitedStack()
		self.data2=LimitedStack.LimitedStack()
	def isEmpty(self):
		return self.data2.isStackEmpty()==1
	def enqueue(self,ele):
		self.data1.stackPush(ele)
	def dequeue(self):
		#ij=0
		#print(self.data1.stackLength())
		#print(self.data1.data)
		while not self.data1.isStackEmpty():
			self.data2.stackPush(self.data1.stackPop())
			#print("ash")

		#print(self.data2.data)
		ans=self.data2.stackPop()
		#print('ans',ans)
		#return ans
		while not self.data2.isStackEmpty():
			self.data1.stackPush(self.data2.stackPop())

		return ans
		#self.data1.stackPush(self.data2.stackPop())

'''q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
#print(q.dequeue())'''

#print("9.Design a double-ended queue using two stacks as instance variables.")
import LimitedStack
class Deck:
	def __init__(self):
		self.data1=LimitedStack.LimitedStack()
		self.data2=LimitedStack.LimitedStack()
	def isEmpty(self):
		return self.data2.isStackEmpty==1
	def addFront(self,ele):
		'''if self.data1.isStackEmpty() and self.data2.isStackEmpty():
			self.data1.stackPush(ele)
			self.data2.stackPush(ele)
		else:''' 
		self.data1.stackPush(ele)


	def addLast(self,ele):
		'''if self.data1.isStackEmpty() and self.data2.isStackEmpty():
			self.data1.stackPush(ele)
			self.data2.stackPush(ele)
		else:'''
		self.data2.stackPush(ele)

	def delFront(self):
		if self.data1.isStackEmpty():
			while not self.data2.isStackEmpty():
				self.data1.stackPush(self.data2.stackPop())
			ans=self.data1.stackPop()
			while not self.data1.isStackEmpty():
				self.data2.stackPush(self.data1.stackPop())
			return ans
		else:
			return self.data1.stackPop()

	def delLast(self):
		if self.data2.isStackEmpty():
			while not self.data1.isStackEmpty():
				self.data2.stackPush(self.data1.stackPop())
			ans=self.data2.stackPop()
			while not self.data2.isStackEmpty():
				self.data1.stackPush(self.data2.stackPop())
			return ans
		else:
			return self.data2.stackPop()

		
'''q=Deck()
q.addFront(0)
q.addFront(-1)
q.addFront(-2)
q.addLast(1)
q.addLast(2)
print(q.delLast())
print(q.delLast())
print(q.delLast())
print(q.delLast())
print(q.delLast())
#print(q.delLast())'''

#print("10.Suppose you have a stack S containing n elements and a queue Q that is initially empty. Write function that use Q to scan S to see if it contains a certain element x, with the additional constraint that your algorithm must return the elements back to S in their original order. You may use S, Q and a constant number of other variables.")
import LimitedStack
S=LimitedStack.LimitedStack()
T=FlexiQueue.FlexiQueue()
S.stackPush("Ashwath")
S.stackPush(12345)
S.stackPush("Hello")
S.stackPush(6789)
print(S.viewStack())
#print(S.stackLength())
def scanx(S,x):
	it=0
	while not S.isStackEmpty():
		v=S.stackPop()
		it+=1
		if v==x:
			print("Element ",x," Found")
		else:
			print(v, "is not the element")
		T.enqueue(v)
	while not T.isEmpty():
		i=1
		#print("a")
		while  i<T.length():
			i+=1
			T.enqueue(T.dequeue())
		S.stackPush(T.dequeue())
	
#scanx(S,12345)
#print(S.viewStack())
#print(T.length())
print("#11.In certain applications of the queue, it is common to repeatedly dequeue an element, process it in some way, and then immediately enqueuer the same element. Modify ArrayQueue implementation to include a rotate( ) method that has semantics identical to the combination, Q.enqueue (Q.dequeue()). However, your implementation should be more efficient than making two separate calls.")
import FlexiQueue
Q1=FlexiQueue.FlexiQueue()
Q1.enqueue(1)
Q1.enqueue(2)
Q1.enqueue(3)
Q1.enqueue(4)

Q1.rotate()

print(Q1.dequeue())
print(Q1.dequeue())
print(Q1.dequeue())
print(Q1.dequeue())

'''print('#12.Give an array based implementation of double-ended queue supporting behaviors like len (), add_first(), add_last(), delete_first(), delete_last(), first() and last(). Double-ended queue should be of fixed capacity. When queue is full, inserting element from one end should cause an element to be lost from the opposite side.')

import Deck

D=Deck.Deck()
print(D.isEmpty())
print(D.length())
D.add_first('S')
print(D.first_element())
D.add_first('A')
print(D.first_element())
D.add_last('H')
print(D.last_element())
D.del_last()
print(D.last_element())
print(D.del_front())

D.add_last('A')
D.add_last('B')
D.add_last('C')
D.add_last('D')
D.add_last('E')
D.add_last('F')
print(D.del_front())
print(D.del_front())
print(D.del_front())
print(D.del_front())
print(D.del_front())
print(D.del_front())
print(D.del_front())

D.add_first('A')
D.add_first('B')
D.add_first('C')
D.add_first('D')
D.add_first('E')
D.add_first('F')
print(D.last_element())'''


