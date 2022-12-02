def list_average(number_list):
    total = 0
    '''
    for i in range(len(list_name)):
        total += list_name[i]
    average_score = total / len(list_name)
    print("average score: ", average_score)
    '''
    if len(number_list) > 0:
        for score in number_list:
            total = total + score
        average_score = total / len(number_list)
        print("average score: ", average_score)
    else:
        print("no data")


def get_the_list(number, number_list):
    while number != "Q" and number != "q":
        number_list.append(int(number))
        number = input("Enter a number: \n")
    number_list.pop(0)
    return number_list


def max_and_min_(number_list):
    if len(number_list) > 0:
        max_number = number_list[0]
        min_number = number_list[0]
        for i in range(len(number_list)):
            if number_list[i] > max_number:
                max_number = number_list[i]
            elif number_list[i] < min_number:
                min_number = number_list[i]
                # new_list.pop(i)
        print("Max number: ", max_number)
        print("Min number: ", min_number)
    else:
        print("no data")


def get_median(number_list):
    if len(number_list) > 0:
        number_list.sort()
        new_list = number_list
        if len(number_list) // 2 == 1:
            position = len(new_list) // 2
            median_number = new_list[position]
        else:
            position_1 = int(len(new_list) / 2 - 1)
            position_2 = int(len(new_list) / 2)
            median_number = (new_list[position_1] + new_list[position_2]) / 2
        print("median number is: ", median_number)
    else:
        print("no data")


def main():
    number_list = []
    number = 0
    number_list = get_the_list(number, number_list)
    print(number_list)
    list_average(number_list)
    max_and_min_(number_list)
    get_median(number_list)


if __name__ == '__main__':
    main()

'''
1 2 3 3 4 5

max = 1
min = 1
if 2 > max:
max = 2
elif 2 < min
min = 2
list.pop(0)


'''
