'''
Sample Code
CS 5001, Fall 2021 - Lecture 9, Exercise 2
Task 1: implement the missing methods in deck_of_cards.py (docstrings provided)
Task 2: implement the following "magic" trick in main(). You will need to
import the DeckOfCards class.
- Create a deck of cards and shuffle it.
- Prompt the user to press any key to draw a card from the deck. You will need
to save their choice.
- Print their card.
- Return the card to the deck and shuffle it.
- Repeat the following steps until the original card is found: prompt the user
to press any key to draw a card. Provide feedback e.g. You drew... There are
N cards remaining.
'''
from deck_of_cards import DeckOfCards

def main():
    # Create a deck of cards and shuffle it.
    deck = DeckOfCards()
    deck.shuffle()

    # Prompt the user to press any key to draw a card from the deck. You will need
    # to save their choice.
    input("Press any key to draw a card")
    card = deck.draw_card()

    # Print their card.
    print("You drew: " + str(card))

    # Return the card to the deck and shuffle it.
    deck.add_card(card)
    deck.shuffle()

    # Repeat the following steps until the original card is found: prompt the user
    # to press any key to draw a card. Provide feedback e.g. You drew... There are
    # N cards remaining.
    card_found = False
    while not card_found and deck.num_cards_in_deck() > 0:
        input("Press any key to draw a card")
        new_card = deck.draw_card()
        print("You drew: " + str(new_card))
        if card == new_card:
            card_found = True
            print("Ta da!")
        else:
            print("Sorry...try again. " + str(deck.num_cards_in_deck) + " remaining")


if __name__ == "__main__":
    main()

