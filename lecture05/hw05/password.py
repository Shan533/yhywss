NUMBER_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOL_LIST = ["@", "!", "#", "$"]
LOWER_LETTER_LIST = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                     "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                     "v", "w", "x", "y", "z"]
UPPER_LETTER_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                     "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                     "V", "W", "X", "Y", "Z"]
ALLOWED_CHARACTERS = NUMBER_LIST + SYMBOL_LIST + LOWER_LETTER_LIST +\
    UPPER_LETTER_LIST


def format_rules(password):
    upper_password = password.upper()
    if upper_password != password:
        check_upper = True
    else:
        check_upper = False

    lower_password = password.lower()
    if lower_password != password:
        check_lower = True
    else:
        check_lower = False

    number_count = 0
    for i in range(len(password)):
        if password[i] in NUMBER_LIST:
            number_count += 1

        if number_count > 0:
            check_number = True
        else:
            check_number = False

    symbol_count = 0
    for i in range(len(password)):
        if password[i] in SYMBOL_LIST:
            symbol_count += 1

        if symbol_count > 0:
            check_symbol = True
        else:
            check_symbol = False

    total = check_lower + check_upper + check_number + check_symbol
    return total


def length_checker(password):
    if len(password) > 12 or len(password) < 9:
        return False
    else:
        return True


def unallowed_character_checker(password):
    for i in range(len(password)):
        if password[i] not in ALLOWED_CHARACTERS:
            return True


def main():

    password = input("input password: \n")
    if length_checker(password):
        if unallowed_character_checker(password):
            print("your password has invalid characters")
        else:
            total = format_rules(password)
            if total >= 3:
                print("good password")
            else:
                print("unallowed characters!")
    else:
        print("password is too short or too long")


if __name__ == '__main__':
    main()
