def main():
    import math
    '''
    1. input the price of the house
    2. annual salary
    3. percent the user can save from the monthly salary

    problem1 calculate down payment

    '''
    total_price = float(input("Total price of the house \n"))
    annual_salary = float(input("How much you make annually? \n"))
    months = 12
    down_payment_percent = 0.25
    monthly_savings_rate = float(input("How many percent you can save from the monthly salary? \n Please enter a number between 0 and 1 e.g. 0.1 for 10% \n"))
    remaining_price = total_price * (1 - down_payment_percent)
    monthly_savings = annual_salary * monthly_savings_rate / months

    down_payment = total_price * down_payment_percent
    months_for_down_payment = math.ceil(down_payment / monthly_savings)
    years_for_down_payment = months_for_down_payment // months
    months_miunus_years = months_for_down_payment % months

    print("How much the user needs for the down payment? \n", down_payment)
    print("How much money the user saves per month? \n", monthly_savings)
    print("How many months it will take to save enough for the down payment?\n", months_for_down_payment)
    print("How many years + months that is?\n", str(years_for_down_payment), "years and", str(months_miunus_years), "months")


if __name__ == '__main__':
    main()
