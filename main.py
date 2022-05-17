import sys
from colors import print_red, print_green, print_yellow
from os.path import exists as file_exists

# Constant variables
INGREDIENTS_LIST_FILE_PATH = 'ingredients.txt'


def add_to_ingredients_file() -> list:
    """Allows the user to manually add ingredients to their ingredients.txt file."""
    print_yellow('Please enter either exit, close, or stop to stop adding ingredients to your list.\n', 1)

    with open(INGREDIENTS_LIST_FILE_PATH, 'w') as file:
        ingredients_list = []
        user_input_ingredients = ''
        while user_input_ingredients.lower() not in ['exit', 'close', 'stop']:
            user_input_ingredients = str(input('Ingredient name: '))
            print()
            file.write(f"{user_input_ingredients}\n")
            ingredients_list.append(user_input_ingredients)
            print_green('Ingredient added!\n')
        print_yellow('Ingredients have finished being added.\n', 1)
    print_green('Here are all of the possible recipes.\n', 1)
    return ingredients_list


def main() -> None:  # sourcery no-metrics
    """Holds all possible recipe ingredients and then outputs all possible recipes based upon every line that is read
    in the ingredients.txt file."""

    if file_exists(INGREDIENTS_LIST_FILE_PATH):  # To verify the file exist.
        with open(INGREDIENTS_LIST_FILE_PATH) as file:
            ingredients_list = file.read().splitlines()
    else:  # When the file doesn't exist.
        print_red('Since the ingredients.txt file does not exist, a new file will be created!\n', 2)
        ingredients_list = add_to_ingredients_file()

    recipes = {  # TODO: Keep adding more recipes
        'Macaroni & Cheese': ['milk', 'noodles', 'cheese'],
        'Cheese Sticks': ['cheese', 'dough'],
        'Cheese Bread': ['cheese', 'dough'],
        'Baked Bread Sticks': ['bread'],
        'Cheese Quesadillas': ['tortilla', 'cheese'],
        'Chicken & Cheese Quesadillas': ['chicken', 'cheese', 'tortilla'],
        'Meat & Cheese Quesadillas': ['meat', 'cheese', 'tortilla'],
        'Ham & Cheese Sandwich': ['ham', 'cheese', 'bread'],
        'Bacon & Cheese Sandwich': ['bacon', 'cheese', 'bread'],
        'BLT Sandwich': ['bacon', 'tomatoes', 'bread', 'lettuce'],
        'Fish Sandwich': ['fish', 'bread'],
        'Turkey Sandwich': ['turkey', 'bread'],
        'Turkey Sandwich w/Cheese': ['turkey', 'bread', 'cheese'],
        'Sausage & Egg Muffin': ['sausage', 'eggs', 'muffins'],
        'Scrambled Eggs': ['eggs'],
        'Cheesy Scrambled Eggs': ['eggs', 'cheese'],
        'Sunny Side Eggs': ['eggs'],
        'Omelette': ['eggs'],
        'Hot Dogs': ['buns', 'hotdog'],
        'Chili Cheese Dogs': ['buns', 'hotdog', 'chili', 'cheese'],
        'Tacos': ['meat', 'shell'],
        'Tacos w/Chicken': ['chicken', 'shell'],
        'Taco Salad': ['meat', 'chips', 'lettuce'],
        'Grilled Chicken Salad': ['lettuce', 'chicken'],
        'Grilled Chicken Avocado Salad': ['lettuce', 'chicken', 'avocado'],
        'Grilled Cheese': ['cheese', 'bread'],
        'French Toast': ['bread', 'eggs'],
        'Burger': ['meat', 'buns'],
        'Cheese Burger': ['meat', 'buns', 'cheese'],
        'Pasta': ['noodles', 'sauce'],
        'Pasta w/Meat': ['noodles', 'sauce', 'meat'],
        'Spaghetti': ['noodles', 'sauce'],
        'Alfredo': ['noodles', 'sauce'],
        'Chicken Alfredo': ['noodles', 'sauce', 'chicken'],
        'Shrimp Scampi Linguine': ['shrimp', 'sauce', 'noodles'],
        'Chicken & Rice Combination': ['chicken', 'rice'],
        'Ice Cream Shake Drink': ['ice cream', 'milk'],
        'Baked potato': ['potatoes'],
        'French Fries': ['potatoes'],
        'Cheesy Baked potato': ['potatoes', 'cheese'],
        'Chili': ['meat', 'tomatoes'],
        'Chili Cheese French Fries': ['meat', 'tomatoes', 'potatoes', 'cheese'],
        'Chili w/Beans': ['meat', 'tomatoes', 'beans'],
        'Pizza': ['dough', 'sauce', 'cheese'],
        'Pepperoni Pizza': ['dough', 'sauce', 'cheese', 'pepperoni'],
        'Pizza w/Meat': ['dough', 'sauce', 'cheese', 'meat'],
        'Pizza w/Chicken': ['dough', 'sauce', 'cheese', 'chicken'],
        'Nachos w/Meat': ['chips', 'meat', 'salsa'],
        'Nachos w/Chicken': ['chips', 'chicken', 'salsa'],
        'Nachos w/Cheese': ['chips', 'meat', 'salsa', 'cheese'],
        'Ice Cream Sandwiches': ['ice cream', 'crackers'],
        'Smore Sandwiches': ['chocolate', 'crackers', 'marshmallows'],
    }
    found_food = False
    for food, ingredients in recipes.items():
        if all(x in ingredients_list for x in ingredients):  # check if ingredients are a sublist of ingredients_list
            print_green(food)
            found_food = True
            print()
    choice = input('Press enter to either continue or exit. Enter add to add to your ingredients list. '
                   'Enter clear to clear all ingredients from the ingredients file: ')
    print()

    if choice.lower() in ['add', 'a']:
        add_to_ingredients_file()
        main()

    if choice.lower() in ['clear', 'clr', 'c']:
        with open(INGREDIENTS_LIST_FILE_PATH, 'r+') as file:
            file.truncate(0)
            print_green('Ingredients file as been cleared successfully!\n', 1)
            choice = input('Want to add to your ingredients list? (yes / no): ')
            print()
            if choice.lower() in ['yes', 'y']:
                add_to_ingredients_file()
                main()
            else:
                sys.exit()

    if not found_food:
        print_red('Sorry, no recipes can be created.\n')
        user_input = str(input('Would you like to add ingredients to the ingredients.txt file (yes / no): '))
        print()
        if user_input.lower() in ['yes', 'y', 'sure']:
            add_to_ingredients_file()
        else:
            sys.exit()

    if found_food:
        sys.exit()


if __name__ == '__main__':
    while True:
        main()
