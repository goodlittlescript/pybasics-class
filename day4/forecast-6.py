import random

# 1 out of 10 rain
possible_weather = [
    "sun",
    "sun",
    "sun",
    "sun",
    "sun",
    "sun",
    "sun",
    "sun",
    "sun",
    "rain",
]

for index in range(0, 10):
    weather = random.choice(possible_weather)
    print(f"I predict day {index} will have: {weather}")
