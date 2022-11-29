'''
sentence = "Today is Tuesday"
print(sentence[-3:])
a = sentence[1:3:-1]
b = sentence[3:1:-1]

print(a)
print(b)

'''


def count_up(number):
    count = 1
    while count < number:
        count = str(count) + str(count + 1)
        count += 1
    return count


def count_down(number):
    count = 1
    while count < number:
        count = str(number) + str(number - 1)
        count -= 1
    return count


def print_evens():
    number = 2
    count = 99
    total = number
    while number < 100:
        total = total + (number + 1)
        number += 1
    
    average = total / count
    return average
    