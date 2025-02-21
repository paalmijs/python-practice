# for loops are different from while loops in that they are used to iterate over a sequence.
# For example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# This will print out apple, banana, and cherry.
# This is a simple example of a for loop.

# You can also loop through a string:
for x in "banana":
    print(x)
# This will print out b, a, n, a, n, a.
# This is a simple example of a for loop.

# You can also break out of a loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# This will print out apple, banana.
# This is a simple example of a for loop break.

# You can also continue to the next iteration:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# This will print out apple, cherry.
# This is a simple example of a for loop continue.

# You can also use the range() function to loop through a set of code a specified number of times:
for i in range(6):
    print(i)
# This will print out 0, 1, 2, 3, 4, 5.
# This is a simple example of a for loop with the range function.