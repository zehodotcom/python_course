# Functions in Python are reusable blocks of code designed to perform a specific task as well as to avoid repeating code


# Function without Arguments, def is the keyword used to define a function.
def greet():
    print("Hello there")


greet()


# Function with Arguments
def greet2(name):
    print(f"Hello, {name}!")


greet2("Alice")


# Function with Optional Parameters
def hello(name, surname=""):
    print(f"hello {name} {surname}")


hello("Steve", "Wilson")
hello("Bryan")
