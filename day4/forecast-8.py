import random

# random is not truly random - it is pseudo-random meaning it is a
# random series based on a seed value. The series is random but
# given the same seed you will always get the same series.
#
# Normally the seed is set to something ever-changing like
# the current time, but we can fix it to get the same choices
# every time (helpful for testing).
#
# Try one of these...

# random.seed(0)
# random.seed(1)
# random.seed(42)

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

possible_moods = {
    "sun": ["happy", "hot", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"],
    "rain": ["miserable", "cold", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"],
}

for index in range(0, 10):
    weather = random.choice(possible_weather)
    possible_moods_given_weather = possible_moods[weather]
    mood = random.choice(possible_moods_given_weather)
    print(f"I predict day {index} will have {weather} and I will be {mood}")
