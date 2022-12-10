'''
Sample Code
CS 5001, Fall 2021 - Lecture 9
Representing office hours using a dictionary.
'''


def is_happening_at(session, time, day):
    '''
        Function -- is_happening_at
            Checks if an office hours session is happening at the given time
            on the given day.
        Parameters:
            session -- A dictionary containing office hours information.
            time -- The hour of the day (24 hour clock), an integer.
            day -- The day of the week.
        Returns:
            True if the office hours session will be happening at the specified
            time and day, False otherwise.
    '''
    return day == session["day"] and time >= session["start"] \
        and time <= session["end"]


def main():
    office_hours = {
        "day": "Tu",
        "start": 16,
        "end": 18,
        "location": "225, Huddle 1",
        "host": "Mr. T"
    }

    user_day = input("What day would you like to attend office hours? ")
    user_time = int(
        input("What time would you like to attend? (24-hour clock) "))
    while not is_happening_at(office_hours, user_time, user_day):
        print("No office hours at that time!")
        user_day = input("Enter a day:\n")
        user_time = int(input("Enter an hour:"))
    print("Office hours available!")


if __name__ == "__main__":
    main()
