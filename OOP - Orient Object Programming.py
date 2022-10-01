# Orient Object Programming
class MyClass:
    x = 4
    y = 10


p1 = MyClass()
print(p1.x)
print(p1.y)
print(MyClass.x + MyClass.y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Agustin", 24)

print("Person name:", p1.name)
print("age:", p1.age)

print(p1)


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introPerson(self):
        print("Hello, my name is", self.name)
        print("and I am", self.age, ", nice to meet u")


p1 = Person1("Carlos", 24)
p1.introPerson()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Dog's name:", self.name)
        print("Age:", self.age)


d1 = Dog("Killy", 2)
d1.intro()


class Puppy(Dog):
    pass


x = Puppy("child1", 0.5)
x.intro()
