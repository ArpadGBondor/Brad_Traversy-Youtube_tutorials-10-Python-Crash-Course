# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Paul", "Sara", "Susan"]

# Simple for loop
print("Simple loop")
for person in people:
    print(f"Current person: {person}")

# Break
print("Break")
for person in people:
    if person == "Sara":
        break
    print(f"Current person: {person}")

# Break
print("Continue")
for person in people:
    if person == "Sara":
        continue
    print(f"Current person: {person}")

# Range
print("Range")
for i in range(len(people)):
    print(f"i: {i} - type: {type(i)} - person: {people[i]}")

print("Custom range")
for i in range(0, 11):
    print(f"i: {i}")
for i in range(100, 105):
    print(f"i: {i}")

# While loops execute a set of statements as long as a condition is true.

print("while loop")

count = 0
while count <= 10:
    print(count)
    count += 1

count = 0
while count < len(people):
    print(f"count: {count} - person: {people[count]}")
    count += 1
