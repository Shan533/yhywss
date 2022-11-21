def main():

    '''
    1.input the amount of total money
    2. tips from 0-1
    3. how many person this bill with split

    '''

    amount = float(input("how much was this bill? \n"))
    tips = float(input("how much tips were this bill with? \nPlease input a \
                       number from 0 to 1 \n"))
    persons = float(input("how many people were this bill with? \n"))

    total_bill = amount + tips
    bill_per_person = total_bill / persons

    print("the bill for each person is", round(bill_per_person, 2))


if __name__ == '__main__':
    main()
