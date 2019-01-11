#Stacks
#Author:Ashwathguru S
#Roll No.181046039

#LimitedStack class contains all the methods to perform operations with stacks
class LimitedStack:
	capacity=10000
	def __init__(self):
		self.data=[]
		self.count=0
#Checks if the Stack is empty.returns true/false
	def isStackEmpty(self):
		'''if self.count==0:
			print("The stack is empty")
		else:
			print("the stack is not empty")'''
		return self.count==0
#Checks if the Stack is full.returns true/false
	def isStackFull(self):
		'''if self.count==LimitedStack.capacity:
			print("The stack is Full")
		else:
			print("The stack is not full")'''
		return self.count==LimitedStack.capacity
	def stackLength(self):
		'''print(self.count)'''
		return self.count
#returns the last element in the stack 	
	def stackPeek(self):
		if not self.isStackEmpty():
			return self.data[-1]
#pushes element into the stack 
	def stackPush(self,ele):
		if not self.isStackFull():
			self.data.append(ele)
			self.count+=1
		else:
			ValError=Exception()
			raise ValError("The stack is full")
#Pops element from the stack
	def stackPop(self):
		if not self.isStackEmpty():
			p=self.data.pop()
			self.count-=1
			return p
#Returns all the elements of the stack
	def viewStack(self):
		if not self.isStackEmpty():
			'''print(self.data)'''
			return self.data
