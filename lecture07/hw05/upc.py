'''
input a str,
operate the string from right to left

when at even position, leave as they are
when at odd position, number * 3

'''


def calculating(upc_code):
    temp_upc = upc_code[::-1]
    total = 0
    for i in range(len(temp_upc)):
        if i % 2 == 0:
            total += int(temp_upc[i])
        else:
            total += 3 * int(temp_upc[i])
    return total


def determining(total):
    if total % 10 == 0:
        return True
    else:
        return False


def main():
    upc_code = input("give me a UPC code: \n")
    if determining(calculating(upc_code)):
        print("valid")
    else:
        print("invalid")


if __name__ == '__main__':
    main()
