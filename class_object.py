#
def sum(x):
    return x+1
print(type(sum))

#class creation
class MyNewClass:
    "This is a docstring. I have created a new class"
    pass
#class
class Man:
     def speak(self): #speak is a method
         print("talk")
     def action(self):
         print("walk")
#object creation
m=Man()
m.speak()
m.action()
m1=Man()
m1.action()

#instance variable
class Dog:
    def talk(self):
        print("bark")
    def set_breed(self,breed):
        self.breed=breed
    def get_breed(self):
        return self.breed
d=Dog()
d1=Dog()
d.set_breed("Golden retriever")
print(d.get_breed())

#init method
class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age = age
        self.color = color

    def walk(self):
        print("run")
d=Dog("tom",5,"black")
d1=Dog("siri",10,"gold")
print(d.name)
print(d.age)
print(d.color)
print(d.__dict__)
print(d1.__dict__)


