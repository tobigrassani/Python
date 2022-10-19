class Person:
    def __init__(self, name, gender, id):
        self.name = name
        self.gender = gender
        self.id = id

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Account(Person):



