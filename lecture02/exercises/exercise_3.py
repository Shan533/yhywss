def main():
    hello_world = "hello worlD"
    all_caps = hello_world.upper()
    capital = hello_world.capitalize()
    replace = hello_world.replace("hello", "Goodbye").replace("world", "World")
    swap = hello_world.swapcase()
    print(all_caps)
    print(capital)
    print(replace)
    print(swap)


if __name__ == "__main__":
    main()
