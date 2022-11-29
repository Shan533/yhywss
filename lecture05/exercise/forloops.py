'''
Sample Solutions
CS 5001, Fall 2021 - Lecture 5
'''


def main():
    print("Exercise 1: print 0 to 5")
    for i in range(6):
        print(i)

    print("Exercise 1: print 5 to 0")
    for i in range(5, -1, -1):
        print(i)

    print("Exercise 1: print odd numbers from 1 to 11")
    for i in range(1, 12, 2):
        print(i)

    print("Exercise 1: extension 1")
    STRING_1 = "A string"
    for letter in STRING_1:
        print(letter)

    print("Exercise 1: extension 2")
    STRING_2 = "Hello, World!"
    for i in range(1, len(STRING_2), 2):
        print(STRING_2[i])

    print("Exercise 2.1: ")
    for i, letter in enumerate(STRING_2):
        if i % 2 == 1:
            print(letter)

    print("Exercise 2.2: ")
    for i, letter in enumerate("ABC"):
        print(letter * (i + 1))


if __name__ == "__main__":
    main()
