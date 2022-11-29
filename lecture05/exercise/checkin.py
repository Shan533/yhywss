'''
Sample Solution
CS 5001, Fall 2021 - Lecture 5, exercise 3

Given a list of guests:
- Use a while loop in main() to prompt the user to enter guest names as they
arrive.
- When a guest arrives, check that they are on the list.
- If they are, remove them from the list.
Print a message to the console when all guests have arrived.
'''


def main():
    expected_guests = ["Darth Vader", "Princess Leia",  "Luke Skywalker"]
    while len(expected_guests) > 0:
        name = input("Enter the name of the guest: ")
        if name in expected_guests:
            position = expected_guests.index(name)
            expected_guests.pop(position)
            print(name, "is checked in")
        else:
            print(name, "is not on the list")
    print("All guests have arrived!")


if __name__ == "__main__":
    main()
