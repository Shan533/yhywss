'''

empty_list = ["1"]
word = "test"
print(type(empty_list[0]))
print(type(word[0]))
validation_result = False
while not validation_result:
    try:
        ingredient = input("give me some input")
        type(ingredient[0])
        validation_result = True
    except IndexError:
        print("Recipe must have at least one ingredient.")

'''

test = "a" * 5
test_1 = "a" * 0
test_2 = "a" * -4
print(len(test))
print(len(test_1))
print(len(test_2))
print(test_1)
print(test_2)