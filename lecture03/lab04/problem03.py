
'''
1.计算function
2.大小写
3.M Tu w th f sa su
'''


def record_day(current_day_raw):
    current_day = current_day_raw.lower()
    return current_day


def calculate_days(current_day):
    if current_day == "m":
        remaining_days = 4
    elif current_day == "tu":
        remaining_days = 3
    elif current_day == "w":
        remaining_days = 2
    elif current_day == "th":
        remaining_days = 1
    elif current_day == "f":
        remaining_days = 0
    elif current_day == "sa":
        remaining_days = 6
    elif current_day == "su":
        remaining_days = 5

    return remaining_days


def main():

    username = input("Please enter your name")
    print("Hello", username, "\n")
    current_day = record_day(input("Current day?"))
    remaining_days = calculate_days(current_day)

    print("you have", remaining_days, "days until Friday")


if __name__ == "__main__":
    main()
