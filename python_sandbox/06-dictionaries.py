# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dictionary
person = {"first_name": "John", "last_name": "Doe", "age": 30}
print(person, type(person))

# Use constructor
person2 = dict(first_name="Sara", last_name="Williams", age=23)
print(person2, type(person2))

# Get value
print(f"Get first name: {person['first_name']}")
print(f"Get last name: {person.get('last_name')}")

# Add key/value
person["phone"] = "555-555-5555"
print(f"phone added: {person}")

# Get dictionary keys
print(f"person keys: {person.keys()}")
print(f"type: {type(person.keys())}")

# Get dictionary items
print(f"person items: {person.items()}")
print(f"type: {type(person.items())}")

# Copy dictionary
person_copy = person.copy()
print(f"person: {person}")
print(f"copy: {person_copy}")

person["email"] = "person@company.com"

print(f"email added: {person}")
print(f"copy: {person_copy}")

# Remove item
del person["age"]
print(f"age removed: {person}")

person.pop("phone")
print(f"phone removed: {person}")

# Clear
person.clear()
print(f"cleared: {person}")

# Length
print(f"person2: {person2}")
print(f"length: {len(person2)}")

# Delete
del person
# print(f"deleted: {person}")
# NameError: name 'person' is not defined.

# List of dictionary
people = [
    {"name": "Martha", "age": 30},
    {"name": "Kevin", "age": 23},
    {"name": "Ben", "age": 55},
]
print(f"people: {people}")
print(f"people[1]: {people[1]}")
