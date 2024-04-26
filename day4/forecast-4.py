# https://docs.python.org/3/library/random.html
import random

history = ["sun", "sun", "sun", "sun", "rain", "sun", "sun", "sun", "sun", "sun"]
random.shuffle(history)

for index, weather in enumerate(history):
    print(f"I predict day {index} will have: {weather}")
