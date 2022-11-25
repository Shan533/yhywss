
'''
    1.input the amount of total money
    2. tips from 0-1
    3. how many person this bill with split
'''

'''

    定义 function
    1. 用户输入钱/tip和人数
    2. 计算总金额
    3. 计算人均金额
'''


def calculate_total_bill(amount, tips):
    '''
        Function - calculate_total_bill
            calculates the total amount of money for the initial bill
        Input:
            amount: float, Initial bill amount
            tips: float from 0 to 1.
        Return:
            total_bill: float, total money need to pay
    '''
    total_bill = amount * (1 + tips)
    return total_bill


def calculate_bill_per_person(total_bill, persons):
    '''
        Function - calculate_bill_per_person
            calculates the bill for each person
        Input:
            total_bill: float, total money this party needs to pay
            persons: int, how many people this party has
        Return:
            bill_per_person: float, the bill that one person need to pay
    '''
    bill_per_person = total_bill / persons
    return bill_per_person


def main():

    amount = float(input("how much was this bill? \n"))
    tips = amount * float(input("how much tips were this bill with? \n \
                                Please input a number from 0 to 1 \n"))
    persons = float(input("how many people were this bill with? \n"))
    total_bill = calculate_total_bill(amount, tips)
    bill_per_person = calculate_bill_per_person(total_bill, persons)

    print("the bill for each person is", round(bill_per_person, 2))


if __name__ == '__main__':
    main()
