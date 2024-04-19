# Values can be anything, including other dictionaries

animals = {
    "horse": {"name": "horse", "top_speed_in_mph": 44, "food": "hay"},
    "penguin": {"name": "penguin", "top_speed_in_mph": 5.6, "food": "krill"},
}

animal = animals["horse"]
name = animal["name"]
top_speed_in_mph = animal["top_speed_in_mph"]
food = animal["food"]

print(f"A {name} has a top speed of {top_speed_in_mph} and eats {food}")

animal = animals["penguin"]
name = animal["name"]
top_speed_in_mph = animal["top_speed_in_mph"]
food = animal["food"]

print(f"A {name} has a top speed of {top_speed_in_mph} and eats {food}")
