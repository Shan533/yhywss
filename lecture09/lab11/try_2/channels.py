class Channel:
    def __init__(self, name, time, shows):
        self.name = name
        self.time = time
        self.shows = shows

    def shows_have_actor(self, actor):
        filtered_shows = []
        for show in self.shows:
            if show.whether_actor_in_show(actor):
                filtered_shows.append(show)
        return filtered_shows
