from create_person_list import create_person_list

def main():
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]
    person_list = create_person_list(people)
    for person in person_list:
        print(f"Name: {person.name}, Age: {person.age}")
        if person.wife:
            print(f"{person.name}'s wife: {person.wife.name}")
        if person.husband:
            print(f"{person.name}'s husband: {person.husband.name}")

if __name__ == "__main__":
    main()
