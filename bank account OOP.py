class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender


class Room:
    def __init__(self, name, access, capacity):
        self.name = name
        self.access = access
        self.capacity = capacity
        self.people = []

    def add_person(self, person):
        if (len(self.people) < self.capacity) & (self.access == person.gender):     # filtering by capacity and gender
            self.people.append(person)
            return True
        return False


p1 = Person("Alissa", "Female")
p2 = Person("Michael", "Male")
p3 = Person("Kelly", "Female")
p4 = Person("Sally", "Female")

room1 = Room("Girl's Bathroom", "Female", 2)
room1.add_person(p1)
room1.add_person(p2)
room1.add_person(p3)
room1.add_person(p4)


print(room1.people)
print(room1.people[0].name)






