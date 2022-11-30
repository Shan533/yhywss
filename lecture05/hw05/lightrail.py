'''
YOUR FILE COMMENT HERE
'''
LINK_STATIONS = ("Northgate", "Roosevelt", "U District",
                 "University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


'''
    Function -- is_valid_station
        Checks if a given string is a valid Seattle light rail station.
        Provided station must match a station name exactly. For example, "mount
        baker" would not be valid because the case doesn't match.
    Parameter:
        station -- The string to check
    Returns:
        True if a given string is a valid Seattle light rail station
        name, False otherwise.
'''


def is_valid_station(station):
    if station in LINK_STATIONS:
        return True
    else:
        return False


'''
    Function -- get_direction
        Given start and end station names, determines if the direction is
        Northbound or Southbound.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        "Northbound" if the end station is north of the start station, or
        "Southbound" if the end station is south of the start station. If
        either station is invalid, or start and end stations are the same,
        return "No destination found".
'''


def get_direction(start, end):
    if start in LINK_STATIONS and end in LINK_STATIONS:
        for i, station in enumerate(LINK_STATIONS):
            if start == station:
                start_position = i
            if end == station:
                end_position = i
        direction_code = calculation(start_position, end_position)
        if direction_code > 0:
            return "Northbound"
        elif direction_code < 0:
            return "Southbound"
        else:
            return "No destination found"
    else:
        return "No destination found"


def calculation(start_position, end_position):
    direction = start_position - end_position
    return direction


'''
    Function -- get_num_stops
        Calculates the number of stops from start to end.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        The number of stops from start to end. If either station is invalid
        or both stations are the same, return 0.
'''


def get_sum_stops(start, end):
    if start in LINK_STATIONS and end in LINK_STATIONS:
        for i, station in enumerate(LINK_STATIONS):
            if start == station:
                start_position = i
            if end == station:
                end_position = i
        if start_position >= end_position:
            sum_stop = start_position - end_position
        else:
            sum_stop = end_position - start_position
        return sum_stop


def main():

    start = input("Enter your start station \n")
    end = input("Enter your end station \n")
    direction = get_direction(start, end)
    print("your direction is: \n", direction)

    if direction == "Northbound":
        sum_stops = get_sum_stops(start, end)
    elif direction == "Southbound":
        sum_stops = get_sum_stops(end, start)
    else:
        sum_stops = 0
    print("your number of stops is: \n", sum_stops)


if __name__ == "__main__":
    main()
