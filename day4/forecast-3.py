#
# Using lists we can write out our "forecasts"
#
history = ["sun", "sun", "sun", "sun", "rain", "sun", "sun", "sun", "sun", "sun"]

for index, weather in enumerate(history):
    print(f"I predict day {index} will have: {weather}")
