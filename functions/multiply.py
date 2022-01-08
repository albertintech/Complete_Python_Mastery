"""A program to demonstrate debuggin in VS Code"""

def multiply(*numbers):
    """Missing docstring"""
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(multiply(1,2,3))
