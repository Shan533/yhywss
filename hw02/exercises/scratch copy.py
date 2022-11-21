def main():

    is_moving = input("does it move? \n")
    is_moving = is_moving.lower()

    if is_moving == "yes" or is_moving == "y":
        is_moving = True
    elif is_moving == "no" or is_moving == "n":
        is_moving = False
    else:
        print("invalid input \n")

    should_moving = input("Should it? \n")
    should_moving = should_moving.lower()

    if should_moving == "yes" or should_moving == "y":
        should_moving = True
    elif should_moving == "no" or should_moving == "n":
        should_moving = False
    else:
        print("invalid input \n")

    if is_moving == should_moving:
        print("No Problem!")
    elif is_moving and not should_moving:
        print("Use duct tape")
    elif should_moving and not is_moving:
        print("Use Wd-40")

    else:
        print("Please restart!\n")


if __name__ == "__main__":
    main()
