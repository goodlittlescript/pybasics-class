comma_separated_values = """
horse,road,ride
pencil,school,write
""".strip()

# Slice and dice works really well
# for very orderly strings.
lines = comma_separated_values.split("\n")
for line in lines:
    noun, location, verb = line.split(",")

    answers = {
        "noun": noun,
        "location": location,
        "verb": verb,
    }

    print(answers)
