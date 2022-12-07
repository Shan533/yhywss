'''
Sample Code
CS 5001, Fall 2021, Lecture 8
This sample code shows how to work with Python dictionaries.
'''


def main():
    print("Working with dictionaries")
    # Dictionary - unordered, key:value pairs. Created using {}
    food_colors = {
        "carrot": "orange",
        "banana": "yellow",
        "lettuce": "green"
    }

    # Access an item using its key.
    print(food_colors["carrot"])

    # Get all keys in the dictionary using .keys()
    print(food_colors.keys())

    # Get all values in the dictionary using .values()
    print(food_colors.values())
    print("orange" in food_colors.values())

    # Add and remove items using the key
    # TODO: Add a new key, "strawberry", with the value "red"
    food_colors["strawberry"] = "red"
    print(food_colors.items())

    # TODO: Remove "lettuce" (and its value) from the
    # dictionary using .pop(key)
    food_colors.pop("lettuce")
    print(food_colors.items())

    # TODO: Change the value belonging to a key by using its key
    food_colors["banana"] = "purple"
    print(food_colors.items())

    # You can use get() to protect against missing keys (KeyError)
    print(food_colors.get("lettuce", "FOO"))


if __name__ == "__main__":
    main()
