'''
用户input一个值chest
chest 落入到一个number pool里
不能直接hard code pool的min & max
三个池子的min & max 不一样

'''


def converter(raw_input):
    converted_output = float(raw_input)
    return converted_output


def is_valid_size(chest, min_size, max_size):
    if min_size <= chest < max_size:
        return True
    else:
        return False


def get_size_kids(chest):
    MIN_SIZE = 26
    MAX_SIZE = 36
    STEP = 2
    size_kids = size_calculator(chest, MIN_SIZE, MAX_SIZE, STEP)
    return size_kids


def get_size_womens(chest):
    MIN_SIZE = 30
    MAX_SIZE = 42
    STEP = 2
    size_womens = size_calculator(chest, MIN_SIZE, MAX_SIZE, STEP)
    return size_womens


def get_size_mens(chest):
    MIN_SIZE = 34
    MAX_SIZE = 52
    STEP = 3
    size_mens = size_calculator(chest, MIN_SIZE, MAX_SIZE, STEP)
    return size_mens


def size_calculator(chest, min_size, max_size, STEP):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5
    XXXXL = 6

    if not is_valid_size(chest, min_size, max_size):
        return "Not available"
    elif is_valid_size(chest, min_size + (S * STEP), min_size + (M * STEP)):
        size = "S"
        return size
    elif is_valid_size(chest, min_size + (M * STEP), min_size + (L * STEP)):
        size = "M"
        return size
    elif is_valid_size(chest, min_size + (L * STEP), min_size + (XL * STEP)):
        size = "L"
        return size

    elif is_valid_size(chest, min_size + (XL * STEP), min_size + (XXL * STEP)):
        size = "XL"
        return size

    elif is_valid_size(chest, min_size + (XXL * STEP), min_size +
                       (XXXL * STEP)):
        size = "XXL"
        return size

    elif is_valid_size(chest, min_size + (XXXL * STEP), min_size + (XXXXL *
                       STEP)):
        size = "XXXL"
        return size


def main():
    # 将输入转化成数字了，数字记录为chest_size
    chest_size_raw = input("Chest measurement in inches:")
    chest_size = converter(chest_size_raw)
    MAX = 52
    MIN = 26
    if is_valid_size(chest_size, MIN, MAX):
        print("Your size choices: \n"
              "Kids size:", get_size_kids(chest_size), "\n"
              "Womens size:", get_size_womens(chest_size), "\n"
              "Mens size:", get_size_mens(chest_size))
    else:
        print("Sorry, we don't carry your size")


if __name__ == '__main__':
    main()
