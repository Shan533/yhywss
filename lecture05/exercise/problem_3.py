def get_the_list(number, number_list):
    while number != "Q" and number != "q":
        number_list.append(int(number))
        number = input("Enter a number: \n")
    return number_list


def calcalute_negative(number_list, negative):
    for i in number_list:
        if i < 0:
            negative += 1
    return negative


def main():
    '''
    number_list = []
    number = 0
    negative = 0
    number_list = get_the_list(number, number_list)
    negative = calcalute_negative(number_list, negative)
    print("you got", negative, "negative values")


    ----------------------------------------------------------------
    origin_list = []
    new_list = []
    number = 0
    origin_list = get_the_list(number, origin_list)
    origin_list.pop(0)
    # print(origin_list)

    for item in origin_list:
        new_list.append(item + 10)
    print(origin_list)
    print(new_list)
    ----------------------------------------------------------------------------
    origin_list = []
    number = 0
    evens_list = []
    origin_list = get_the_list(number, origin_list)
    origin_list.pop(0)

    for i in origin_list:
        if i % 2 == 0:
            evens_list.append(i)

    print(origin_list)
    print(evens_list)
    ----------------------------------------------------------------------------

    list_a = list(input("give me a list of numbers"))
    print(list_a)
    print(type(list_a[0]))
    ----------------------------------------------------------------------------
    origin_list = []
    number = 0
    value = 0
    origin_list = get_the_list(number, origin_list)
    origin_list.pop(0)

    for i, number in enumerate(origin_list):
        if number == i:
            value += 1
    print(origin_list)
    print(value)
    ----------------------------------------------------------------------------
    '''

    sentence = input("please enter a sentence")
    words = sentence.split(" ")
    words_test = sentence.split("e")
    for word in words:
        print(word)

    print(words)
    print(words_test)


if __name__ == '__main__':
    main()
