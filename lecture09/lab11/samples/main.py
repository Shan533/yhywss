'''
Sample Solution - Lab 11
CS 5001, Fall 2021

An example driver.
'''
from actor import *
from show import *
from channel import *


def populate_channels():
    '''
        Function -- populate_channels
            Helper function to create a list of Channels populated with Shows
            and Actors. Only used to tidy up the main function below.
        Returns:
            A list of Channel objects.
    '''
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    channel1 = Channel("DEF", 42, [show1])
    channel2 = Channel("XYZ", 31, [show2, show3])
    return [channel1, channel2]


# PURPOSE
# Get a list of Shows starring a given Actor from a given list of Channels.
# In this implementation, available_channels and shows are both lists but sets
# would be a good alternative.
# SIGNATURE
# shows_starring :: Actor, List<Channel> => List<Show>
def shows_starring(actor, available_channels):
    '''
        Function -- shows_starring
            Get a list of Shows starring a given Actor from a list of Channels.
            In this implementation, available_channels and shows are both lists
            but sets would be a good alternative.
        Parameters:
            actor -- an Actor
            available_channels -- a list of Channels.
        Returns:
            A list of Shows starring the Actor.
    '''
    shows = []
    for channel in available_channels:
        shows += channel.get_shows_by_actor(actor)
    return shows


def main():
    channels = set(populate_channels())
    shows = shows_starring(Actor("Actor", "1"), channels)
    print(shows)
    for show in shows:
        print(show)


if __name__ == "__main__":
    main()
