'''
workout: M W F Sa or holidays
rest Tu Th and non-holidays

M W F running
Sa or holidays go fo a hike

raining & workout > swim
duration
    running & "temperature > 75" or "temperature < 35"  ---  duration = 30
    else duration = 45

all "else" go into "swimming"

'''


def main():

    day_raw = input("What day is it?\n")
    holidays_raw = input("Is it a holiday?\n")
    raining_raw = input("Is it raining?\n")
    temperature_raw = input("What is the temperature? \n")

    day = day_raw.lower()
    holidays = holidays_raw.lower()
    raining = raining_raw.lower()
    temperature = int(temperature_raw.lower())

    if holidays == "n":
        if day == "tu" or day == "th" or day == "su":
            workout = False
            print("Take a rest day")
        elif day == "m" or day == "w" or day == "f" or day == "sa":
            workout = True
            if raining == "y":
                print("Swim for 45 minutes")
            elif raining == "n":
                if day == "m" or day == "w" or day == "f":
                    if temperature > 75 or temperature < 35:
                        print("Run for 30 minutes")
                    elif temperature < 75 and temperature > 35:
                        print("Run for 45 minutes")
                    else:
                        print("Swim for 35 minutes")
                elif day == "sa":
                    print("Hike for 45 minutes")
                else:
                    print("Swim for 35 minutes")
            else:
                print("Swim for 35 minutes")
        else:
            print("Swim for 35 minutes")
    elif holidays == "y":
        workout = True
        if raining == "n":
            print("Hike for 45 minutes")
        elif raining == "y":
            print("Swim for 45 minutes")
        else:
            print("Swim for 35 minutes")
    else:
        print("Swim for 35 minutes")


if __name__ == '__main__':
    main()
