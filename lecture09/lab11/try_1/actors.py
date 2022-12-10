class Actor:

    def __init__(self, first_name, last_name, shows):
        self.first_name = first_name
        self.last_name = last_name
        self.shows = shows

    def is_starring_at(self, show):
        '''
        输入shows
        输出self是否参演了这个show
        '''

        return show in self.shows

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __eq__(self, other):
        return self.first_name == other or self.last_name == other


def main():
    '''
    hanks = Actor("Tom", "Hanks", ["Modern Family", "White House"])
    jerry = Actor("Ben", "Jerry", ["Modern Family", "Breaking Bad",
    "Mike and Jerry"])
    mike = Actor("Mike", "Erics", ["Mike and Jerry", "Breaking Bad"])
    print(hanks.is_starring_at("Breaking Bad"))
    print(mike.is_starring_at("Breaking Bad"))
    '''


if __name__ == '__main__':
    main()
