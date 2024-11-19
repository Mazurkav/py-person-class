class Person:
    # Class attribute to store instances by their name
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Add this instance to the people dictionary by name
        Person.people[name] = self
        self.wife = None
        self.husband = None

    def set_spouse(self, spouse: 'Person', relationship: str):
        """Sets spouse for the person based on the relationship type (wife or husband)."""
        if relationship == "wife":
            self.wife = spouse
            spouse.husband = self
        elif relationship == "husband":
            self.husband = spouse
            spouse.wife = self


def create_person_list(people):
    person_instances = []
    # First, create Person instances
    for p in people:
        # Create a Person instance
        person = Person(p['name'], p['age'])
        person_instances.append(person)

    # Now set the spouses (wife/husband) based on the input data
    for p in people:
        person = Person.people[p['name']]  # Retrieve the created person instance
        if 'wife' in p and p['wife'] is not None:
            person.set_spouse(Person.people[p['wife']], 'husband')
        if 'husband' in p and p['husband'] is not None:
            person.set_spouse(Person.people[p['husband']], 'wife')

    return person_instances


# Example for testing:
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)

# Tests
assert isinstance(person_list[0], Person)  # True
assert person_list[0].name == "Ross"
assert person_list[0].wife is person_list[2]  # True
assert person_list[0].wife.name == "Rachel"

assert person_list[1].name == "Joey"
assert person_list[1].wife is None  # No wife for Joey

assert isinstance(person_list[2], Person)  # True
assert person_list[2].name == "Rachel"
assert person_list[2].husband is person_list[0]  # True
assert person_list[2].husband.name == "Ross"
assert person_list[2].husband.wife is person_list[2]  # True

assert Person.people == {
    "Ross": person_list[0],
    "Joey": person_list[1],
    "Rachel": person_list[2]
}