
def line(param1, param2):
    output_line = param1 * param2
    return output_line


def larger(param1, param2):
    if param1 > param2:
        return param1
    else:
        return param2


def average(param1, param2, param3):
    params = 3
    sum = param1 + param2 + param3
    average_number = sum / params
    return average_number


def median(param1, param2, param3):
    if param1 >= param2:
        if param3 >= param1:
            median_number = param1
        elif param2 >= param3:
            median_number = param2
        elif param2 <= param3:
            median_number = param3

        # else:
        # median_number = param3
    elif param1 < param2:
        if param3 <= param1:
            median_number = param1
        elif param3 >= param2:
            median_number = param2
        else:
            median_number = param3

    return median_number


def volume_sphere(param):
    # V=(4/3)πr^3。
    PI = 3.14159
    volume = (4/3) * PI * param ** 3
    return volume


def grade(score):
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 60 <= score < 80:
        grade = "C"
    elif score < 60:
        grade = "F"
    else:
        grade = "Invalid Score"

    return grade


def main():

    # print(line("e", 3))
    # print(larger(6, 3))
    # print(average(6, 3, 9))
    # print(median(9, 8, 9))
    # print(volume_sphere(10))
    # print(grade(120))



    


if __name__ == "__main__":
    main()
