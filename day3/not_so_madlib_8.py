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
def animal_facts(animal):
    name = animal["name"]
    top_speed_in_mph = animal["top_speed_in_mph"]
    food = animal["food"]
    return f"A {name} has a top speed of {top_speed_in_mph} and eats {food}"


print("Let's do a not-so-madlib! Give me a...")
animal_name = input("Animal: ")
print("---")

if animal_name in animals:
    animal = animals[animal_name]
    print(animal_facts(animal))
else:
    print(f"Unknown animal: {animal_name}")
