class Person:
    number_of_people=0
    def __init__(self,name):
        self.name=name
        Person.number_of_people=Person.number_of_people+1
p=Person("ram")
p1=Person("shyam")
print(Person.number_of_people)

#class methods
class Count:
    number_of_people=0
    def __init__(self,name):
        self.name=name
        Count.number_of_people=Count.number_of_people+1

    @classmethod
    def get_num_of_ppl(cls):
        return cls.number_of_people
c=Count("rob")
c1=Count(" bin")
print(Count.get_num_of_ppl())

#static method
class Math:
    @staticmethod
    def add_5(x):
        return x+5

    @staticmethod
    def add_10(y):
        return y+10
m=Math()
print(m.add_5(7))
print(m.add_10(20))

