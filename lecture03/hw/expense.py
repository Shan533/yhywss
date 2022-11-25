def calculate_mileage(start, end):
    '''
    Function --
        calculate_mileage Calculates miles driven using the start and end
        odometer values.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
        number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a number
        greater than 0 and greater than the start value.

    Returns: The miles driven, a number. If either parameter is invalid
             (e.g. either parameter is negative or end is less than start),
             returns 0.
    '''
    if start <= 0 or end <= start:
        return 0
    else:
        miles_driven = end - start
        return miles_driven


def get_reimbursement_amount(mileage):
    '''
        Function -- get_reimbursement_amount
            Calculates the amount in dollars that the employee should be
            reimbursed based on their mileage and the standard rate per mile.
            The standard rate for 2020 is 57.5 cents per mile.

        Parameters:
            mileage -- The number of miles driven.

        Returns:
            The amount the employee should be reimbursed in dollars,
            a float rounded to 2 decimal places.
    '''
    RATE = 0.575
    reimbursed_amount = round(RATE * mileage, 2)
    return reimbursed_amount


def get_actual_mileage_rate(mpg, fuel_price):
    '''
        Function --
        get_actual_mileage_rate Calculates the actual trip cost per
        mile in dollars based on the car's MPG and the fuel price.

        Parameters:
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel cost in dollars per gallon, a non-negative
        float.

        Returns:
        The actual cost per mile in dollars, a float rounded to 4 decimal
        places.
        If supplied arguments are invalid, returns 0.0
    '''
    if mpg < 0 or fuel_price < 0 or type(mpg) != int:
        actual_cost = 0.0
        return actual_cost
    else:
        actual_cost = round(fuel_price / mpg, 4)
        return actual_cost


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''

    Function --
        get_actual_trip_cost Calculates the cost of a trip in dollars
        based on the miles driven, the MPG of the car, and the fuel price
        per gallon.

    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
                 number greater than 0.

        end -- The odometer reading at the end of the trip. Expecting a number
               greater than 0 and greater than the start value.

        mpg -- The car's miles per gallon (MPG), an integer greater than 0.

        fuel_price -- The fuel price per gallon, a non-negative float.

    Returns:
    The cost of the drive in dollars, a float rounded to 2 decimal
    places. If any of the supplied arguments are invalid, returns 0.0

'''

    if not 0 < start < end:
        return 0.0
    elif float(mpg) <= 0 or fuel_price < 0 or type(mpg) != int:
        return 0.0
    else:
        mileage = end - start
        actual_cost = round(mileage * fuel_price / mpg, 2)
        return actual_cost


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR \n \
            Options: \n \
            1 - Calculate reimbursement amount from odometer readings \n \
            2 - Calculate reimbursement amount from miles traveled \n \
            3 - Calculate the actual cost of your trip")
    choice = input("Enter your choice (1, 2, or 3): \n")

    if choice == "1":
        start = float(input("Enter your starting odometer reading: \n"))
        end = float(input("Enter your ending odometer reading: \n"))
        mileage = calculate_mileage(start, end)
        reimbursement_amount = get_reimbursement_amount(mileage)
        print("You will be reimbursed $", reimbursement_amount)
    elif choice == "2":
        mileage = float(input("Enter the number of miles traveled: \n"))
        if mileage >= 0:
            reimbursement_amount = get_reimbursement_amount(mileage)
        else:
            reimbursement_amount = 0.0
        print("You will be reimbursed $", reimbursement_amount)
    elif choice == "3":
        start = float(input("Enter your starting odometer reading: \n"))
        end = float(input("Enter your ending odometer reading: \n"))
        mpg = int(input("Enter your car's MPG: \n"))
        fuel_price = float(input("Enter the fuel price per gallon: \n"))
        actual_cost = get_actual_trip_cost(start, end, mpg, fuel_price)
        print("Your trip cost $", actual_cost)
    else:
        print("Not a valid choice")


if __name__ == "__main__":
    main()
