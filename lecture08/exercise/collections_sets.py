'''
Sample Code
CS 5001, Fall 2021, Lecture 8
This sample code shows how to work with Python sets.
'''


def main():
    print("Working with sets")
    # Sets - Unordered, mutable. Created using {} or set()
    avengers = {"Captain America", "Iron Man", "Hulk", "Thor", "Black Widow"}
    thor_family = {"Thor", "Loki", "Odin"}

    # Access items by iterating or searching
    for character in avengers:
        print(character, "is an Avenger")

    # Add items to a set using .add()
    # TODO: Add "Black Panther" and "Captain Marvel" to the avengers
    avengers.add("Black Panther")
    avengers.add("Captain Marvel")
    print(avengers)

    # Perform operations on multiple sets e.g. union, intersection, difference
    # TODO: Use a set method to find the members of thor_family that are also
    #       in avengers. Should just be Thor.
    print(thor_family.intersection(avengers))
    print(thor_family.union(avengers))
    print(thor_family.difference(avengers))

    # TODO: Use a set method to find the members of avengers that are NOT in
    #       thor_family. Should be everyone except Thor.
    print(thor_family ^ avengers)  # provides the disjoint sets, not quite
    # what we were aiming for
    print(avengers.difference(thor_family))  # here's the one

    # set1.difference(set2) set1中，不属于set2的
    # set2.difference(set1) set2中，不属于set1的
    # set1.intersection(set2) 交集
    # set1.union(set2) 两个set的并集
    # set1 ^ set2 两个set里所有的”or"


if __name__ == "__main__":
    main()
