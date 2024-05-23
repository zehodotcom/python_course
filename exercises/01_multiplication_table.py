# Get the number from the user
number = int(input("Enter a number: \n"))

# Print the multiplication table for the entered number
print(f"Multiplication table for {number}:\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
