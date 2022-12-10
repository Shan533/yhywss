from actors import *
from shows import *
from channels import *


def objects_dictionary():
    actor1 = Actor("Mike", "Lee")
    actor2 = Actor("Lebron", "James")
    actor3 = Actor("Ben", "Jerry")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    channel1 = Channel("DEF", 42, [show1])
    channel2 = Channel("XYZ", 31, [show2, show3])
    return [channel1, channel2]


def all_shows_have_actor(actor, channels):
    all_filtered = []
    for channel in channels:
        all_filtered += channel.shows_have_actor(actor)
    return all_filtered


def main():
    channels = objects_dictionary()
    all_filtered = all_shows_have_actor(Actor("Lebron", "James"), channels)

    '''
    for channel in channels:
        all_filtered += channel.shows_have_actor(Actor("Mike", "Lee"))
        # all_filtered.append(channel.shows_have_actor(Actor("Mike", "Lee")))
    '''
    for show in all_filtered:
        print(show)


if __name__ == "__main__":
    main()
