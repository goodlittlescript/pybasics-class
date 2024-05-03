madlib = """\
I'm gonna take my hockey stick to the old town road
I'm gonna ride 'til I can't no more
"""

# Regular expressions are another strategy
# These allow you to write the reverse of interpolation.
# Use () to define capture groups

import re

pattern = """\
I'm gonna take my (.*) to the old town (.*)
I'm gonna (.*) 'til I can't no more
"""

result = re.match(pattern, madlib)

answers = {
    "noun": result.group(1),
    "location": result.group(2),
    "verb": result.group(3),
}

print(answers)
