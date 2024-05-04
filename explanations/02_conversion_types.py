example_number = 784

# Convert to float
float_number = float(example_number)
print("Value as float:", float_number)

# Convert to string
string_number = str(example_number)
print("Value as string:", string_number)

# Convert to boolean
boolean_number = bool(example_number)
print("Value as boolean:", boolean_number)

# Convert to integer - is an example, since the conversion is not necessary because that number was integer
integer_number = int(example_number)
print("Value as integer:", integer_number)

# In Python there is a concept called Truthy and Falsy, i.e. certain data types will be evaluated
# as true or truthy and others as false or falsy (“”, 0, None)
print(bool("car"))  # True
print(bool(""))  # False
print(bool("0"))  # True
print(bool(None))  # False
print(bool(0))  # False
print(bool(3.765))  # True
