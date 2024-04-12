import sys


def prompt_str(type):
    return f"{type.ljust(10)}: "


def get_word(type):
    response = input(prompt_str(type))

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
