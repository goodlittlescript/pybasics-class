# Protect against unknowns

animals = {
    "horse": {"name": "horse", "top_speed_in_mph": 44, "food": "hay"},
    "penguin": {"name": "penguin", "top_speed_in_mph": 5.6, "food": "krill"},
}

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
