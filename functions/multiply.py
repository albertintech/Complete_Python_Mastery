"""A program to demonstrate debuggin in VS Code"""

def multiply(*numbers):
    """Missing docstring"""
    total = 1
    for number in numbers:
        total *= number
    return total # move this line to the right to demo error

print("Start")
print(multiply(1,2,3))
