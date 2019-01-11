'''Develop a student Information System to admit students into course. The number of courses offered will be Embedded Systems,VLSI Design and Medical Software. Number of seats in each course is 5. Admission is based on first come first serve basis. Once the seats in one course are filled, student can get admitted to other course if seats are available. Information stored are name of student, course selected and Marks in qualifying exam. Once the student is admitted, registration number should be auto-generated based on course selected. Provide display functions to display the student details course wise, display information of students who scored max marks in qualifying exam across all course.'''

class college:
	
	def __init__(self):
		self.apply_list=[]
		self.size=5
		self.course_id={'001':'EMD','002':'VLSI','003':'MSW'}
		self.max_marks=0
		self.topper=None
		self.EMD_list={}
		self.EMD_count=0
		self.VLSI_list={}
		self.VLSI_count=0
		self.MSW_list={}
		self.MSW_count=0

	def generate_id(self,courseid,seat_no):
		return "2018"+str(courseid)+str(seat_no)
	
	def applicants_list(self,name,course_wanted,marks):
		if marks is not None:
			self.apply_list.append([name,course_wanted,marks])
	
	def EMD(self,name,marks):
		if self.EMD_count<self.size:
			self.EMD_count+=1
			self.EMD_list[self.generate_id('001',self.EMD_count)]=[name,marks]
		else:
			print("EMD COURSE FULL")
			ch=input("Want Different course?: ")
			if ch=='VLSI':
				self.VLSI(name,marks)
			elif ch=='MSW':
				self.MSW(name,marks)
			else:
				print("TRY AGAIN NEXT YEAR")
	def VLSI(self,name,marks):
		if self.VLSI_count<self.size:
			self.VLSI_count+=1
			self.VLSI_list[self.generate_id('002',self.VLSI_count)]=[name,marks]
		else:
			print("VLSI COURSE FULL")
			ch=input("Want Different course?: ")
			if ch=='EMD':
				self.EMD(name,marks)
			elif ch=='MSW':
				self.MSW(name,marks)
			else:
				print("TRY AGAIN NEXT YEAR")
	def MSW(self,name,marks):
		if self.MSW_count<self.size:
			self.MSW_count+=1
			self.MSW_list[self.generate_id('003',self.MSW_count)]=[name,marks]
		else:
			print("MSW COURSE FULL")
			ch=input("Want Different course?: ")
			if ch=='EMD':
				self.EMD(name,marks)
			elif ch=='VLSI':
				self.VLSI(name,marks)
			else:
				print("TRY AGAIN NEXT YEAR")

	def admit(self):
		for name,course_wanted,marks in self.apply_list:
			if self.EMD_count==5 & self.VLSI_count==5 & self.MSW_count==5:
				print("ALL COURSES FULL")
			else:
				if marks>self.max_marks:
					self.max_marks=marks
					self.topper=name
				if course_wanted=='EMD':
					self.EMD(name,marks)
				if course_wanted=='VLSI':
					self.VLSI(name,marks)
				if course_wanted=='EMD':
					self.MSW(name,marks)

	def get_topper(self):
		print(self.topper,self.max_marks)

sois=college()
'''import random
import numpy as np
np.random.choice(['EMD','VLSI','MSW'])
np.random.randint(100,size=1)

for i in range(50):
	n=np.random.choice(['AAA','BBB','CCC'])
	su=np.random.choice(['EMD','VLSI','MSW'])
	m=np.random.randint(100)
	sois.applicants_list(n,su,m)

sois.admit()
sois.get_topper()
print("EMBEDDED STUDENTS: ",sois.EMD_list)
print("VLSI STUDENTS: ",sois.VLSI_list)
print("MSW STUDENTS: ",sois.MSW_list)

#print(sois.apply_list)'''

