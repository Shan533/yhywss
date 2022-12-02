def recursive_multiplication(number, times):
    if number == 0 or number == 1:
        return number
    elif times == 1:
        return number
    elif times == 0:
        return 1
    else:
        return number + recursive_multiplication(number, times - 1)


def main():
    number = int(input("Enter a number"))
    times = int(input("Enter times"))
    output = recursive_multiplication(number, times)
    print(number, "*", times, "=", output)


if __name__ == '__main__':
    main()
