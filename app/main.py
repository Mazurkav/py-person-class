from typing import List, Dict, Union


class Person:
    # Class attribute to store all Person instances by name
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a new Person instance.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age
        # Add this instance to the class-level people dictionary
        Person.people[name] = self


def create_person_list(
    people: List[Dict[str, Union[str, int, None]]]
) -> List[Person]:
    """
    Create a list of Person instances from a list of dictionaries.

    :param people: A list of dictionaries containing person data.
    :return: A list of Person instances.
    """
    # Create instances without setting wife/husband links yet
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Set wife/husband attributes after all instances are created
    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]

    return person_list
