# Strings are objects
# They have function you can call on them
# Calling a function looks like this...

print("hello world")
print("hello world".upper())
print("hello world".title())
print("hello world".capitalize())

# You can see what functions and other attributes are available on
# an object by calling the __dir__ function.

print("hello world".__dir__())

# The functions with double-underscores are special and often implement
# other things in the language. For example __dir__ implements the "dir"
# function. We speak of them as "internal" functions. Generally they
# aren't used directly.
print(dir("hello world"))
