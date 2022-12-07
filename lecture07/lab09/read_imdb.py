def label_devider(file_content):
    bad_labels = []
    good_labels = []
    other_labels = []
    for reviews in file_content:
        reviews_splitted = reviews.split("\t")
        try:
            if reviews_splitted[1].strip() == "0":
                bad_labels.append(reviews)
            elif reviews_splitted[1].strip() == "1":
                good_labels.append(reviews)
            else:
                raise ValueError("Error processing the file1.")
        except ValueError:
            print("Error processing the file2.")
    devided_labels_lists = [bad_labels, good_labels, other_labels]
    return devided_labels_lists


def name_validation(file_name):
    validation = False
    while not validation:
        try:
            file_path = "lecture07/lab09/" + file_name.strip() + ".txt"
            with open(file_path, 'r') as file:
                file_content = file.readlines()
                validation = True
        except FileNotFoundError:
            print("File not found")
            file_name = input("Enter the path to the IMDB dataset: \n")
    return file_content


def main():
    file_name = input("Enter the path to the IMDB dataset: \n")
    file_content = name_validation(file_name)
    devided_labels_lists = label_devider(file_content)

    goodname_validation = False
    while not goodname_validation:
        try:
            good_labels_name = input("Enter the path to store \
                                     the good labels: \n")
            if good_labels_name.strip() == '':
                raise ValueError("Invalid file name. Please try again.")
            else:
                # try:
                good_labels_path = "lecture07/lab09/" + \
                                   good_labels_name.lower().strip() + ".txt"
                good_labels_file = open(good_labels_path, 'w')
                good_labels = devided_labels_lists[0]
                for lines in good_labels:
                    good_labels_file.write(lines)
                # good_labels_file.write(devided_labels_lists[0])
                goodname_validation = True
                good_labels_file.close()
                # except FileExistsError:
                #    print("this file already exists")
        except ValueError:
            print("Invalid file name. Please try again.")

        bad_validation = False
        while not bad_validation:
            bad_labels_name = input("Enter the path to store \
                                    the bad labels: \n")
            if bad_labels_name.strip() == '':
                raise ValueError("Invalid file name. Please try again.")
            else:
                # try:
                bad_labels_path = "lecture07/lab09/" + \
                                  bad_labels_name.lower().strip() + ".txt"
                bad_labels_file = open(bad_labels_path, 'w')
                bad_labels = devided_labels_lists[1]
                for lines in bad_labels:
                    bad_labels_file.write(lines)
                # bad_labels_file.write(devided_labels_lists[1])
                bad_validation = True
                bad_labels_file.close()
                # except FileExistsError:
                #   print("this file already exists")


if __name__ == '__main__':
    main()
