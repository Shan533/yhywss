#You're hosting a pizza party and you're planning to order 20 pizzas. Write some code to calculate how many guests you can have, assuming each pizza has 8 slices and each person will eat 3 slices.

pizzas = 20
slices_total = 8 * pizzas
slices_per_guest = 3
guests = slices_total // slices_per_guest

print(guests)

# Your local pizza restaurant charges 9.99 for standard pizzas (pepperoni, veggie, cheese etc) and 12.99 for specialty pizzas. You decide to order 3 specialty pizzas for your party. The remaining pizzas will be standard. Your local pizza restaurant has a buy-one-get-one half price offer on standard pizzas. How much will your order cost in total?

pizzas_standard = 5
cost_specialty = 12.99 * 3
cost_standard = 5 // 2 * 9.99

cost_total = cost_specialty + cost_standard

print(cost_total)