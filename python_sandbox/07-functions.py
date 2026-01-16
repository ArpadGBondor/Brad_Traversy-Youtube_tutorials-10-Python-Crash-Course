# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name="Sam"):
    print(f"Hello {name}!")


sayHello("Alma")
sayHello()  # default Sam


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


print(f"2+3={getSum(2,3)}")
num = getSum(4, 5)
print(f"4+5={getSum(4,5)}")

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one
# expression. Very similar to JS arrow functions


getSum_lambda = lambda num1, num2: num1 + num2

print(f"2+3={getSum_lambda(2,3)}")
num = getSum(4, 5)
print(f"4+5={getSum_lambda(4,5)}")
