# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]

fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)
print(f"Fruits: {fruits}")

# Get a value
print(f"Fruit #1: {fruits[1]}")

# Get length
print(f"Fruits length: {len(fruits)}")

# Append to list
fruits.append("Mangos")
print(f"Appended mangos: {fruits}")

# Remove from list
fruits.remove("Grapes")
print(f"Removed grapes: {fruits}")

# In sert into position
fruits.insert(2, "Strawberries")
print(f"Inserted strawberries at #2: {fruits}")

# Change value
fruits[0] = "Blueberries"
print(f"Changed #0 to blueberries: {fruits}")

# Remove position
print(f"Popped position #1: {fruits.pop(1)}")
print(f"Fruits: {fruits}")

# Reverse list
fruits.reverse()
print(f"Reversed: {fruits}")

# Sort list
fruits.sort()
print(f"Sorted: {fruits}")

# Reverse sort list
fruits.sort(reverse=True)
print(f"Reverse sorted: {fruits}")
