'''
Sample Solution - Lab 11
CS 5001, Fall 2021

This module contains a class representing a TV show.
'''


class Show:
    '''
        Class -- Show
            Represents a TV show.
        Attributes:
            title -- the show's title
            cast -- a list of actors appearing in the show
        Methods:
            cast_contains -- Checks if a particular Actor has been in the show.
    '''

    def __init__(self, title, cast):
        '''
            Constructor -- Creates a new instance of Show
            Parameters:
                self -- The current Show object
                title -- the show's title
                cast -- a list of actors appearing in the show
        '''
        self.title = title
        self.cast = cast
    
    def cast_contains(self, actor):
        '''
            Method -- cast_contains
                Checks if a given Actor is in this Show's cast.
            Parameters:
                self -- the current Show object.
                actor -- the Actor to search for.
            Returns:
                True if the Actor is in the cast, False otherwise.
        '''
        return actor in self.cast
    


    def __str__(self):
        '''
            Method -- __str__
                Creates a string representation of the Show
            Parameters:
                self -- The current Show object
            Returns:
                A string representation of the Show.
        '''

        return self.title

