factor_1 = float(input("give me a number"))
factor_2 = input("what operations are you going to do next?")
subtotal = factor_1

while factor_2.upper() != "Q":
    if factor_2[0] == "+":
        subtotal = subtotal + float(factor_2[1:].replace(" ", ""))
    elif factor_2[0] == "-":
        subtotal = subtotal - float(factor_2[1:].replace(" ", ""))
    elif factor_2[0] == "*":
        subtotal = subtotal * float(factor_2[1:].replace(" ", ""))
    elif factor_2[0] == "-":
        subtotal = subtotal / float(factor_2[1:].replace(" ", ""))
    else:
        print("Invalid operations")

    print(subtotal)
    factor_2 = input("what operations are you going to do next?")
print("Thank you!")
print("Your final subtotal is", subtotal)
