# Define a list of animals
animals = ["bird", "cat", "dog", "rat", "horse"]

# Print the first element of the list
print(animals[0])

# Change the first element of the list
animals[0] = "cow"
print(animals)

# Print the elements of the list starting from the third element
print(animals[2:])

# Print the last element of the list
print(animals[-1])

# Print every second element of the list (even-indexed elements)
print(animals[::2])

# Create a list of numbers from 0 to 20
numbers = list(range(21))
print(numbers)

# Print all the odd numbers from the list
print(numbers[1::2])
# Outputs: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# This prints all the odd numbers from the list by starting from the second element and taking every second element thereafter.
