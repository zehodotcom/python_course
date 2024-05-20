# Logical operators in Python (AND, OR, NOT) are used to combine conditional statements, returning True or False based on the logic applied.
# They help in decision-making by evaluating multiple conditions simultaneously.

fuel = True
engine_on = True
age = 18

# Check if the person can start the journey if they have fuel and the engine is on and they are older than 17
if fuel and (engine_on and age > 17):
    print("You can start the journey")

# Check if the person can start the journey if they have fuel and either the engine is on or they are older than 17
if fuel and (engine_on or age > 17):
    print("You can start the journey")

# Check if the person cannot start the journey if they do not have fuel but either the engine is on or they are older than 17
if not fuel and (engine_on or age > 17):
    print("You cannot start the journey")
