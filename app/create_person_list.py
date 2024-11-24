from person import Person

def create_person_list(people):
    person_list = []
    for p in people:
        person = Person(p["name"], p["age"])
        if "wife" in p and p["wife"] is not None:
            person.wife = Person.people.get(p["wife"])
        if "husband" in p and p["husband"] is not None:
            person.husband = Person.people.get(p["husband"])
        person_list.append(person)
    return person_list
