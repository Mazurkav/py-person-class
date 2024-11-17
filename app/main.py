class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


    def set_spouse(self, spouse):
        if self.age < spouse.age:
            self.wife = spouse
            spouse.husband = self
        else:
            self.husband = spouse
            spouse.wife = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        new_person = Person(person["name"], person["age"])

    for person in people:
        new_person = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            spouse = Person.people[person["wife"]]
            new_person.set_spouse(spouse)
        elif "husband" in person and person["husband"]:
            spouse = Person.people[person["husband"]]
            new_person.set_spouse(spouse)
    return list(Person.people.values())


# Example usage
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)

# Test the functionality
print(isinstance(person_list[0], Person))  # True
print(person_list[0].name)  # "Ross"
print(person_list[0].wife is person_list[2])  # True
print(person_list[0].wife.name)  # "Rachel"

print(isinstance(person_list[2], Person))  # True
print(person_list[2].name)  # "Rachel"
print(person_list[2].husband is person_list[0])  # True
print(person_list[2].husband.name)  # "Ross"
print(person_list[2].husband.wife is person_list[2])  # True

print(Person.people)  # Should contain Ross, Joey, and Rachel in the dictionary
