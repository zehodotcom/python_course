# The ternary operator in Python is a shorthand for the if-else statement that allows a conditional expression to be written in a single line.
# It follows the syntax: value_if_true if condition else value_if_false.

# We have a classic if-else example
age = 48
if age >= 18:
    print("Is an adult")
else:
    print("Is a minor")

# The above example can be simplified with a ternary operator:
age = 20
message = "Is an adult" if age >= 18 else "Is a minor"
print(message)

# The ternary operator can also be used directly with Python's print statement:
age = 16
print("Is an adult" if age >= 18 else "Is a minor")
