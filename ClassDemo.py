class Person:
  def __init__(self,sid, fname, lname):
    self.id = sid
    self.firstname = fname
    self.lastname = lname
  def printInfo(self):
      print(f"\t Your id is:{self.id} , Your first name is: {self.firstname},Your last name is:{self.lastname}.")

class Student(Person):
  def __init__(self,sid, fname, lname,grade):
    super().__init__(sid,fname,lname)
    self.grade = grade

  def printInfo(self):
      print(f"\t Your id is:{self.id} , Your first name is: {self.firstname},Your last name is:{self.lastname}.")
  
  def getGrade(self):
     return self.grade

class Teacher(Person):
  def __init__(self,sid, fname, lname,email):
    super().__init__(sid,fname,lname)
    self.email = email
    self.students = []

  def printInfo(self):
      print(f"\t Your id is:{self.id} , Your first name is: {self.firstname},Your last name is:{self.lastname}, Your Email address is:{self.email}.")
  
  def getEmail(self):
     return self.email

  def addStudent(self,student):
     if type(student) is Student:
         self.students.append(student)

  def getStudents(self):
      return self.students

  def getNumberOfStudents(self):
      return len(self.students)

  def getAverage(self):
      sum =0
      for s in teacher.getStudents():
          sum += int(s.getGrade())

      avg = sum / len(teacher.getStudents())
      return avg

  def getTopGrade(self):
      maxGrade = 0
      for s in teacher.getStudents():
          grade = int(s.getGrade())
          if maxGrade < grade:
              maxGrade = grade
              
      return maxGrade


listOfStudents = []
listOfTeachers = []

print("Enter student information:")
for i in range(1,3):
    firstname = input("Enter your first name:")
    lastname = input("Enter your lasst name:")
    grade = input("Enter your Grade:")
    student = Student(i,firstname,lastname, grade)
    listOfStudents.append(student)

print("Enter teacher information:")
for i in range(1,2):
    firstname = input("Enter your first name:")
    lastname = input("Enter your lasst name:")
    email = input("Enter your email address:")
    teacher = Teacher(i,firstname,lastname, email)
    listOfTeachers.append(teacher)
    for student in listOfStudents:
        teacher.addStudent(student)

print("List of students:")
for student in listOfStudents:
    if type(student) is Student:
        student.printInfo()
        print("\t\t Your grade:",student.getGrade())

for teacher in listOfTeachers:
    if type(teacher) is Teacher:
        print("Teacher info:")
        teacher.printInfo()
        print("List of students:")
        for s in teacher.getStudents():
            print("\t Student id:", s.id)
            print("\t Student first name:", s.firstname)
            print("\t Student last name:", s.lastname)
            print("\t Student grade:", s.grade)
        
        teacher.getAverage()
        print("\t Number of students:", teacher.getNumberOfStudents())
        print("\t Best Grade:", teacher.getTopGrade())

class Thought(object):
   def __init__(self):
       print("Thought, always come and go from the constructor!")
   def message(self, text):
      print("Thought, always come and go" , text)

class Advice(Thought):
   def __init__(self, text):
      super(Advice, self).__init__()
      super(Advice, self).message(text)
   def message(self, text):
      print(f"Warning: Risk is always involved when you are dealing with {text}!")

A= Advice("from the brain")
A.message("Developers")
       

