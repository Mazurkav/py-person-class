from person import Person

def create_person_list(people: list) -> list:
    # Create Person instances from the list of dictionaries
    person_instances = []
    for person_data in people:
        # Create the Person instance
        person = Person(person_data["name"], person_data["age"])
        person_instances.append(person)

    # Set spouses for each person if any
    for person_data in people:
        person = Person.people[person_data["name"]]  # Get the instance
        if "wife" in person_data and person_data["wife"] is not None:
            wife = Person.people[person_data["wife"]]
            person.set_spouse(wife, is_wife=True)
            wife.set_spouse(person, is_wife=False)
        if "husband" in person_data and person_data["husband"] is not None:
            husband = Person.people[person_data["husband"]]
            person.set_spouse(husband, is_wife=False)
            husband.set_spouse(person, is_wife=True)

    return person_instances
