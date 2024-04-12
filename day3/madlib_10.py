import sys

#
# Use this like:
#
#  python3 madlib_10.py < answers.txt 2>/dev/null
#
# The "<" is a redirection where the inputs come from the file rather
# than a person typing them in.
#


def get_word(type):
    sys.stderr.write(f"{type.ljust(10)}: ")
    sys.stderr.flush()
    response = input()

    # If a user is typing then stdin will be a "tty" (teletypewriter).
    # If a file provided the input then stdin will not be a tty and as
    # a result the user will not see the inputs because they did not
    # type them. In that case echo back the response so our formatting
    # remains good.
    if not sys.stdin.isatty():
        sys.stderr.write(response + "\n")
        sys.stderr.flush()

    return response


sys.stderr.write("Let's do a madlib! Give me a...\n")
sys.stderr.flush()
noun = get_word("Noun")
location = get_word("Location")
verb = get_word("Verb")
sys.stderr.write("---\n")
sys.stderr.flush()

print(
    f"""
I'm gonna take my {noun} to the old town {location}
I'm gonna {verb} 'til I can't no more
"""
)
