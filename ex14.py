# pylint: disable=invalid-name, missing-docstring
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print("We have", count, "even numbers")
