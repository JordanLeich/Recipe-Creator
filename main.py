import os
import sys
from colors import print_red, print_green
from time import sleep


def main():  # sourcery no-metrics
    """Holds all possible recipe ingredients and then outputs all possible recipes based upon every line that is read
    in the ingredients.txt file."""
    ingredients_list_file_path = 'ingredients.txt'

    try:
        with open('ingredients.txt') as file:
            ingredients_list = file.read().splitlines()

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
                'Hotdogs': ['buns', 'hotdog'],
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

            for food, ingredients in recipes.items():
                if all(map(lambda i: i in ingredients_list, ingredients)):
                    print_green(food)
                    print()
            if os.stat(ingredients_list_file_path).st_size == 0:
                print_red('No recipes can be created, try adding more to the ingredients.txt file and rerun the '
                          'program!\n', 3)

        sleep(1)
        input("Press enter to exit...")
        file.close()
        sys.exit()
    except FileNotFoundError:
        print_red('Please create a new text file named: ingredients.txt and rerun the program!\n', 2)
        input("Press enter to exit...")
        sys.exit()


if __name__ == '__main__':
    main()
