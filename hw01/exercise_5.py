pizzas = int(input("how many pizzas you are going to buy: \n"))
slices_per_pizza = int(input("how many slices a pizza can be cut into: \n"))
slices_per_guest = int(input("how many slices each guest would eat: \n"))
slices_total = slices_per_pizza * pizzas
guests = slices_total // slices_per_guest
print(guests)
