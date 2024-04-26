#
# Another option is to use `choice` on each iteration.
#
import random

history = ["sun", "sun", "sun", "sun", "rain", "sun", "sun", "sun", "sun", "sun"]

for index in range(0, 10):
    weather = random.choice(history)
    print(f"I predict day {index} will have: {weather}")
