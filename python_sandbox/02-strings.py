# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Gabriel"
age = 39

# Concatenate
print("Hello, my name is " + name + " and I am " + str(age) + ".")

# String Formatting
print("My name is {name} and I am {age}.".format(name=name, age=age))

# F-Strings (3.6+)
print(f"My name is {name} and I am {age}.")

# String Methods
s = "hello world"
S = "HELLO WORLD"

# Capitalise string
print(
    f'Capitalise string "{s}" -> "{s.capitalize()}"'
)  # "hello world" -> "Hello world"

# Make all uppercase
print(f'Make all uppercase "{s}" -> "{s.upper()}"')  # "hello world" -> "HELLO WORLD"

# Make all lowercase
print(f'Make all lowercase "{S}" -> "{S.lower()}"')  # "HELLO WORLD" -> "hello world"

# Swap case
print(f'Swap case "{S}" -> "{S.swapcase()}"')  # "HELLO WORLD" -> "hello world"
print(f'Swap case "{s}" -> "{s.swapcase()}"')  # "hello world" -> "HELLO WORLD"

# Get length
print(f'Length "{s}" -> {len(s)}')  # "hello world" -> 11

# Replace
print(
    f'Replace "{s}" -> "{s.replace('world','everyone')}"'
)  # "hello world" -> "hello everyone"

# Count
sub = "l"
print(f'Count "{sub}" in "{s}" -> {s.count(sub)}')  # "hello world" -> 3

# Starts with
sub = "hello"
print(f'Starts with "{sub}": "{s}" -> {s.startswith(sub)}')  # "hello world" -> True

# Ends with
sub = "world"
print(f'Ends with "{sub}": "{s}" -> {s.endswith(sub)}')  # "hello world" -> True

# Split into a list
print(f'Split into a list "{s}" -> {s.split()}')  # "hello world" -> ['hello', 'world']

# Find position
print(f'Find position "{s}" -> {s.find('r')}')  # "hello world" -> 8
print(">>> note: position is indexed from 0")

# Is all alphanumeric
print(f'Is all alphanumeric "{s}" -> {s.isalnum()}')  # "hello world" -> False
alnum = "HelloWorld123"
print(f'Is all alphanumeric "{alnum}" -> {alnum.isalnum()}')  # "HelloWorld123" -> True

# Is all alphabetic
print(f'Is all alphabetic "{s}" -> {s.isalpha()}')  # "hello world" -> False
print(f'Is all alphabetic "{alnum}" -> {alnum.isalpha()}')  # "HelloWorld123" -> False
alpha = "HelloWorld"
print(f'Is all alphabetic "{alpha}" -> {alpha.isalpha()}')  # "HelloWorld" -> True

# Is all numeric
print(f'Is all numeric "{s}" -> {s.isnumeric()}')  # "hello world" -> False
numeric = "12345"
print(f'Is all numeric "{numeric}" -> {numeric.isnumeric()}')  # "12345" -> True
