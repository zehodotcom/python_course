# Infinite loops
# Loops happen when there is no exit condition, and would run forever. Whenever there is a loop, make sure there is an exit condition.

while True:
    word = input("$")
    print(word)
    if word.lower() == "exit":
        break
