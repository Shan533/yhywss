def is_palindrome(word):
    word_trimmed = word.lower().replace(" ", "")
    if len(word) > 1:
        if word_trimmed == reverse(word):
            return True
        return False
    return False


def reverse(word):
    word_trimmed_reversed = word[::-1].lower().replace(" ", "")
    return word_trimmed_reversed


def main():
    word = input("give me a word \n")
    print(is_palindrome(word))


if __name__ == '__main__':
    main()
