# Group facts into dictionaries (key-value pairs).

#
# A colon separates key from value. A comma separates pairs.
# Get values using []
#

horse = {
    "name": "horse",
    "top_speed_in_mph": 44,
    "food": "hay",
}

penguin = {
    "name": "penguin",
    "top_speed_in_mph": 5.6,
    "food": "krill",
}

name = horse["name"]
top_speed_in_mph = horse["top_speed_in_mph"]
food = horse["food"]

print(f"A {name} has a top speed of {top_speed_in_mph} and eats {food}")

name = penguin["name"]
top_speed_in_mph = penguin["top_speed_in_mph"]
food = penguin["food"]

print(f"A {name} has a top speed of {top_speed_in_mph} and eats {food}")
