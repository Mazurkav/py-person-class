class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
