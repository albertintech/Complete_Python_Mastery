# pylint: disable=invalid-name, missing-docstring

import math

result = 2 + 2
print(result)
result = 2 * 5
print(result)

x = 1
y = 1
unit = 3
print(x * y * unit)

is_published = False
has_cs_degree = True
course_name = "Python Mastery"

print(math.pi)
print(len(course_name))
print("Howdy do 'my' partner?!")
print(course_name[0:6])
print(course_name[7:-1])
print(course_name[::-1])  # reverse a string

print(round(2.9))
print(abs(-2.9))

# Falsy Values
# ""
# 0
# None

print(bool(""))
print(bool("spam"))

print(ord("b"))
print(ord("B"))

age = 12
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligilbe"

message = "Eligible" if age >= 18 else "Not eligible"

print(message)
