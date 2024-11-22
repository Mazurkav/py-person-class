class Person:
    # Class attribute to store people by name
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        # Add the instance to the class-level dictionary using the name as the key
        Person.people[name] = self

    def set_spouse(self, spouse_name):
        # Set the spouse relationship
        spouse = Person.people.get(spouse_name)
        if spouse:
            if self.age < spouse.age:  # Assuming if the age is less, they are the wife
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people):
    person_instances = []

    # First, create all Person instances
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person)

    # Now, link spouses where applicable
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            person.set_spouse(spouse_name)

    # Return the list of Person instances
    return person_instances
