'''


'''


def main():

    shape_raw = input("Select a shape \n \
    A: triangle\n \
    B: square\n \
    C: rectangle\n")

    shape = shape_raw.lower()

    if shape == "a":
        width_raw = input("Enter the width:")
        width = float(width_raw)
        if width > 0:
            height_raw = input("Enter the height:")
            height = float(height_raw)
            calculating_factor = 1/2
            if height > 0:
                area = width * height * calculating_factor
                print("The area of the triangle is: " + str(round(area, 2)))
            else:
                print("Invalid height")
        else:
            print("Invalid width")

    elif shape == "b":
        width_raw = input("Enter the width:")
        width = float(width_raw)
        if width > 0:
            area = width ** 2
            print("The area of the square is: " + str(round(area, 2)))
        else:
            print("Invalid width")

    elif shape == "c":
        width_raw = input("Enter the width:")
        width = float(width_raw)
        if width > 0:
            height_raw = input("Enter the height:")
            height = float(height_raw)
            if height > 0:
                area = width * height
                print("The area of the rectangle is: " + str(round(area, 2)))
            else:
                print("Invalid height")
        else:
            print("Invalid width")

    else:
        print("Unknown shape")


if __name__ == '__main__':
    main()
