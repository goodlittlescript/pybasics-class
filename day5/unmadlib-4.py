madlib = """\
I'm gonna take my hockey stick to the old town road
I'm gonna ride 'til I can't no more
"""

# Does not work well for irregular strings
madlib_words = madlib.split()
print(madlib_words)

answers = {
    "noun": madlib_words[4],
    "location": madlib_words[9],
    "verb": madlib_words[12],
}

print(answers)
