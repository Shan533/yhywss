def in_list_summing(unit_list):
    if len(unit_list) == 0:
        return 0
    elif len(unit_list) == 1:
        return unit_list[0]
    else:
        total = unit_list[0] + in_list_summing(unit_list[1:])
        return total


def among_list_summing(lists):
    if len(lists) == 0:
        return 0
    elif len(lists) == 1:
        return in_list_summing(lists[0])
    else:
        total = in_list_summing(lists[0]) + among_list_summing(lists[1:])
        return total


def main():
    list_1 = [[1, 2, 3], [10,  20,  30], [100,  200,  300]]
    print(among_list_summing(list_1))


if __name__ == '__main__':
    main()
