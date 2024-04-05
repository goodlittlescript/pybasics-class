#
# There are other types of objects with other functions.
#

the_string = "hello world"
the_integer = 1

print("------------------------")
print("attributes of the string")
print(dir(the_string))

# swapcase
print(the_string.swapcase())

print("------------------------")
print("attributes of the integer")
print(dir(the_integer))

# addition
print(the_integer + 2)

# multiplication
print(the_integer * 2)

# equality
print(the_integer == 1)
print(the_integer == 2)
print(the_integer == (10 - 9))

#
# Notably many of these have an internal function associated.
#

print(the_integer.__add__(2))
print(the_integer.__mul__(2))
print(the_integer.__eq__(10 - 9))
