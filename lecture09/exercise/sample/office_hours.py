class OfficHours:
    '''
        Class -- OfficeHours
            Represents an office hours session.
        Attributes:
            start_hour -- The hour that the session starts (24-hour clock).
            end_hour -- The hour that the session ends (24-hour clock).
            day -- The day of the week, a string.
            location -- The location of the office hours, a string.
            host -- The name of the person hosting office hours.
        Methods:
            is_happening_at -- Checks if the office hours are taking place at
            a given time on a given day.
    '''
    def __init__(self, start_hour, end_hour, day, location, host):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.day = day
        self.location = location
        self.host = host

    def is_happening_at(self, time, day):
        return day == self.day and time >= self.start_hour and time <= self.end_hour 


def main():
    offhour1 = OfficHours(16, 18, "Tu", "225, Huddle 1", "Mr. T")
    offhour2 = OfficHours(16, 18, "Mon", "225, Huddle 3", "Mr. L")
    
    print("Office Hours available on Tuesday at 5pm: ", offhour1.is_happening_at(17, "Tu"))
    print("Office Hours available on Wednesday at 5pm: ", offhour1.is_happening_at(17, "Wed"))

if __name__ == "__main__":
    main()