# Load data from file...
import json

# data
with open("ace_high.json") as f:
    cards = json.loads(f.read())


# code
def card_names(card_1, card_2):
    return f"{card_1['name']},{card_2['name']}"


def total_value(card_1, card_2):
    return card_1["value"] + card_2["value"]


print("Let's play a game! Give me two cards...")
card_name_1 = input("Card 1: ")
card_name_2 = input("Card 2: ")
print("---")

card_1 = cards[card_name_1]
card_2 = cards[card_name_2]

print(f"You gave me: {card_names(card_1, card_2)}")
print(f"The total value of these cards is: {total_value(card_1, card_2)}")
