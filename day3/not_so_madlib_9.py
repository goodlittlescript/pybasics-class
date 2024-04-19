# Same pattern comes up everywhere

# data
cards = {
    "A": {
        "name": "Ace",
        "value": 1,
    },
    "2": {
        "name": "2",
        "value": 2,
    },
    "3": {
        "name": "3",
        "value": 3,
    },
    "4": {
        "name": "4",
        "value": 4,
    },
    "5": {
        "name": "5",
        "value": 5,
    },
    "6": {
        "name": "6",
        "value": 6,
    },
    "7": {
        "name": "7",
        "value": 7,
    },
    "8": {
        "name": "8",
        "value": 8,
    },
    "9": {
        "name": "9",
        "value": 9,
    },
    "10": {
        "name": "10",
        "value": 10,
    },
    "J": {
        "name": "Jack",
        "value": 11,
    },
    "Q": {
        "name": "Queen",
        "value": 12,
    },
    "K": {
        "name": "King",
        "value": 13,
    },
}


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
