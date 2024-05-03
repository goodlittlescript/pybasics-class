madlib = """\
I'm gonna take my hockey stick to the old town road to the old town road
I'm gonna ride 'til I can't no more
"""

# Regular expressions can also be fooled because of ambigities.
#
# What should the answer be?
#
#   noun = "hockey stick to the old town road"
#   location = "road"
#   verb = "ride"
#
# Or
#
#   noun = "hockey stick"
#   location = "road to the old town road"
#   verb = "ride"
#
# Both produce the same madlib text.

import re

pattern = """\
I'm gonna take my (.+) to the old town (.+)
I'm gonna (.+) 'til I can't no more
"""

result = re.match(pattern, madlib)

answers = {
    "noun": result.group(1),
    "location": result.group(2),
    "verb": result.group(3),
}

print(answers)

# Regex have MANY flags to allow you to get specific about
# what you want to match
#
# Here the '?' modifier means "shortest possible match". By
# default it will be "longest possible match"
#
# https://docs.python.org/3/library/re.html#regular-expression-syntax

altpattern = """\
I'm gonna take my (.+?) to the old town (.+)
I'm gonna (.+) 'til I can't no more
"""

result = re.match(altpattern, madlib)

answers = {
    "noun": result.group(1),
    "location": result.group(2),
    "verb": result.group(3),
}

print(answers)
