VOWELS = ("A", "E", "I", "O", "U")


def whether_have_vowels(vocabulary):
    for i in range(len(vocabulary)):
        if vocabulary[i].upper() in VOWELS:
            return True
    return False


def check_every_vocab(list_name):
    if len(list_name) == 0:
        return 0
    elif len(list_name) == 1:
        return whether_have_vowels(list_name[0])
    else:
        return whether_have_vowels(list_name[0]) + \
               check_every_vocab(list_name[1:])


def main():
    list_name = ["laji", "412", "21412"]
    if check_every_vocab(list_name) != len(list_name):
        print("bad")
    elif check_every_vocab(list_name) == len(list_name):
        if len(list_name) == 0:
            print("You have no vocabulary")
        else:
            print("good")


if __name__ == "__main__":
    main()
