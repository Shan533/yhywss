'''
user input a binary number, we convert to a decimal number

'''


def main():
    total = 0
    number = input("Number please \n")
    length = len(number)
    for i in range(len(number)):
        if number[i] != "0" and number[i] != "1":
            return print("invalid input")
    for i in range(len(number)):
        if number[i] == "1":
            value = 2 ** (length - i - 1)
            total += value
        elif number[i] == "0":
            total += 0
    print(total)


if __name__ == "__main__":
    main()
