import sys

#
# Use this like:
#
#  python madlib_9.py
#  python madlib_9.py < answers.txt
#
# The "<" is a redirection where the inputs come from the file rather
# than a person typing them in.
#


def get_word(type):
    response = input(f"{type.ljust(10)}: ")

    # If a user is typing then stdin will be a "tty" (teletypewriter).
    # If a file provided the input then stdin will not be a tty and as
    # a result the user will not see the inputs because they did not
    # type them. In that case echo back the response so our formatting
    # remains good.
    if not sys.stdin.isatty():
        print(response)

    return response


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
