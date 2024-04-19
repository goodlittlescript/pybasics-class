# Or to change the data

# data
animals = {
    "horse": {"name": "american quarter horse", "top_speed_in_mph": 44, "food": "hay"},
    "penguin": {"name": "emperor penguin", "top_speed_in_mph": 5.6, "food": "krill"},
    "sloth": {"name": "three-toed-sloth", "top_speed_in_mph": 0.17, "food": "leaves"},
    "fish": {"name": "goldfish", "top_speed_in_mph": 0.86, "food": "algae"},
    "dog": {"name": "german shepard", "top_speed_in_mph": 30, "food": "everything"},
}

# code
print("Let's do a not-so-madlib! Give me a...")
animal_name = input("Animal: ")
print("---")

if animal_name in animals:
    animal = animals[animal_name]
    name = animal["name"]
    top_speed_in_mph = animal["top_speed_in_mph"]
    food = animal["food"]

    print(f"A {name} has a top speed of {top_speed_in_mph} and eats {food}")
else:
    print(f"Unknown animal: {animal_name}")
