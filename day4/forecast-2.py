# Lists are "lists of values". They're a data structure like dictionaries.

#
# A comma separates items.
#

letters = ["a", "b", "c"]

#
# Get values using []
# Zero based indexing
#

print(letters[0])
# a
print(letters[1])
# b
print(letters[2])
# c

#
# Out of range causes an error
#

print(letters[3])
# IndexError: list index out of range

#
# Set values using []=
#

letters[0] = "A"
print(letters)
# ['A', 'b', 'c']

#
# Can't assign outside of existing range
# but you can append/concat
#

letters[3] = "d"
# IndexError: list assignment index out of range

letters.append("d")
print(letters)
# ['A', 'b', 'c', 'd']

letters += ["e", "f", "g"]
print(letters)
# ['A', 'b', 'c', 'd', 'e', 'f', 'g']

#
# You can iterate lists
#

for letter in letters:
    print(f"letter: {letter}")
# letter: A
# letter: b
# letter: c
# letter: d
# letter: e
# letter: f
# letter: g

#
# You can enumerate lists
#

for index, letter in enumerate(letters):
    print(f"{index}: {letter}")
# 0: A
# 1: b
# 2: c
# 3: d
# 4: e
# 5: f
# 6: g

#
# Interesting things...
#

# negative index
letters[-1]
# g
letters[-2]
# f

# multiply value to make list
["a"] * 2
# ['a', 'a']
["a", "b"] * 2
# ['a', 'b', 'a', 'b']
