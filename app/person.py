class Person:
    # Class attribute to store people by their names
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Add this instance to the people dictionary
        Person.people[name] = self
        self.wife = None
        self.husband = None

    def set_spouse(self, spouse: "Person", is_wife: bool):
        """Sets the spouse for the person instance."""
        if is_wife:
            self.wife = spouse
        else:
            self.husband = spouse
