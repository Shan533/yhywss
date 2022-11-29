def main():

    name_list = ["A", "B", "C", "D"]
    while len(name_list) > 0:
        name = input("give me your name: \n")
        if name in name_list:
            name_list.remove(name)
            print(name, "Welcome to my party!")
        else:
            print("That name is not in the list!")
    print("All guests have arrived!")


if __name__ == '__main__':
    main()
