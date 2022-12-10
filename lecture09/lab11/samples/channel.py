'''
Sample Solution - Lab 11
CS 5001, Fall 2021

This module contains a class representing a TV channel.
'''


class Channel:
    '''
        Class -- Channel
            Represents a TV channel.
        Attributes:
            name -- the Channel name
            number -- the Channel number
            shows -- a list of Shows on this channel
        Methods:
            get_shows_by_actor -- Get the shows on this channel that an Actor
            has appeared in.
    '''

    def __init__(self, name, number, shows):
        '''
            Constructor -- Creates a new instance of Channel
            Parameters:
                self -- The current Channel object
                name -- the Channel name
                number -- the Channel number
                shows -- a list of Shows on this channel
        '''
        self.name = name
        self.number = number
        self.shows = shows

    def get_shows_by_actor(self, actor):
        '''
            Method -- get_shows_by_actor
                Gets all the shows on this Channel that a given Actor has
                appeared in.
            Parameters:
                self -- the current Channel object
                actor -- the Actor to search for
            Returns:
                A list of Show objects.
        '''
        ret = []
        for show in self.shows:
            if show.cast_contains(actor):
                ret.append(show)
        return ret
