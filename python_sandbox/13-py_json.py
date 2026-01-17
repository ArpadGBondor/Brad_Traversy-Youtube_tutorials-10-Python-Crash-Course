# JSON is commonly used with data APIS. Here how we can parse JSON into a Python
# dictionary

import json

# Sample JSON
userJSON = '{"first_name":"John","last_name":"Doe","age":30}'

print(userJSON)

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user["first_name"])

# Dictionary to JSON

car = {"make": "Vauxhall", "model": "Astra", "year": 2010}

print(car)

carJSON = json.dumps(car)

print(carJSON)
