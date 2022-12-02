'''
user input 1/2/3
validate input immediately

if 1 -- save a new recipe
    ● "Enter the ingredients on one line. Separate
    each ingredient with a comma. "
    ● "Enter the directions (1 paragraph only): "
    ● "Enter the time needed in minutes: "
    ● "Enter the name of the recipe: "
if 2 -- read a recipe
if 3 -- quit

'''


def input_validation(task_raw):
    try:
        task = int(task_raw.strip())
        return task
    except ValueError:
        print("Invalid input")


def ingredient_validation():
    validation_result = False
    while not validation_result:
        try:
            ingredient_raw = input("Enter the ingredients on one line. Separate each with a comma. \n")
            ingredient = ingredient_raw.strip()
            type(ingredient[0])
            validation_result = True
        except IndexError:
            print("Recipe must have at least one ingredient.")
    return ingredient


def strings_to_list(strings):
    recipe_list = []
    recipe_list_raw = strings.split(",")
    for item in recipe_list_raw:
        recipe_list.append(item.strip())
    return recipe_list


def time_validation():
    valid_input = False
    while not valid_input:
        try:
            time_raw = input("Enter the time needed in minutes: \n")
            time = int(time_raw)
            # validating_string = "test" * time
            if time < 0:
                raise ValueError("Invalid time. Must be an integer greater than or equal to 0")
            else:
                valid_input = True

        except ValueError:
            print("Invalid time. Must be an integer greater than or equal to 0")
    return time


def name_validation(raw_name):
    recipe_valid = False
    recipe_valid_2 = True
    recipe_name = ""
    while not recipe_valid:
        recipe_name_half = raw_name.strip().lower().replace(" ", "_")
        while not recipe_valid_2:
            raw_name = input("Enter a string containing only letters, numbers, and spaces")
            # recipe_name_half = raw_name.strip().lower().replace(" ", "_")
        for i in range(len(recipe_name_half)):
            if not recipe_name_half[i].isalnum():
                recipe_name = recipe_name_half.replace(recipe_name_half[i], "")
        if len(recipe_name) == 0:
            recipe_valid_2 = False
            raise ValueError("unable to create the filename. \n")

        else:
            recipe_valid = True
    file_path = "lecture06/hw06/" + recipe_name + ".txt"
    return file_path


def content_generator(recipe_list, time, file_path, directions):
    time_expression = "Time: " + str(time) + " minutes"
    head = [file_path, "", "Ingredients", ""]
    foot = ["", time_expression, "", "Directions:", directions]
    content = head + recipe_list + foot
    return content


def main():
    task_raw = input("MENU: 1 - Save a new recipe, \
2 - Read a recipe, 3 - Quit \n")
    task = input_validation(task_raw)
    if task == 1:
        ingredient = ingredient_validation()
        recipe_list = strings_to_list(ingredient)
        directions = input("Enter the directions (1 paragraph only): ")
        time = time_validation()

        raw_name = input("Enter the name of the recipe")
        file_path = name_validation(raw_name)
        file = open(file_path, "w")

        content = content_generator(recipe_list, time, file_path, directions)
        for item in content:
            file.write(item + "\n")
        file.close()
        print(raw_name, "recipe saved to", file_path)

    if task == 2:
        path_valid = False
        while not path_valid:
            try:
                raw_name = input("Enter the name of the recipe: \n")
                file_path = name_validation(raw_name)
                with open(file_path, "r") as file:
                    path_valid = True
                    file_contents = file.read()
                    print(file_contents)
            except FileNotFoundError:
                print("Unable to print", raw_name)

    if task == 3:
        print("Thanks for using")


if __name__ == '__main__':
    main()
