#Python 
#example of variables and data

age = 25
height = 5.9
name = "Beni"
is_Student = True
fruits = ["apple", "banana", "orange"]
person = {"name" : "vincent", "age": 30}
x = 10
y = 5 
addition = x + y
subtraction = x - y 
multiplication = x * y
division = x / y

age = 20 

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("youre an adult")
else:
    print("u are senior")

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
    
count = 0 
while count < 5:
    print(count)
    count += 1
    
def greet(name):
    print("Hello "+ name + "!")
    
greet("beni")

message = "Hello, World"

print(message[0])
print(message[7:12])
print(len(message))

with open("example.txt", "w") as file:
    file.write("Hello, world")
    
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
try:
    result = 10/0
except ZeroDivisionError:
    print("Error division by zero")
    
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def greet(self):
        print("Hello, my name is ", self.name + "my age is, " + self.age)
        
person1 = Person("Beni", 22)
person1.greet()

class Student(Person):
    def __init___(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id
        
    def study(self):
        print(self.name, "is studying")

student1 = Student("Beni",22, "19-1208")
student1.study()

def countdown(n):
    while n > 0:
        yield n 
        n -= 1
        
for i in countdown(5):
    print(i)
    
def decorator(func):
    def wrapper():
        print("Benofre calling the function")
        func()
        print("after calling the function")
    return wrapper

def say_hello():
    print("Hello, World")
    
say_hello()


def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n-1)
        
print(factorial(5))

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

union_set = set1 | set2
print(union_set)

intersection_set = set1 & set2
print(intersection_set)

numbers = [1,3,4,5]

print(len(numbers))

numbers.append(6)
print(numbers)

print(max(numbers))

#virtualenv myenv
#source myenv/bin/activate

import unittest

def add(x,y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,5),8)
        self.assertEqual(add(-1,1),0)
        
if __name__ == '__main__':
    unittest.main()
    


class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.item.pop()
    
    def is_empty(self):
        return len(self.items) == 0 
    
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())

