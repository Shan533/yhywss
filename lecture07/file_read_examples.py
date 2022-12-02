'''
Sample Code
CS 5001, Fall 2020, Lecture 7

This module shows different ways to read a file.
'''


def read_whole_file(file_path):
    '''
        Function -- read_whole_file
            Reads an entire file in one go.
        Parameter:
            file_path -- the path of the file
        Returns:
            The contents of the file (a string)
    '''
    file = open(file_path, "r")
    file_contents = file.read()
    file.close()
    return file_contents


def file_as_list(file_path):
    '''
        Function -- file_as_list
            Reads a file as a list of lines
        Parameter:
            file_path -- the path of the file
        Returns:
            The contents of the file (a list of strings)
    '''
    file = open(file_path, "r")
    file_contents = file.readlines()
    file.close()
    return file_contents


def line_by_line(file_path):
    '''
        Function -- line_by_line
            Reads a file one line at a time.
        Parameter:
            file_path -- the path of the file
        Returns:
            The contents of the file (a list of strings)
    '''
    lines = []
    file = open(file_path, "r")
    line = file.readline()
    lines.append(line)
    while line:
        line = file.readline()
        lines.append(line)
    file.close()
    return lines


def line_by_line_neater(file_path):
    '''
        Function -- line_by_line_neater
            Reads a file one line at a time using some Python magic.
        Parameter:
            file_path -- the path of the file
        Returns:
            The contents of the file (a list of strings)
    '''
    lines = []
    file = open(file_path, "r")
    for line in file:
        lines.append(line)
    file.close()
    return lines
    

def best_practice(file_path):
    '''
        Function -- best_practice
            Reads a file one line at a time using "with". This is best practice
            because it automatically closes the file.
        Parameter:
            file_path -- the path of the file
        Returns:
            The contents of the file (a list of strings)
    '''
    lines = []
    # Opens the file and assigns it to the variable called file
    try:
        with open(file_path, "r") as file:
            # The following is the line by line option but the others work too
            for line in file:
                lines.append(line)
    except FileNotFoundError:
        print("File not found")
    # The file is automatically closed when using "with"
    return lines


def main():
    path = "order.txt"
    # print(read_whole_file(path))
    # print(file_as_list(path))
    # print(line_by_line(path))
    # print(line_by_line_neater(path))
    print(best_practice(path))


if __name__ == "__main__":
    main()