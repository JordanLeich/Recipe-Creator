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
            if 'milk' in ingredients_list and 'noodles' in ingredients_list and 'cheese' in ingredients_list:
                print_green('Macaroni & Cheese\n')
            if 'cheese' in ingredients_list and 'dough' in ingredients_list:
                print_green('Cheese Sticks\n')
                print_green('Cheese Bread\n')
            if 'bread' in ingredients_list:
                print_green('Baked Bread Sticks\n')
            if 'tortilla' in ingredients_list and 'cheese' in ingredients_list:
                print_green('Cheese Quesadillas\n')
            if 'tortilla' in ingredients_list and 'cheese' in ingredients_list and 'chicken' in ingredients_list:
                print_green('Chicken & Cheese Quesadillas\n')
            if 'tortilla' in ingredients_list and 'cheese' in ingredients_list and 'meat' in ingredients_list:
                print_green('Meat & Cheese Quesadillas\n')
            if 'cheese' in ingredients_list and 'bread' in ingredients_list and 'ham' in ingredients_list:
                print_green('Ham & Cheese Sandwich\n')
            if 'eggs' in ingredients_list or 'egg' in ingredients_list:
                print_green('Scrambled Eggs\n')
                print_green('Sunny Side Eggs\n')
                print_green('Omelette\n')
            if 'bread' in ingredients_list and 'hotdog' in ingredients_list or 'bun' in ingredients_list:
                print_green('Hotdogs\n')
            if 'meat' in ingredients_list and 'shell' in ingredients_list:
                print_green('Tacos w/Meat\n')
            if 'chicken' in ingredients_list and 'shell' in ingredients_list or 'shells' in \
                    ingredients_list:
                print_green('Tacos w/Chicken\n')
            if 'meat' in ingredients_list and 'chips' in ingredients_list or 'shells' in \
                    ingredients_list and 'salad' in ingredients_list or 'lettuce' in ingredients_list:
                print_green('Tacos Salad\n')
            if 'bread' in ingredients_list and 'cheese' in ingredients_list:
                print_green('Grilled Cheese\n')
            if 'bread' in ingredients_list and 'egg' in ingredients_list or 'eggs' in ingredients_list:
                print_green('French Toast\n')
            if 'bread' in ingredients_list and 'meat' in ingredients_list or 'burger' in ingredients_list:
                print_green('Burger\n')
            if 'bread' in ingredients_list and 'meat' in ingredients_list or 'burger' in ingredients_list and 'cheese' \
                    in ingredients_list:
                print_green('Cheese Burger\n')
            if 'noodles' in ingredients_list and 'sauce' in ingredients_list:
                print_green('Pasta\n')
                print_green('Spaghetti\n')
                print_green('Alfredo\n')
            if 'noodles' in ingredients_list and 'sauce' in ingredients_list and 'meat' in ingredients_list:
                print_green('Pasta or Spaghetti or Alfredo w/Meat\n')
            if 'noodles' in ingredients_list and 'sauce' in ingredients_list and 'chicken' in ingredients_list:
                print_green('Pasta or Spaghetti or Alfredo w/Chicken\n')
            if 'chicken' in ingredients_list and 'rice' in ingredients_list:
                print_green('Chicken & Rice Combination\n')
            if 'ice cream' in ingredients_list and 'milk' in ingredients_list:
                print_green('Ice Cream Shake Drink\n')
            if 'potato' in ingredients_list or 'potatoes' in ingredients_list:
                print_green('Baked potato\n')
                print_green('French Fries\n')
            if 'potato' in ingredients_list or 'potatoes' in ingredients_list and 'cheese' in ingredients_list:
                print_green('Cheesy Baked potato\n')
                print_green('French Fries\n')
            if 'meat' in ingredients_list and 'tomato' in ingredients_list or 'tomatoes' in ingredients_list:
                print_green('Chili\n')
            if 'beans' in ingredients_list and 'meat' in ingredients_list and 'tomato' in ingredients_list or \
                    'tomatoes' in ingredients_list:
                print_green('Chili w/Beans\n')
            if 'potato' in ingredients_list or 'potatoes' in ingredients_list and 'cheese' in ingredients_list and \
                    'meat' in ingredients_list or 'chili' in ingredients_list:
                print_green('Chili Cheese French Fries\n')
            if 'dough' in ingredients_list and 'cheese' in ingredients_list and 'sauce' in ingredients_list:
                print_green('Pizza\n')
            if 'dough' in ingredients_list and 'cheese' in ingredients_list and 'sauce' in ingredients_list and 'meat' \
                    in ingredients_list:
                print_green('Pizza w/Meat\n')
            if 'dough' in ingredients_list and 'cheese' in ingredients_list and 'sauce' in ingredients_list and \
                    'chicken' in ingredients_list:
                print_green('Pizza w/Chicken\n')
            if 'chips' in ingredients_list and 'meat' in ingredients_list and 'salsa' in ingredients_list:
                print_green('Nachos\n')
            if 'chips' in ingredients_list and 'meat' in ingredients_list and 'salsa' in ingredients_list and \
                    'cheese' in ingredients_list:
                print_green('Nachos w/Cheese\n')
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
