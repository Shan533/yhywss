'''
sentence = "Today is Tuesday"
print(sentence[-3:])
a = sentence[1:3:-1]
b = sentence[3:1:-1]

print(a)
print(b)

'''
for man in range(1, -10, 1):
    print(man)

'''
for count in range(11):
    print(count)
'''
'''
number = 0
while number < 11:
    print(number)
    number = number + 1
# using while loop and for loop to calculate "n!"
'''


def calculating(n):
    total = 1
    while n >= 1:
        total = n * total
        n -= 1
    return total


def calculating_for(n):
    total = 1
    for number in range(n + 1):
        if number == 1:
            total = 1
        total *= number
    return total


print(calculating(3))
print(calculating_for(3))
print("test_length_checker")
