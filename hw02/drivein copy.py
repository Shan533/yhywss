'''
Starter Code
CS5001, Fall 2022 - Lecture 2, exercise 5
This program calculates a customer's bill for a drive-in restaurant.
'''


def main():

    CHEESEBURGER_PRICE = 1.99
    FRIES_PRICE = 1.00
    COMBO_DISCOUNT = 0.9  # Applied if an order includes cheeseburgers and
    # fries and it's a  weekend
    DAY_DISCOUNT = 0.5  # Applied on weekdays.
    TAX = 1.1  # Applied after any discounts.

    cheeseburgers = int(input("How many cheeseburgers do you want? "))
    fries = int(input("How many orders of fries do you want? "))
    day = input("What day is it? (M, Tu, W, Th, F, Sa, or Su) ")
    day = day.upper()

    is_combo = cheeseburgers > 0 and fries > 0

    if day == "M" or day == "TU" or day == "W" or day == "TH" or day == "F" 
            and not is_combo:
        subtotal = cheeseburgers * CHEESEBURGER_PRICE + fries * FRIES_PRICE
        price_after_discount = subtotal * DAY_DISCOUNT
        total_after_tax = price_after_discount * TAX
        print("Total: ${:.2f}".format(total_after_tax))
    elif day == "M" or day == "TU" or day == "W" or day == "TH" or day == "F" and is_combo:
        subtotal = cheeseburgers * CHEESEBURGER_PRICE + fries * FRIES_PRICE
        price_after_discount = subtotal * DAY_DISCOUNT
        total_after_tax = price_after_discount * TAX
        print("Total: ${:.2f}".format(total_after_tax))
    elif day == "SA" or day == "SU" and is_combo:
        subtotal = cheeseburgers * CHEESEBURGER_PRICE + fries * FRIES_PRICE
        price_after_discount = subtotal * COMBO_DISCOUNT
        total_after_tax = price_after_discount * TAX
        print("Total: ${:.2f}".format(total_after_tax))
    elif day == "SA" or day == "SU" and not is_combo:
        subtotal = cheeseburgers * CHEESEBURGER_PRICE + fries * FRIES_PRICE
        total_after_tax = subtotal * TAX
        print("Total: ${:.2f}".format(total_after_tax))


if __name__ == "__main__":
    main()
