madlib_1 = """\
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
"""
madlib_2 = """\
I'm gonna take my pencil to the old town school
I'm gonna write 'til I can't no more
"""
madlib_3 = """\
I'm gonna be what I want, what I want
What I want, yeah (what I want, what I want)
"""

# You can also use regular expressions to identify when text matches.
# Matches are truthy.
# Non-matches are "None" a falsey value.
import re

pattern = """\
I'm gonna take my (.+) to the old town (.+)
I'm gonna (.+) 'til I can't no more
"""

result = re.match(pattern, madlib_1)
if result:
    print(f"match:\t{result}")
else:
    print(f"not a match:\t{result}")

result = re.match(pattern, madlib_2)
if result:
    print(f"match:\t{result}")
else:
    print(f"not a match:\t{result}")

result = re.match(pattern, madlib_3)
if result:
    print(f"match:\t{result}")
else:
    print(f"not a match:\t{result}")
