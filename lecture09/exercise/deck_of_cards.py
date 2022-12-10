'''
Sample Code
CS 5001, Fall 2021 - Lecture 9
A deck of cards.
'''
import random
from playing_card import PlayingCard


class DeckOfCards:
    '''
        Class -- DeckOfCards
            Represents a deck of cards.
        Attributes:
            cards -- A list of PlayingCards contained in the deck.
        Methods:
            create_deck -- Helper method. Creates a standard card deck.
            shuffle -- Shuffle the cards.
            num_cards_in_deck -- Gets the number of cards in the deck.
            draw_card -- Removes and returns a card.
            add_card -- Adds a card to the deck.
    '''
    SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
    MIN_VAL = 1  # lowest value of a card i.e. the Ace
    MAX_VAL = 13  # highest value of a card i.e. the King

    def __init__(self):
        '''
            Constructor -- creates a new instance of DeckOfCards
            Parameters:
                self -- the current DeckOfCards object
        '''
        self.create_deck()

    def create_deck(self):
        '''
            Method -- create_deck
                Helper method to populate the deck of cards.
            Parameter:
                self -- The current DeckOfCards object
        '''
        self.cards = []
        for suit in self.SUITS:
            for i in range(self.MIN_VAL, self.MAX_VAL + 1):
                self.cards.append(PlayingCard(i, suit))

    def shuffle(self):
        '''
            Method -- shuffle
                Shuffles the cards in the deck
            Parameter:
                self -- The current DeckOfCards object
        '''
        random.shuffle(self.cards)

    # Exercise 2
    def num_cards_in_deck(self):
        '''
            Method -- num_cards_in_deck
                Gets the number of cards in the deck.
            Parameter:
                self -- The current DeckOfCards object
            Returns:
                The number of cards in the deck.
        '''
        return len(self.cards)
    # Exercise 2

    def draw_card(self):
        '''
            Method -- draw_card
                Removes and returns the last card in the deck. Hint: you will
                need a list method for this one.
            Parameter:
                self -- The current DeckOfCards object
            Returns:
                A PlayingCard object.
        '''
        the_last_card = self.cards[-1]
        self.cards.pop()
        return the_last_card


    # Exercise 2
    def add_card(self, new_card):
        '''
            Method -- add_card
                Adds the given card to the deck.
            Parameter:
                self -- The current DeckOfCards object
                new_card -- A PlayingCard object.
        '''
        self.cards.append(new_card)

    def __str__(self):
        '''
            Method -- __str__
                Returns a string representation of the deck.
            Parameter:
                self -- The current DeckOfCards object
            Returns: 
                A string representation of the deck.
        '''
        return str(self.cards)