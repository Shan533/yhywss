'''
Sample Code
CS 5001, Fall 2021 - Lecture 9
A playing card class.
'''


class PlayingCard:
    '''
        Class -- PlayingCard
            Represents a playing card.
        Attributes:
            value -- the card's value, an integer.
            suit -- the card's suit, a string
    '''
    name = None

    def __init__(self, value, suit):
        '''
            Constructor -- creates a new instance of PlayingCard
            Parameters:
                self -- the current PlayingCard object
                value -- the card's value, an integer
                suit -- the card's suit, a string
        '''
        self.value = value
        self.suit = suit
        self.set_name()

    def set_name(self):
        '''
            Method -- set_name
                Helper method to set the name of special cards.
            Parameter:
                self -- The current PlayingCard object
            Returns:
                Nothing. Sets the attribute if applicable.
        '''
        NAMES = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        if self.value in NAMES:
            self.name = NAMES[self.value]

    def __str__(self):
        '''
            Method -- __str__
                Creates a string representation of the PlayingCard
            Parameter:
                self -- The current PlayingCard object
            Returns:
                A string representation of the PlayingCard.
        '''
        return "{} of {}".format(self.value, self.suit)

    def __eq__(self, other):
        '''
            Method -- __eq__
                Checks if two objects are equal
            Parameters:
                self -- The current PlayingCard object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.value == other.value and self.suit == other.suit


def main():
    two_of_spades = PlayingCard(2, "spades")
    queen_of_hearts = PlayingCard(12, "hearts")
    three_of_clubs = PlayingCard(3, "clubs")
    print(two_of_spades.name)
    print(str(two_of_spades))


if __name__ == "__main__":
    main()
