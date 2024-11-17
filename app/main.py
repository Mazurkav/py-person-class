class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

    def set_spouse(self, spouse):
        # This method sets the spouse reference for wife or husband
        if self.age < spouse.age:  # Assuming the female is younger
            self.wife = spouse
            spouse.husband = self
        else:
            self.husband = spouse
            spouse.wife = self


def create_person_list(people):
    person_instances = []

    # First, create all Person instances and add them to the person_instances list
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_instances.append(new_person)  # Append the created instance to the list

    # Next, set the spouses (wife or husband)
    for person in people:
        new_person = next(p for p in person_instances if p.name == person["name"])

        if "wife" in person and person["wife"]:
            spouse = next(p for p in person_instances if p.name == person["wife"])
            new_person.set_spouse(spouse)
        elif "husband" in person and person["husband"]:
            spouse = next(p for p in person_instances if p.name == person["husband"])
            new_person.set_spouse(spouse)

    # Return the list of created Person instances
    return person_instances


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
