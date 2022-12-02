def time_validator(times):
    parts = times.split(":")
    if len(parts) != 2:
        raise ValueError("HH:MM")
    return parts[0]


def main():
    times = input("Enter \n")
    print(time_validator(times))


if __name__ == "__main__":
    main()
