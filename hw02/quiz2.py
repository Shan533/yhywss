def main():

    origin = int(input("please enter a integer"))
    determine_number = int(input("determine integer"))

    remainder = origin % determine_number

    if remainder == 0 and origin >= 0:
        print(-origin)

    elif origin < 0 and remainder != 0:
        print(origin**2)

    else:
        print(origin)



if __name__ == '__main__':
    main()
