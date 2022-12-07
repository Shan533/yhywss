def main():
    height = input("height: ")
    width = input("width: ")
    character = input("character: ")
    return drawing(height, width, character)


def drawing(height, width, character):
    for i in range(int(height)):
        content = []
        if i == 0 or i == int(height) - 1:
            for j in range(int(width)):
                content.append(character)
            test = "".join(content)
            print(test)
        else:
            for j in range(int(width)):
                if j == 0 or j == int(width) - 1:
                    content.append(character)
                else:
                    content.append(" ")
                test = "".join(content)
            print(test)


if __name__ == '__main__':
    main()
