name = "Antonio"
surname = "Reyes"
# Concatenate the first name and last name with a space in between to form the full name
full_name = f"{name} {surname}"
print(full_name)

animal = " gorilla "
sentence = "Python is a powerful programming language"
word = "python"

## Python Common String Methods

print(animal.upper())  # Output: " GORILLA "
print(animal.lower())  # Output: " gorilla "
print(animal.capitalize())  # Output: " gorilla " (first letter capitalized)
print(animal.title())  # Output: " Gorilla " (first letter of each word capitalized)
print(animal.strip())  # Output: "gorilla" (removes leading and trailing whitespace)
print(animal.rstrip())  # Output: " gorilla" (removes trailing whitespace)
print(animal.lstrip())  # Output: "gorilla " (removes leading whitespace)
print(animal.strip().capitalize())  # Output: "Gorilla" (strips then capitalizes)
print(animal.find("illa"))  # Output: 4 (index where "illa" starts)
print(
    animal.replace("illa", "ILLA")
)  # Output: " gorILLA " (replaces "illa" with "ILLA")
print("ILLA" in animal)  # Output: False (checks if "ILLA" is in the string)
print("ILLA" not in animal)  # Output: True (checks if "ILLA" is not in the string)
print(
    animal.isupper()
)  # Output: False (checks if all characters in the string are uppercase)
print(
    animal.islower()
)  # Output: True (checks if all characters in the string are lowercase)
print(
    sentence.startswith("Python")
)  # Output: True (checks if the string starts with "Python")
print(
    sentence.endswith("language")
)  # Output: True (checks if the string ends with "language")
