def main():
    file_path = "lecture07/lab09/imdb_labelled.txt"
    with open(file_path, "r") as file:
        contents = file.readlines()
        print(contents[0])

if __name__ == '__main__':
    main()