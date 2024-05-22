# For loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each element in the sequence.
# It simplifies repetitive tasks by automating the iteration process

# Access elements of the list one by one
languages = ["C#", "Javascript", "Python"]
for i in languages:
    print(i)

# The range() function returns a sequence of numbers
for number in range(9):
    print(number)

print("-----------")

# Using range() with Start and Step. In this case generates numbers from 2 to 9, incrementing by 2 each time
for i in range(2, 10, 2):
    print(i)

# Strings as an iterable
language = "Python"
for x in language:
    print(x)

print("-----------")

# For - else
search = 86
for number in range(6):
    print(number)
    if number == search:
        print("Number found!", search)
        break
else:
    print("Number not found!")

# Iterating Over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating Over a Dictionary
student_grades = {"Steve": 91, "Charlie": 85, "Adam": 93}
for name, grade in student_grades.items():
    print(f"{name} has a grade of {grade}")

# Nested Loops
# A for loop inside another for loop (nested loop) can be used to iterate over multi-dimensional data structures
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
