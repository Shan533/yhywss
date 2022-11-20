def main():

    answer_1 = input("When planning a trip, you... \n \
                     A: Find the hot parties. \n \
                     B: Sorts out all the logistics \n \
                     C: Lets everyone else take charge \n")
    answer_2 = input("What are you most afraid of? \n \
                     A: Not being accepted \n \
                     B: Losing someone close to me \n \
                     C: Looking stupid in front of others \n")
    answer_3 = input("What was your favorite toy as a kid? \n \
                     A: She-Ra \n \
                     B: He-Man \n \
                     C: Video games \n")

    answer_1_lowercase = answer_1.lower()
    answer_2_lowercase = answer_2.lower()
    answer_3_lowercase = answer_3.lower()

    if answer_1_lowercase == "a" \
       and answer_2_lowercase == "a" \
       and answer_3_lowercase == "a":

        print("We calculate your character as Ginny")

    elif answer_1_lowercase == "a" \
            and answer_2_lowercase == "a" \
            and answer_3_lowercase == "b":

        print("We calculate your character as Draco")

    elif answer_1_lowercase == "a" \
            and answer_2_lowercase == "a" \
            and answer_3_lowercase == "c":

        print("We calculate your character as Sirius")

    elif answer_1_lowercase == "a" \
            and answer_2_lowercase == "b":

        print("We calculate your character as Dobby")

    elif answer_1_lowercase == "a" \
            and answer_2_lowercase == "c":

        print("We calculate your character as Voldemort")

    elif answer_1_lowercase == "b":

        print("We calculate your character as Hermione")

    elif answer_1_lowercase == "c" \
        and answer_2_lowercase == "a" \
            and answer_3_lowercase == "a":

        print("We calculate your character as Luna")

    elif answer_1_lowercase == "c" \
        and answer_2_lowercase == "a" \
            and answer_3_lowercase == "b":

        print("We calculate your character as Hagrid")
    elif answer_1_lowercase == "c" \
        and answer_2_lowercase == "a" \
            and answer_3_lowercase == "c":

        print("We calculate your character as Ron")

    elif answer_1_lowercase == "c" \
            and answer_2_lowercase == "b":

        print("We calculate your character as Tonks")

    elif answer_1_lowercase == "c" \
            and answer_2_lowercase == "c":

        print("We calculate your character as Slughorn")


if __name__ == '__main__':
    main()
