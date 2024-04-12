print("Let's do a madlib! Give me a...")
noun = input("Noun: ")
location = input("Location: ")
verb = input("Verb: ")
print("---")

# multiline strings use fences

print(
    f"""
I'm gonna take my {noun} to the old town {location}
I'm gonna {verb} 'til I can't no more
"""
)

# you can use \ to "escape" the newlines

# print(f"""\
# I'm gonna take my {noun} to the old town {location}
# I'm gonna {verb} 'til I can't no more\
# """)

# escapes come up in other places too...

# print("I want to \"put quotes\" into my \"quoted string\" so everything \"just works\"")
