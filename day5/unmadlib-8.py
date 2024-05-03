madlib = """\
I'm gonna be what I want, what I want
What I want, yeah (what I want, what I want)
"""

# You can also use regular expressions to change text
import re

verb = "swim"
result = re.sub("want", verb, madlib)
print(result)
