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


