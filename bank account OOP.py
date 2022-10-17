class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


p = Person("Alissa", "Female")
print(f"Hello my name is {p.get_name().upper()}")
print(f"and beeing {p.get_gender().lower()} is the best in world.")

p2 = Person("Michael", "Male")
print(f"Hello my name is {p2.get_name().upper()}")
print(f"and beeing {p2.get_gender().lower()} is the best in world.")





