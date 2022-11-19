'''
CS5001
Haiyang Yu
compute speed
'''


def main():
    distance = float(input("How many kilometers did you run? \n"))
    hours = int(input("What was your finish time? Enter hours: \n"))
    minutes = int(input("Enter minutes: \n"))

    distance_miles = distance / 1.61
    time_total_minutes = 60 * hours + minutes
    time_total_hours = hours + minutes / 60

    pace_in_mins = time_total_minutes / distance_miles
    pace_in_hours = time_total_hours / distance_miles

    print(str(round(distance_miles, 2)) + " miles\n", str(round(pace_in_mins, 2)) + " pace\n",
    str(round(pace_in_hours, 2)) + " MPH\n")
    print("%s:%s" % (time_total_hours, time_total_minutes))


if __name__ == "__main__":
    main()