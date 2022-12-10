'''
Sample Solution - Lab 11
CS 5001, Fall 2021

This module contains a class representing an actor.
'''


class Actor:
    '''
        Class -- Actor
            Represents an actor.
        Attributes:
            firstname -- the Actor's first name
            lastname -- the Actor's last name
            shows -- a list of Shows the Actor has appeared in.
        Methods:
            appears_in -- Checks if the Actor has appeared in a Show.
    '''

    def __init__(self, firstname, lastname):
        '''
            Constructor -- Creates a new instance of Actor
            Parameters:
                self -- The current Actor object
                firstname -- the Actor's first name
                lastname -- the Actor's last name
        '''
        self.firstname = firstname
        self.lastname = lastname
        # self.shows = []
    '''
    def appears_in(self, show):
        
            Method -- appears_in
                Checks if this Actor appeared in a given Show by searching in
                this Actor's shows list.
            Parameters:
                self -- The current Actor
                show -- A Show object
            Returns:
                True if the current Actor appeared in the given Show, False
                otherwise.
        
        return show in self.shows
    '''
    def __str__(self):
        '''
            Method -- __str__
                Creates a string representation of the Actor
            Parameters:
                self -- The current Actor object
            Returns:
                A string representation of the Actor
        '''
        return "{} {}".format(self.firstname, self.lastname)

    def __eq__(self, other):
        '''
            Method -- __eq__
                Checks if two objects are equal
            Parameters:
                self -- The current Actor object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.firstname == other.firstname and \
            self.lastname == other.lastname
