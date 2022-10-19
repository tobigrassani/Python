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
            print(f">>>>>{person.name} approved to join {room1.name}")
            return True
        print(f"{person.name} denied to join {room1.name}<<<<<")
        return False


p1 = Person("Alissa", "Female")
p2 = Person("Michael", "Male")
p3 = Person("Kelly", "Female")
p4 = Person("Sally", "Female")
p5 = Person("Maria", "Female")
p6 = Person("Thomas", "Male")
p7 = Person("John", "Male")
p8 = Person("Alex", "Male")



room1 = Room("Girl's Bathroom", "Female", 2)
room2 = Room("Boy's Bathroom", "Male", 3)
room1.add_person(p1)
room1.add_person(p2)
room1.add_person(p3)
room1.add_person(p4)
room2.add_person(p1)
room2.add_person(p2)
room2.add_person(p3)
room2.add_person(p4)


print(room1.people)
print(room1.people[0].name)






