'''
Sample Code
CS 5001, Fall 2022 - Lecture 4

A drive-through ordering system
'''


def calc_item_cost(quantity, price):
    '''
        Function -- calc_item_cost
            Calculate cost based on the quantity ordered and the price per item
        Parameters:
            quantity -- The quantity ordered
            price -- The price of the item
        Returns:
            The subtotal for the item
    '''
    return quantity * price


def calc_subtotal(cost1, cost2, cost3):
    '''
        Function -- calc_subtotal
            Calculate the subtotal for the order.
        Parameters:
            cost1 - the cost of the first item type
            cost2 - the cost of the second item type
            cost3 - the cost of the third item type
        Returns:
            The order subtotal.
    '''
    return cost1 + cost2 + cost3


def calc_tax(subtotal, rate):
    '''
        Function -- calc_tax
            Calculates the tax due on an order.
        Parameters:
            subtotal -- the order subtotal
            rate -- the tax rate. A float between 0 and 1.
    '''
    return subtotal * rate


def calc_total(subtotal, tax):
    '''
        Function -- calc_total
            Totals the order: cost of each menu item ordered plus tax.
        Parameters:
            subtotal -- the subtotal before tax
            tax -- the tax amount
        Returns:
            The order total.
    '''
    return subtotal + tax


def receipt_line(item_name, quantity, unit_price, subtotal):
    '''
        Function -- receipt_line
            Formats a receipt line item.
        Parameters:
            item_name -- the name of the item.
            quantity -- the quantity ordered.
            unit_price -- the unit price of the item.
            sub_total -- the line item subtotal.
        Returns:
            A formatted line for the receipt.
    '''
    return "{}: {} x ${:.2f} = ${:.2f}".format(item_name, quantity, unit_price,
                                               subtotal)


def receipt_subtotal(subtotal):
    '''
        Function -- receipt_subtotal
            Formats the subtotal line of a receipt.
        Parameters:
            subtotal -- The subtotal amount.
        Returns:
            The formatted subtotal line of a receipt.
    '''
    return "Total before tax: ${:.2f}".format(subtotal)


def receipt_tax(tax):
    '''
        Function -- receipt_tax
            Formats the tax line of a receipt.
        Parameters:
            tax -- The tax amount.
        Returns:
            The formatted tax line of a receipt.
    '''
    return "Tax: ${:.2f}".format(tax)


def receipt_total(total):
    '''
        Function -- receipt_total
            Formats the total line of a receipt.
        Parameters:
            total -- The total amount.
        Returns:
            The formatted total line of a receipt.
    '''
    return "Total: ${:.2f}".format(total)


def main():
    CHEESEBURGER_PRICE = 2.00
    FRIES_PRICE = 2.05
    MILKSHAKE_PRICE = 2.85
    TAX_RATE = 0.1

    MOVIE_TICKET_PRICE = 7.95
    ADMISSIONS_TAX = .05

    print("Welcome to the drive through.")
    # Ask the customer how many of each of the following they would like:
    # cheeseburgers, fries, and milkshakes
    cheeseburgers = int(input("How many cheeseburgers would you like? "))
    fries = int(input("How many orders of fries would like? "))
    milkshake = int(input("How many milkshakes would you like? "))

    # Ask the customer to provide a name for the order
    name = input("Can I get a name for the order? ")

    cheeseburgers_cost = calc_item_cost(cheeseburgers, CHEESEBURGER_PRICE)
    fries_cost = calc_item_cost(fries, FRIES_PRICE)
    milkshakes_cost = calc_item_cost(milkshake, MILKSHAKE_PRICE)
    subtotal = calc_subtotal(cheeseburgers_cost, fries_cost, milkshakes_cost)
    tax = calc_tax(subtotal, TAX_RATE)
    total = calc_total(subtotal, tax)

    # Print an itemized receipt for the order, including their name.
    print("RECEIPT:")
    print("Order for", name)
    # Here are the prices:
    # cheeseburger = 2.00, fries = 2.05, milkshake = 2.85
    print(receipt_line("Cheeseburgers", cheeseburgers, CHEESEBURGER_PRICE,
                       cheeseburgers_cost))
    print(receipt_line("Fries", fries, FRIES_PRICE, fries_cost))
    print(receipt_line("Milkshakes", milkshake, MILKSHAKE_PRICE,
                       milkshakes_cost))
    # Add 10% tax to the total
    print(receipt_subtotal(subtotal))
    print(receipt_tax(tax))
    print(receipt_total(total))

    # NEW FEATURE
    movie_tickets = int(input("How many movie tickets would you like? "))

    # Print an itemized receipt for the customer
    # which includes the number of tickets,
    # the price before tax, the tax amount,
    # and the total paid.
    movie_tickets_cost = calc_item_cost(movie_tickets, MOVIE_TICKET_PRICE)
    movie_tickets_tax = calc_tax(movie_tickets_cost, ADMISSIONS_TAX)
    movie_tickets_total = calc_total(movie_tickets_cost, movie_tickets_tax)
    print(receipt_line(
        "Movie Tickets", movie_tickets, MOVIE_TICKET_PRICE,
        movie_tickets_cost))
    print(receipt_subtotal(movie_tickets_cost))
    print(receipt_tax(movie_tickets_tax))
    print(receipt_total(movie_tickets_total))


if __name__ == "__main__":
    main()
