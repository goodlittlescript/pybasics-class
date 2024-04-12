print("Let's do a madlib! Give me a...")
noun = input("Noun: ")
location = input("Location: ")
verb = input("Verb: ")
print("---")

# f-strings (format strings) are a shorthand
# way to interpolate values into a string.
#
# You will probably use this A LOT.

print(f"I'm gonna take my {noun} to the old town {location}")
print(f"I'm gonna {verb} 'til I can't no more")

#
# There are similar alternatives like this...
#

# print("I'm gonna take my {} to the old town {}".format(noun, location))
# print("I'm gonna {} 'til I can't no more".format(verb))

#
# and this...
#

# print("I'm gonna take my %s to the old town %s" % (noun, location))
# print("I'm gonna %s 'til I can't no more" % (verb))
