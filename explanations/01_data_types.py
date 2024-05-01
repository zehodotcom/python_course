# Importing Enum module
from enum import Enum

# DATA TYPES IN PYTHON

# String - are sequences of characters enclosed within single quotes ('') or double quotes (""). They represent text data and can contain letters, numbers, symbols, and spaces.
my_string = "Hello there"
print("Greetings:", my_string)

# Integer - represent whole numbers without any decimal point. They can be positive, negative, or zero.
my_integer = 42
print("My Integer:", my_integer)

# Float - represent real numbers with a decimal point. They can also be expressed in scientific notation.
my_float = 3.14
print("My Float:", my_float)

# Boolean - represent truth values, typically either True or False. They are often used in conditional statements and logical operations.
is_adult = True
print("is an adult?:", is_adult)

# None - represents the absence of a value or a null value. It is often used to indicate that a variable has not been assigned a value yet or as a placeholder.
my_none = None
print(my_none)

# List - are ordered collections of items, which can be of different data types. They are mutable, meaning their elements can be changed after creation. Lists are defined using square brackets [].
animals = [
    "dog",
    "cat",
    "bird",
    "dog",
    "horse",
    "elephant",
]
print(animals)

# Tuple - are similar to lists but are immutable, meaning their elements cannot be changed after creation. They are defined using parentheses ().
my_tuple = (
    1,
    "two",
    3.0,
)
print(my_tuple)

# Dictionary - are unordered collections of key-value pairs. Each key is associated with a value, allowing for efficient lookup and retrieval of data. Dictionaries are defined using curly braces {}.
book = {
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "year": 1997,
    "genre": "Fantasy",
}
print(book)

# Set - are unordered collections of unique elements. They are useful for tasks like removing duplicates from a list or testing membership. Sets are defined using curly braces {}.
fruits = {
    "watermelon",
    "orange",
    "lemon",
    "cherry",
    "banana",
    "apple",
}
print(fruits)


# Define an Enum class
class Color(Enum):
    BLACK = 1
    BLUE = 2
    WHITE = 3
    RED = 4
    GREEN = 5
    YELLOW = 6


# Enum -  are a way to define symbolic names for constant values.
color_black = Color.BLACK
print("What color is it?:", color_black.name)
