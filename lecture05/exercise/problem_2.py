

def word_list(input_word):
    for i, letter in enumerate(input_word):
        if i % 2 == 1:
            print(letter)


def word_multiplied(input_word):
    for i, letter in enumerate("ABC"):
        print(letter * (i + 1))


def main():
    input_word = input("Enter a word \n")
    letter_list = word_list(input_word)
    print(letter_list)
    print(word_multiplied(input_word))


if __name__ == '__main__':
    main()
