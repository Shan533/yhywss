def length_checker(input_message):
    length = len(input_message)
    if length > 1:
        return True
    else:
        return False

# letter_checker(A, APPLE, _____):
# str = hint[:position] + input_letter + hint[position:]


def letter_checker(input_letter, answer, hint):
    position = 0
    while position < len(answer):
        if input_letter == answer[position]:
            hint = hint[:position] + input_letter + hint[position+1:]
            position += 1
        else:
            position += 1
    return hint


def progress_checker(input_letter, answer):
    position = 0
    progress = ""
    while position < len(answer):
        if input_letter == answer[position]:
            position += 1
            progress = input_letter
        else:
            position += 1
            progress = progress
    return progress


def main():
    answer_1 = "APPLE"
    answer_2 = "OBVIOUS"
    answer_3 = "XYLOPHONE"
    hint_1 = "_____"
    hint_2 = "_______"
    hint_3 = "_________"
    progress_so_far = ""
    guesses = 0
    limitation = 6
    round = 0

    output_1 = games(answer_1, hint_1)
    output_2 = games(answer_2, hint_2)
    output_3 = games(answer_3, hint_3)

    if output_1:
        round += 1
    if output_2:
        round += 1
    if output_3:
        round += 1

    print("“You won", round, "out of 3")


def won_counting(output):
    round = 0
    if output:
        round += 1
    return round


def games(answer, hint):
    guesses = 0
    limitation = 6
    progress_so_far = ""
    round = 0
    while guesses < limitation:
        input_message = input("Enter a letter or word:").upper()
        if length_checker(input_message):
            if input_message == answer:
                print("You win!")
                hint = answer
                guesses = 6
                round += 1
                return True
            else:
                guesses += 0
                print(hint)
                print("Your guesses so far:", progress_so_far)
        else:
            hint = letter_checker(input_message, answer, hint)
            guesses += 1
            progress_so_far = progress_so_far + progress_checker(
                input_message, answer)
            if hint.upper() == answer:
                print("You win!")
                return True
                guesses = 6
                round += 1

            else:
                print(hint)
                print("Your guesses so far:", progress_so_far)
    if hint.upper() != answer:
        print("You lose! The word was", answer)
        return False


if __name__ == '__main__':
    main()


'''
    while guesses < limitation:
        input_message = input("Enter a letter or word:").upper()
        if length_checker(input_message):
            if input_message == answer_1:
                print("You win!")
                guesses = 6
                round += 1

            else:
                guesses += 0
                print(hint_1)
                print("Your guesses so far:", progress_so_far)
        else:
            hint_1 = letter_checker(input_message, answer_1, hint_1)
            guesses += 1
            progress_so_far = progress_so_far + progress_checker(
                input_message, answer_1)
            if hint_1.upper() == answer_1:
                print("You win!")
                guesses = 6
                round += 1

            else:
                print(hint_1)
                print("Your guesses so far:", progress_so_far)
    if hint_1.upper() != answer_1:
        print("You lose! The word was", answer_1)
'''
