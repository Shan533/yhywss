DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")
LOCATIONS = ["A", "B", "C"]
HOSTS = ["Aike", "Bob", "Cylan"]


class OfficeHours:
    '''
    Class -- OfficeHours
        Represents the available office hours
    Attributes:
        time -- A range of time on the available day.
    Methods:
        is_happening_at -- returns whether the office hours happen at the given time.
    
    
    '''
    # DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")
    # LOCATIONS = ["A", "B", "C"]
    # HOSTS = ["Aike", "Bob", "Cylan"]
    
    host = None
    day = None
    
    def __init__(self, start_hour, end_hour, day, location):
        self.start = start_hour
        self.end = end_hour
        self.day = day
        self.location = location
        self.set_host()

    def set_host(self):
        # LOCATIONS = ["A", "B", "C"]
        # HOSTS = ["Aike", "Bob", "Cylan"]
        for i in range(len(LOCATIONS)):
            if self.location == LOCATIONS[i]:
                self.host = HOSTS[i]

    def is_happening_at(self, time, day):
        if day == self.day:
            if self.start <= time <= self.end:
                return True
        else:
            return False


def main():
    mon_aike = OfficeHours(9, 12, "Mon", "Aike")
    tue_bob = OfficeHours(13, 16, "Tue", "Bob")
    wed_cylan = OfficeHours(11, 15, "Wed", "Cylan")
    
    
    output = tue_bob.is_happening_at(13, "Wed")
    print(output)

if __name__ == "__main__":
    main()