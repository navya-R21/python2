class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def show(self):
        print(f'{self.name}{self.age}')

class Dog(Pet):
    def speak(self):
        print("bark")
class Cat(Pet):
    def speak(self):
        print("meow")
d= Dog("siri", 2)
print(d.show())

c=Cat("Bobby",5)
print(c.show())

#using super()
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def show(self):
        print(f'{self.name}{self.age}')

class Dog(Pet):
    def speak(self):
        print("bark")
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def show(self):#here show method  is been overrided
            print(f'{self.name} {self.age} {self.color}')

    def speak(self):
        print("meow")

c2=Cat("billy",2,"white")
print(c2.__dict__)
print(c2.show())
print(c2.speak())


