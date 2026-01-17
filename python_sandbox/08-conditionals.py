# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple IF
print("IF")
if x > y:
    print(f"{x} is greater than {y}")

# IF + ELSE
print("IF+ELSE")
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not greater than {y}")

# IF + ELIF + ELSE
print("IF+ELIF+ELSE")
if x > y:
    print(f"{x} is greater than {y}")
elif y > x:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} and {y} are equal")

# NESTED IF
print("NESTED IF")
if x > 2:
    if x <= 10:
        print(f"{x} is greater than 2 and less or equal to 10.")

# Logical operators (and, or, not) - Used to combine conditional statements

# and
print("logical and")
if x > 2 and x <= 10:
    print(f"{x} is greater than 2 and less or equal to 10.")

# and
print("logical or")
if x > 22 or x <= 10:
    print(f"{x} is greater than 22 or less or equal to 10.")

# and
print("logical not")
if not (x == y):
    print(f"{x} not equal to {y}.")


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

# IN
if x in numbers:
    print(f"x: {x} is in {numbers}")
if y in numbers:
    print(f"y: {y} is in {numbers}")

# NOT IN
if x not in numbers:
    print(f"x: {x} is not in {numbers}")
if y not in numbers:
    print(f"y: {y} is not in {numbers}")

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is y:
    print(f"x: {x} is y: {y}")

if x is not y:
    print(f"x: {x} is not y: {y}")

z = 10

if x is z:
    print(f"x: {x} is z: {z}")
if x is not z:
    print(f"x: {x} is not z: {z}")

# let's compare different types


def compare(x, y):
    if x is y:
        print(f"x: {x} is y: {y}")
    if x is not y:
        print(f"x: {x} is not y: {y}")


# int
print(type(1))
compare(1, 1)  # is
compare(1, 2)  # is not

# str
print(type("a"))
compare("a", "a")  # is
compare("a", "b")  # is not

# tuple
print(type(("a", "a")))
compare(("a", "a"), ("a", "a"))  # is <-- !!!

# list
print(type(["a", "a"]))
compare(["a", "a"], ["a", "a"])  # is not

# set
print(type({"a", "a"}))
compare({"a", "a"}, {"a", "a"})  # is not

# dict
print(type({"a": "a"}))
compare({"a": "a"}, {"a": "a"})  # is not
