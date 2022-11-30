campuses = ["boston", "seattle", "vancouver"]

for i, city in enumerate(campuses):
    print("the campus", i + 1, "is in", city)

campuses[2] = "portland"

for i, city in enumerate(campuses):
    print("the campus", i + 1, "is in", city)

campuses.append("london")

for i, city in enumerate(campuses):
    print("the campus", i + 1, "is in", city)

campuses.insert(0, "toronto")

for i, city in enumerate(campuses):
    print("the campus", i + 1, "is in", city)

campuses.remove("london")
print(campuses)

output = "tocoma" in campuses
output_2 = "london" in campuses
output_3 = "seattle" in campuses
print(output, output_2, output_3)

jeep = campuses.pop(0)
print("jeep =", jeep)
audi = campuses.pop()
print(audi)
