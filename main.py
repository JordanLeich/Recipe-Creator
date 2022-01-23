import sys
from colors import print_red, print_green
from os.path import exists as file_exists


# Constant variables
INGREDIENTS_LIST_FILE_PATH = 'ingredients.txt'


def main() -> None:  # sourcery no-metrics
    """Holds all possible recipe ingredients and then outputs all possible recipes based upon every line that is read
    in the ingredients.txt file."""

    if file_exists(INGREDIENTS_LIST_FILE_PATH):  # To verify the file exist.
        with open(INGREDIENTS_LIST_FILE_PATH) as file:
            ingredients_list = file.read().splitlines() # TODO steralize list of invalid characters  
    else:  # When the file doesn't exist.
        print_red('Please create a new text file named: ingredients.txt and rerun the program!\n', 2)
        # TODO create file, open and allow user to input details for next rerun of program
        sys.exit()

    recipes = {  # TODO: Keep adding more recipes
        'Macaroni & Cheese': ['milk', 'noodles', 'cheese'],
        'Cheese Sticks': ['cheese', 'dough'],
        'Cheese Bread': ['cheese', 'dough'],
        'Baked Bread Sticks': ['bread'],
        'Cheese Quesadillas': ['tortilla', 'cheese'],
        'Chicken & Cheese Quesadillas': ['chicken', 'cheese', 'tortilla'],
        'Meat & Cheese Quesadillas': ['meat', 'cheese', 'tortilla'],
        'Ham & Cheese Sandwich': ['ham', 'cheese', 'bread'],
        'Scrambled Eggs': ['eggs'],
        'Sunny Side Eggs': ['eggs'],
        'Omelette': ['eggs'],
        'Hot dogs': ['buns', 'hotdog'],
        'Chili Cheese Dogs': ['buns', 'hotdog', 'chili', 'cheese'],
        'Tacos': ['meat', 'shell'],
        'Tacos w/Chicken': ['chicken', 'shell'],
        'Taco Salad': ['meat', 'chips', 'lettuce'],
        'Grilled Cheese': ['cheese', 'bread'],
        'French Toast': ['bread', 'eggs'],
        'Burger': ['meat', 'buns'],
        'Cheese Burger': ['meat', 'buns', 'cheese'],
        'Pasta': ['noodles', 'sauce'],
        'Pasta w/Meat': ['noodles', 'sauce', 'meat'],
        'Spaghetti': ['noodles', 'sauce'],
        'Alfredo': ['noodles', 'sauce'],
        'Chicken Alfredo': ['noodles', 'sauce', 'chicken'],
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
        'Nachos': ['chips', 'meat', 'salsa'],
        'Nachos w/Cheese': ['chips', 'meat', 'salsa', 'cheese'],
    }
    found_food = False
    for food, ingredients in recipes.items():  # N^2 algorithm # TODO decrease time complexity
        if all(x in ingredients_list for x in ingredients): # check if ingredients are a sublist of ingredients_list
            print_green(food)
            found_food = True
            print()
            
    if not found_food:
        print_red('No recipes can be created, try adding more to the ingredients.txt file and rerun the '
                  'program!\n', 3)


if __name__ == '__main__':
    main()
