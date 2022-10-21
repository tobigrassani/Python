class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


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

    def del_person(self, person):
        self.people.remove(person)

    def show_people(self):
        print(self.people)


p1 = Person("Alissa", "Female")
p2 = Person("Michael", "Male")
p3 = Person("Kelly", "Female")

room1 = Room("Girl's Bathroom", "Female", 2)
room2 = Room("Boy's Bathroom", "Male", 3)

room1.add_person(p1)
room1.add_person(p2)
room1.add_person(p3)

room2.add_person(p1)
room2.add_person(p2)
room2.add_person(p3)

room1.show_people()
room2.show_people()








