# Develop a student Information System to admit students into course. 
# The number of courses offered will be Embedded Systems, VLSI Design and Medical Software. 
# Number of seats in each course is 5.
#  Admission is based on first come first serve basis.
#   Once the seats in one course are filled, student can get admitted to other course if seats are available.
#  Information stored are name of student, course selected and Marks in qualifying exam. 
#  Once the student is admitted, registration number should be auto-generated based on course selected. 
#  Provide display functions to display the student details course wise, display information of students
#   who scored max marks in qualifying exam across all course.



class sois:
	def __init__(self):
		self.courses = {'ES':[],'VLSI':[]}

	def admit(self,student):
		if len(self.courses[student['course_name']]) != 5:
			student=self._gen(student)
			self.courses[student['course_name']].append(student)
			return student['Reg']
		else:
			print("course full!!")

	def display(self,course):
		for student in self.courses[course]:
			for k,v in student.items():
				print(k,v)

	def getmax(self):
		max_marks = 0
		for course, slist in self.courses.items():
			for student in slist:
				if max_marks < student['marks']:
					max_marks = student['marks']
					max_student = student
			
		return max_student

	def _gen(self,student):
		c = len(self.courses[student['course_name']])
		student['Reg'] = student['course_name'] + str(c+1)
		return student
		
def college():
	sobj = sois()
	s1 = {'Name':'uday','course_name':'ES','marks':89}
	s2 = {'Name':'a','course_name':'ES','marks':85}
	s3 = {'Name':'d','course_name':'ES','marks':80}
	s4 = {'Name':'f','course_name':'ES','marks':90}
	s5 = {'Name':'q','course_name':'ES','marks':95}
	s6 = {'Name':'r','course_name':'ES','marks':70}
	sobj.admit(s1)
	sobj.admit(s2)
	sobj.admit(s3)
	sobj.admit(s4)
	sobj.admit(s5)
	sobj.admit(s6)
	sobj.display('ES')
	sobj.display('VLSI')
	print(sobj.getmax())

if __name__ == '__main__':
	college()