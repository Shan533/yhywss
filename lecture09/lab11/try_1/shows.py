from actors import Actor
CASTS = ["Tom Hanks", "Ben Jerry", "Mike Erics"]
SHOWS = [["Modern Family", "White House"], ["Modern Family", "Breaking Bad", "Mike and Jerry"], ["Mike and Jerry", "Breaking Bad"]]


class Show:
    def __init__(self, title):
        self.title = title
        self.get_casts()

    def get_casts(self):
        '''
        输入电视剧
        输出参演电视剧的所有卡司
        '''
        self.casts = []
        for i in range(len(SHOWS)):
            if self.title in SHOWS[i]:
                self.casts.append(CASTS[i])
        return self.casts


def main():
    modern_family = Show("Modern Family")
    white_house = Show("White House")
    breaking_bad = Show("Breaking Bad")
    mike_and_jerry = Show("Mike and Jerry")
    print(modern_family.casts)
    print(breaking_bad.casts)
    print(modern_family.get_casts())


if __name__ == '__main__':
    main()
