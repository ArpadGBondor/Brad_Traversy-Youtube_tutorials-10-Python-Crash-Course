# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'  # str
# name = "Jack"  # str
# is_cool = True  # bool

print('Hello')

# Multiple assignments
x, y, name, is_cool = (1, 2.5, 'John', True)


# Basic math
a = x + y
print(x,y,name,is_cool,a)

print(type(x))
print(type(y))
print(type(name))
print(type(is_cool))
print(type(a))

# Casting
x_str = str(x)
x_float = float(x)
print(x,type(x))
print(x_str,type(x_str))
print(x_float,type(x_float))

y_int = int(y)              # 2.5 -> 2
y_int_float = float(y_int)  # 2 -> 2.0
print(y,type(y))
print(y_int,type(y_int))
print(y_int_float,type(y_int_float))

