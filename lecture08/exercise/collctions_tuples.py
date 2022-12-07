'''
Sample Code
CS 5001, Fall 2021, Lecture 8
This sample code shows how to work with Python tuples.
'''


def main():
    print("Working with tuples")
    # Tuple - ordered, immutable. Created using parentheses, ()
    my_tuple = ("ABC", "DEF", "GHI")

    # Access an item using its index, just like a list.
    print(my_tuple[1])

    # Concatenate tuples using +, just like lists
    new_tuple = my_tuple[:2] + ("JKL", "MNO")
    print(new_tuple)

    # TODO: Retrieve the item "GHI" from my_tuple and print it
    print(my_tuple[-1])


if __name__ == "__main__":
    main()
