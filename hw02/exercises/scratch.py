def main():
    
    is_moving = input("does it move? \n")
    is_moving = is_moving.lower()

    if is_moving == "yes" or is_moving == "y":
        is_moving = "y"
    elif is_moving == "no" or is_moving == "n":
        is_moving = "n"
    else: 
        print("invalid input \n")
        
    should_moving = input("Should it? \n")
    should_moving = should_moving.lower()

    if should_moving == "yes" or should_moving == "y":
        should_moving = "y"
    elif should_moving == "no" or should_moving == "n":
        should_moving = "n"
    else:
        print("invalid input \n")
        
    exit
        
    if is_moving == should_moving:
        print("No Problem!")
    elif is_moving == "y" and should_moving == "n":
        print("Use duct tape")
        
    else:
        print("Use WD-40")


if __name__ == "__main__":
    main()