'''
1. input the message
2. give some flexibility to the input
3. X101 X102 just print the message"You have successfully registered for
<course number>"
4. if they want to register B classes, they need earned A/B in 101 and A/B/C
in 102. They should input their grades manually. (upper or lower)
'''


def main():
    course_input = input("Enter a course number")
    course_number = course_input.lower()

    if course_number == "x101" or course_number == "x 101":
        print("You have successfully registered for X101")

    elif course_number == "x102" or course_number == "x 102":
        print("You have successfully registered for X102")

    elif course_number == "b500" or course_number == "b 500":
        grade_x101 = input("What grade did you get for X101?")
        grade_x101_lower = grade_x101.lower()
        grade_x102 = input("What grade did you get for X102?")
        grade_x102_lower = grade_x102.lower()

        if grade_x101_lower == "a" or grade_x101_lower == "b":
            if grade_x102_lower == "a" or grade_x102_lower == "b" or \
                    grade_x102_lower == "c":
                print("You meet all the prerequisites and have successfully \
                    registered for B500")
            elif grade_x102_lower == "d" or grade_x102_lower == "f":
                print("You do not meet the prerequisites for B500")
            else:
                print("Invalid anwser")
        elif grade_x101_lower == "c" or grade_x101_lower == "d" \
                or grade_x101_lower == "f":
            print("You do not meet the prerequisites for B500")
        else:
            print("Invalid anwser")

    elif course_number == "b525" or course_number == "b 525":
        grade_x101 = input("What grade did you get for X101?")
        grade_x101_lower = grade_x101.lower()
        grade_x102 = input("What grade did you get for X102?")
        grade_x102_lower = grade_x102.lower()
        if grade_x101_lower == "a" or grade_x101_lower == "b":
            if grade_x102_lower == "a" or grade_x102_lower == "b" \
               or grade_x102_lower == "c":
                print("You meet all the prerequisites and have successfully \
                      registered for B525")
            elif grade_x102_lower == "d" or grade_x102_lower == "f":
                print("You do not meet the prerequisites for B525")
            else:
                print("Invalid anwser")
        elif grade_x101_lower == "c" or grade_x101_lower == "d" \
                or grade_x101_lower == "f":
            print("You do not meet the prerequisites for B525")
        else:
            print("Invalid anwser")

    elif course_number == "b701" or course_number == "b 701":
        grade_x101 = input("What grade did you get for X101?")
        grade_x101_lower = grade_x101.lower()
        grade_x102 = input("What grade did you get for X102?")
        grade_x102_lower = grade_x102.lower()

        if grade_x101_lower == "a" or grade_x101_lower == "b":
            if grade_x102_lower == "a" or grade_x102_lower == "b" \
               or grade_x102_lower == "c":
                print("You meet all the prerequisites and have successfully \
                      registered for B701")
            elif grade_x102_lower == "d" or grade_x102_lower == "f":
                print("You do not meet the prerequisites for B701")
            else:
                print("Invalid Anwser")

        elif grade_x101_lower == "c" or grade_x101_lower == "d" or \
                grade_x101_lower == "f":
            print("You do not meet the prerequisites for B701")

        else:
            print("Invalid anwser")

    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()
