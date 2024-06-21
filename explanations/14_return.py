# The return keyword in Python is used within a function to exit the function and optionally pass an expression back to the caller.
# When a function is called, it executes the statements within the function body.
# The return statement is used to send a result back to where the function was invoked. If no return statement is present, the function returns None by default.


def add(a, b):
    result = a + b
    return result


sum = add(1, 2)
print(sum)
