#sizes of datatypes
#integer
import weakref

x=10
import sys
print(sys.getsizeof(x))

#string
str=''
print(sys.getsizeof(str))

str_1='mad'
print(sys.getsizeof(str_1))

#lists
mem=[]
print(sys.getsizeof(mem))

mem_1=[1,2,3]
print(sys.getsizeof(mem_1))

#dictionary
dic={ }
print(sys.getsizeof(dic))

dic_1={1:'jon', 4:'ram' }
print(sys.getsizeof(dic_1))

#sets
S={}
print(sys.getsizeof(S))

S_1={ 1,2,3}
print(sys.getsizeof(S_1))

#Dead Object
class Car:
    def __init__(self,w):
        self.wheels=w
c= Car(4)
print("c memory location:", hex(id(c)))

r=weakref.ref(c)
print("before:",r)

c=None
print("after:",r)
print("garbage collected immediately")


