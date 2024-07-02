# List unpacking is a powerful feature in Python that allows you to assign the elements of a list to multiple variables in a single statement.
# This can make your code cleaner and more readable.

numbers = [1, 2, 3]
# we give a name to each element
first, second, third = numbers
print(first, second, third)

# You can unpack lists of different lengths using the * operator, which captures the remaining elements
first, *other = numbers  # other contains the values of 2 and 3 packed in a list
print(numbers)
first, *other, third = numbers
print(numbers)

# If you want to ignore certain elements during unpacking, you can use the _ variable conventionally as a placeholder
data = ["Alex", 40, "Engineer", "London"]

# Unpack the list, ignoring the third element
name, age, _, city = data

print(name, "-", age, "-", city)
