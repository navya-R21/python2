
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
    def add_students(self,student):
        if(len(self.students)<self.max_students):
            self.students.append(student)
            return True
        return False
    def avg_grade(self):
        value=0
        for s in self.students:
            value=value+s.get_grade()
        return value/len(self.students)

s1= Student("tom",20,99)
s2= Student("ram",19,56)
s3= Student("kam",18,89)

c1=Course ("science",2)
print(c1.add_students(s1))
print(c1.add_students(s2))
print(c1.add_students(s3))
print(c1.avg_grade())






