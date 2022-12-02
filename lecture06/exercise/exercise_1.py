def recursive_factorial(number):
    if int(number) == 0:
        return 1
    elif int(number) == 1 or int(number) == 2:
        return number
    else:
        return int(number) * recursive_factorial(int(number) - 1)


def main():
    print("Welcome to the recursive factorial function calculator!")
    print("Enter a number to calculate the recursive factorial of")
    number = input("Enter a number")
    print(number, "! = ", recursive_factorial(number))


if __name__ == '__main__':
    main()
