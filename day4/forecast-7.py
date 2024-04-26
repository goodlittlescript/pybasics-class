#
# One choice can pick the probabilities for another.
#
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

# 1 out of 10 happy, 1 out of 10 hot ... if sun
# 1 out of 10 miserable, 1 out of 10 cold ... if rain
possible_moods = {
    "sun": ["happy", "hot", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"],
    "rain": ["miserable", "cold", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"],
}

for index in range(0, 10):
    weather = random.choice(possible_weather)
    possible_moods_given_weather = possible_moods[weather]
    mood = random.choice(possible_moods_given_weather)
    print(f"I predict day {index} will have {weather} and I will be {mood}")
