# List of animals
animals = ["dog", "cat", "bird", "dog", "horse", "penguin"]

# Check if 'dog' is in the list and print its first occurrence index
if "dog" in animals:
    print(animals.index("dog"))

# To know how many times 'dog' exists in the list
print(animals.count("dog"))

# Finding all indices of 'dog' in the list
dog_indices = [index for index, animal in enumerate(animals) if animal == "dog"]
print("All indices of 'dog':", dog_indices)

# Check if any of a list of animals is in the list
search_animals = ["cat", "elephant"]
found_animals = [animal for animal in search_animals if animal in animals]
print("Found animals from search list:", found_animals)

# Check if all animals from another list are in the list
if all(animal in animals for animal in search_animals):
    print("All search animals are in the list")
else:
    print("Not all search animals are in the list")
