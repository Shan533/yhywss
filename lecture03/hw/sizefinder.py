'''
1. input the size number in inches
2. output the size

'''


def main():
    chest_size_raw = input("Chest measurement in inches:")
    chest_size = converter(chest_size_raw)

    size_kids = size_calculator_kid(chest_size)
    size_womens = size_calculator_womens(chest_size)
    size_mens = size_calculator_mens(chest_size)

    print("Your size choices: \n"
          "Kids size:", size_kids, "\n"
          "Womens size:", size_womens, "\n"
          "Mens size:", size_mens)


def converter(raw_input):
    converted_output = float(raw_input)
    return converted_output



def size_calculator(chest_size_raw):

    if 26 <= chest_size_raw < 28:
        size_kids = "S"
        size_womens = "Not available"
        size_mens = "Not available"
    return size_kids, size_womens, size_mens


def size_calculator_kid(chest_size_raw):

    if 26 <= chest_size_raw < 28:
        size_kids = "S"
    elif 28 <= chest_size_raw < 30:
        size_kids = "M"
    elif 30 <= chest_size_raw < 32:
        size_kids = "L"
    elif 32 <= chest_size_raw < 34:
        size_kids = "M"
        
    return size_kids


def size_calculator_womens(chest_size_raw):

    if 26 <= chest_size_raw < 28:
        size_womens = "Not available”"
    return size_womens


def size_calculator_mens(chest_size_raw):

    if 26 <= chest_size_raw < 28:
        size_mens = "Not available”"
    return size_mens


if __name__ == '__main__':
    main()
