'''
Sample Solution
CS 5001, Fall 2021, Lab 9

A module for processing and viewing the IMDB sentiment analysis dataset.
'''


SUCCESS = 0
NOT_FOUND = 1
WRONG_FORMAT = 2


def read_file(filename, pos, neg):
    '''
        Function -- read_file
            Reads the IMDB data. Returns an integer representing the outcome of
            the file read.
        Parameters:
            filename -- A string file path
            pos -- The positive reviews as a list of strings
            neg -- The negative reviews as a list of strings
        Returns:
            An integer representing the outcome of the file read.
    '''
    try:
        with open(filename, "r") as file:
            for line in file:
                processed = process_line(line)
                if processed[-1] == 0:
                    neg.append(processed[0])
                else:
                    pos.append(processed[0])
            return SUCCESS
    except FileNotFoundError:
        return NOT_FOUND
    except ValueError:
        return WRONG_FORMAT


def process_line(line):
    '''
        Function -- process_line
            Helper function to process a line in the IMDB file. Assumes
            ValueErrors will be caught by the calling function.
        Parameter:
            line -- A string to process.
        Returns:
            A string split into a list with extra spaces removed and the label
            converted to a number.
    '''
    parts = line.split("\t")
    for i, part in enumerate(parts):
        parts[i] = part.strip()
    parts[-1] = int(parts[-1])
    return parts


def write_file(reviews, filename):
    '''
        Function -- write_file
            Write reviews to a file.
        Parameters:
            reviews -- A list of strings. Each string is a line in the file.
        Returns:
            None. This function does not return.
    '''
    with open(filename, "w") as file:
        for review in reviews:
            file.write(review + "\n")


def process_display(user_in, pos, neg):
    '''
        Function -- process_display
            Processes the user's display request.
        Parameters:
            user_in -- The string entered by the user
            pos -- The list of positive reviews
            neg -- The list of negative reviews
        Returns:
            The requested review if the input is valid, or an error message if
            the input is invalid.
    '''
    QUIT = "q"
    POS = "p"
    NEG = "n"
    if user_in == QUIT:
        return "Quitting..."
    else:
        parts = user_in.split(" ")
        try:
            if parts[0] == POS:
                return pos[int(parts[1])]
            elif parts[0] == NEG:
                return neg[int(parts[1])]
            else:
                return "Command must start with either 'p' or 'n'"
        except ValueError:
            return "Review number must be a valid integer"
        except IndexError:
            return "Review number must be between 0 and " + str(len(pos) - 1)


def main():
    FILE_PROMPT = "Enter the path to the IMDB dataset:\n"

    imdb_path = input(FILE_PROMPT)
    positive = []
    negative = []

    valid_file = False
    while not valid_file:
        outcome = read_file(imdb_path, positive, negative)
        if outcome == SUCCESS:
            valid_file = True
        else:
            if outcome == NOT_FOUND:
                print("File not found!")
            elif outcome == WRONG_FORMAT:
                print("Wrong format. Did you enter the correct filepath?")
            imdb_path = input(FILE_PROMPT)

    write_file(positive, "positive.txt")
    write_file(negative, "negative.txt")

    user_in = ""
    while user_in != "q":
        print("Select a review using the following commands:")
        print("p review_index: selects the positive review at the given index")
        print("n review_index: selects the negative review at the given index")
        user_in = input("Enter your choice:")
        print(process_display(user_in, positive, negative))


if __name__ == "__main__":
    main()
