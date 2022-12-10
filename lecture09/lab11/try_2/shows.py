class Show:
    def __init__(self, title, casts):
        self.title = title
        self.casts = casts

    def whether_actor_in_show(self, actor):
        return actor in self.casts

    def __str__(self):
        return self.title
