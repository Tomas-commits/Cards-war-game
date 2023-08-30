import random

def main():
    deck_of_cards = [{"Ace of Spades": 14}, {"Ace of Hearts": 14}, {"Ace of Diamonds": 14}, {"Ace of Clubs": 14},
                     {"King of Spades": 13}, {"King of Hearts": 13}, {"King of Diamonds": 13}, {"King of Clubs": 13},
                     {"Queen of Spades": 12}, {"Queen of Hearts": 12}, {"Queen of Diamonds": 12},
                     {"Queen of Clubs": 12},
                     {"Jack of Spades": 11}, {"Jack of Hearts": 11}, {"Jack of Diamonds": 11}, {"Jack of Clubs": 11},
                     {"10 of Spades": 10}, {"10 of Hearts": 10}, {"10 of Diamonds": 10}, {"10 of Clubs": 10},
                     {"9 of Spades": 9}, {"9 of Hearts": 9}, {"9 of Diamonds": 9}, {"9 of Clubs": 9},
                     {"8 of Spades": 8}, {"8 of Hearts": 8}, {"8 of Diamonds": 8}, {"8 of Clubs": 8},
                     {"7 of Spades": 7}, {"7 of Hearts": 7}, {"7 of Diamonds": 7}, {"7 of Clubs": 7},
                     {"6 of Spades": 6}, {"6 of Hearts": 6}, {"6 of Diamonds": 6}, {"6 of Clubs": 6},
                     {"5 of Spades": 5}, {"5 of Hearts": 5}, {"5 of Diamonds": 5}, {"5 of Clubs": 5},
                     {"4 of Spades": 4}, {"4 of Hearts": 4}, {"4 of Diamonds": 4}, {"4 of Clubs": 4},
                     {"3 of Spades": 3}, {"3 of Hearts": 3}, {"3 of Diamonds": 3}, {"3 of Clubs": 3},
                     {"2 of Spades": 2}, {"2 of Hearts": 2}, {"2 of Diamonds": 2}, {"2 of Clubs": 2},
                     ]
    player_name = input("Please enter your name: ")
    print("Game starts!")
    shuffle_deck(deck_of_cards)
    print("Cards are splitted and shuffled")
    input("Please enter to reveal cards...")

    print(list(deck_of_cards[0].values())[0])


def shuffle_deck(deck):
    random.shuffle(deck)

def split_decks(deck):
    half_deck = len(deck) / 2
    cnt = 0
    player_deck = []
    computer_deck = []
    for card in deck:
        if cnt == half_deck:
            player_deck.append(card)
        else:
            computer_deck.append(card)
            cnt = + 1
    return player_deck, computer_deck

def card_reveal_duel(player_deck, computer_deck):
    player_card = list(player_deck[0].values())[0]
    computer_card = list(computer_deck[0].values())[0]
    player_deck[0].pop()
    duel_cards = []
    if player_card == computer_card:
        equal()
    elif player_card > computer_card:
        victory(player_card)
    elif player_card < computer_card:






main()
