print("Let's do a madlib! Give me a...")

# Functions exist because they solve some
# problem common enough to make them worthwhile

noun = input("Noun: ".ljust(10))
location = input("Location: ".ljust(10))
verb = input("Verb: ".ljust(10))
print("---")

print(
    f"""
I'm gonna take my {noun} to the old town {location}
I'm gonna {verb} 'til I can't no more
"""
)
