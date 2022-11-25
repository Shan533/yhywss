'''
CS5001
Shanshan Wu
Fall 2022
an interactive size finder
prompt the user for their chest measurement in inches
then return the user's size according to
three size charts: kids, women, and men.
'''

# 定义了布尔运算的单元，输入值，上限值，下限值。只要在范围内，输出true, 否则输出false
def is_valid_size(chest, min_size, max_size,):
    if chest >= min_size and chest < max_size:
        return True
    return False

# 定义了input-output（主要）功能，输入值chest, 动态的min & max值，输出chest属于哪个size
def get_size(chest, min_size, max_size, step_size):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5
    if not is_valid_size(chest, min_size, max_size):
        return "not avaliable"
    elif is_valid_size(chest, min_size + step_size * S,
                       min_size + step_size * M):
        return "S"
    elif is_valid_size(chest, min_size + step_size * M,
                       min_size + step_size * L):
        return "M"
    elif is_valid_size(chest, min_size + step_size * L,
                       min_size + step_size * XL):
        return "L"
    elif is_valid_size(chest, min_size + step_size * XL,
                       min_size + step_size * XXL):
        return "XL"
    elif is_valid_size(chest, min_size + step_size * XXL,
                       min_size + step_size * XXXL):
        return "XXL"
    return "XXXL"

# 在kids这个列里，上下限是多少，递进step是多少 ，输出
def get_kids_size(chest):
    KIDS_MIN = 26
    KIDS_MAX = 36
    STEP = 2
    return "Kids size: " + get_size(chest, KIDS_MIN, KIDS_MAX, STEP)


# 在women这个列里，上下限是多少，递进step是多少

def get_women_size(chest):
    WOMEN_MIN = 30
    WOMEN_MAX = 42
    STEP = 2
    return "Womens size: " + get_size(chest, WOMEN_MIN, WOMEN_MAX, STEP)


# 在men这个列里，上下限是多少，递进step是多少

def get_men_size(chest):
    MEN_MIN = 34
    MEN_MAX = 53
    STEP = 3
    return "Mens size: " + get_size(chest, MEN_MIN, MEN_MAX, STEP)

#main 第一层先判断了是否数字在总的范围内，如果在总范围内，那么肯定要输出三行的size statement;否则的话，直接output sorry
# 如果数字在总范围内
def main():
    MIN_INCHES = 26
    MAX_INCHES = 52
    chest = float(input("Chest measurement in inches:"))
    if is_valid_size(chest, MIN_INCHES, MAX_INCHES):
        print("Your size choices:")
        print(get_kids_size(chest))
        print(get_women_size(chest))
        print(get_men_size(chest))
    else:
        # when chest measurement is out of range
        print("Sorry, we don't carry your size")


if __name__ == "__main__":
    main()
