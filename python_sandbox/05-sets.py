# SET: A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {"Apples", "Oranges", "Bananas"}

print(fruits_set)

# Check if in set
print(f'Apples in: {"Apples" in fruits_set}')

# Add to set
fruits_set.add("Grapes")
print(f"Grapes added: {fruits_set}")
print(
    ">>> Comment: Never rely on the order of a set. Ever. Order can change between runs."
)
print(">>> Run 1: Grapes added: {'Oranges', 'Grapes', 'Apples', 'Bananas'}")
print(">>> Run 2: Grapes added: {'Apples', 'Grapes', 'Bananas', 'Oranges'}")
print(">>> Run 2: Grapes added: {'Apples', 'Bananas', 'Oranges', 'Grapes'}")

# Remove from set
fruits_set.remove("Bananas")
print(f"Bananas removed: {fruits_set}")


# Clear set
fruits_set.clear()
print(f"Cleared set: {fruits_set}")

# Delete set
del fruits_set
# print(f"ERROR: {fruits_set}")
# NameError: name 'fruits_set' is not defined
