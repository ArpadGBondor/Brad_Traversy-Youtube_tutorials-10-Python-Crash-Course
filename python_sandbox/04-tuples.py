# TUPLE: A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_tuple = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

print(fruits_tuple)

# Single value needs trailing comma
fruits2_tuple = ("Apples",)

# Get value
print(f"Value #1: {fruits_tuple[1]}")

# CANNOT change value
# fruits[0] = "Bananas"
# TypeError: 'tuple' object does not support item assignment

# Delete tuple
del fruits2_tuple
# print(fruits2)
# NameError: name 'fruits2' is not defined. Did you mean: 'fruits'?

# Length
print(f"Fruits length: {len(fruits_tuple)}")
