# Often you can pull out the repeated parts and
# you get a "nice" program as a result


def get_word(type):
    return input(f"{type}: ".ljust(10))


print("Let's do a madlib! Give me a...")
noun = get_word("Noun")
location = get_word("Location")
verb = get_word("Verb")
print("---")

print(
    f"""
I'm gonna take my {noun} to the old town {location}
I'm gonna {verb} 'til I can't no more
"""
)
