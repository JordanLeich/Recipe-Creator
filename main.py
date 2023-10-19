import sys
import os

# Constant variables
INGREDIENTS_LIST_FILE_PATH = 'ingredients.txt'

recipes = [
        ('Macaroni & Cheese', ['milk', 'noodles', 'cheese']),
        ('Cheese Sticks', ['cheese', 'dough']),
        ('Cheese Bread', ['cheese', 'dough']),
        ('Baked Bread Sticks', ['bread']),
        ('Cheese Quesadillas', ['tortilla', 'cheese']),
        ('Chicken & Cheese Quesadillas', ['chicken', 'cheese', 'tortilla']),
        ('Meat & Cheese Quesadillas', ['meat', 'cheese', 'tortilla']),
        ('Ham & Cheese Sandwich', ['ham', 'cheese', 'bread']),
        ('Bacon & Cheese Sandwich', ['bacon', 'cheese', 'bread']),
        ('BLT Sandwich', ['bacon', 'tomatoes', 'bread', 'lettuce']),
        ('Fish Sandwich', ['fish', 'bread']),
        ('Turkey Sandwich', ['turkey', 'bread']),
        ('Turkey Sandwich w/Cheese', ['turkey', 'bread', 'cheese']),
        ('Sausage & Egg Muffin', ['sausage', 'eggs', 'muffins']),
        ('Scrambled Eggs', ['eggs']),
        ('Cheesy Scrambled Eggs', ['eggs', 'cheese']),
        ('Sunny Side Eggs', ['eggs']),
        ('Omelette', ['eggs']),
        ('Hot Dogs', ['buns', 'hotdog']),
        ('Chili Cheese Dogs', ['buns', 'hotdog', 'chili', 'cheese']),
        ('Tacos', ['meat', 'shell']),
        ('Tacos w/Chicken', ['chicken', 'shell']),
        ('Taco Salad', ['meat', 'chips', 'lettuce']),
        ('Grilled Chicken Salad', ['lettuce', 'chicken']),
        ('Grilled Chicken Avocado Salad', ['lettuce', 'chicken', 'avocado']),
        ('Grilled Cheese', ['cheese', 'bread']),
        ('French Toast', ['bread', 'eggs']),
        ('Burger', ['meat', 'buns']),
        ('Cheese Burger', ['meat', 'buns', 'cheese']),
        ('Pasta', ['noodles', 'sauce']),
        ('Pasta w/Meat', ['noodles', 'sauce', 'meat']),
        ('Spaghetti', ['noodles', 'sauce']),
        ('Alfredo', ['noodles', 'sauce']),
        ('Chicken Alfredo', ['noodles', 'sauce', 'chicken']),
        ('Shrimp Scampi Linguine', ['shrimp', 'sauce', 'noodles']),
        ('Chicken & Rice Combination', ['chicken', 'rice']),
        ('Ice Cream Shake Drink', ['ice cream', 'milk']),
        ('Baked potato', ['potatoes']),
        ('French Fries', ['potatoes']),
        ('Cheesy Baked potato', ['potatoes', 'cheese']),
        ('Chili', ['meat', 'tomatoes']),
        ('Chili Cheese French Fries', ['meat', 'tomatoes', 'potatoes', 'cheese']),
        ('Chili w/Beans', ['meat', 'tomatoes', 'beans']),
        ('Pizza', ['dough', 'sauce', 'cheese']),
        ('Pepperoni Pizza', ['dough', 'sauce', 'cheese', 'pepperoni']),
        ('Pizza w/Meat', ['dough', 'sauce', 'cheese', 'meat']),
        ('Pizza w/Chicken', ['dough', 'sauce', 'cheese', 'chicken']),
        ('Nachos w/Meat', ['chips', 'meat', 'salsa']),
        ('Nachos w/Chicken', ['chips', 'chicken', 'salsa']),
        ('Nachos w/Cheese', ['chips', 'meat', 'salsa', 'cheese']),
        ('Ice Cream Sandwiches', ['ice cream', 'crackers']),
        ('Smore Sandwiches', ['chocolate', 'crackers', 'marshmallows']),
        ('Fruit Salad', ['apple', 'banana', 'orange', 'grapes']),
        ('Fruit Smoothie', ['banana', 'strawberries', 'yogurt']),
        ('Caesar Salad', ['lettuce', 'croutons', 'parmesan', 'dressing']),
        ('Caprese Salad', ['tomatoes', 'mozzarella', 'basil', 'olive oil']),
        ('Grilled Shrimp', ['shrimp', 'garlic', 'lemon', 'butter']),
        ('Margarita Pizza', ['dough', 'tomatoes', 'mozzarella', 'basil', 'olive oil']),
        ('Vegetable Stir-Fry', ['broccoli', 'carrots', 'bell pepper', 'zucchini', 'soy sauce']),
        ('Spicy Tofu Curry', ['tofu', 'coconut milk', 'curry paste', 'bell pepper', 'onion']),
        ('Homemade Lasagna', ['lasagna noodles', 'ground beef', 'ricotta cheese', 'mozzarella cheese', 'tomato sauce']),
        ('Sushi Rolls', ['sushi rice', 'nori seaweed', 'fish', 'avocado', 'cucumber', 'soy sauce']),
        ('Spinach and Feta Stuffed Chicken', ['chicken breast', 'spinach', 'feta cheese', 'garlic', 'lemon']),
        ('Mango Salsa', ['mango', 'red onion', 'cilantro', 'lime juice']),
        ('Avocado Toast', ['avocado', 'bread', 'salt', 'pepper', 'red pepper flakes']),
        ('Chocolate Chip Cookies', ['flour', 'butter', 'sugar', 'chocolate chips', 'baking soda']),
        ('Fruit Smoothie Bowl', ['yogurt', 'banana', 'strawberries', 'granola', 'honey']),
        ('Pancakes', ['flour', 'milk', 'eggs', 'baking powder', 'syrup']),
        ('Greek Salad', ['cucumber', 'tomato', 'red onion', 'kalamata olives', 'feta cheese']),
        ('Hawaiian Pizza', ['dough', 'tomato sauce', 'ham', 'pineapple', 'mozzarella cheese']),
        ('Crispy Chicken Tenders', ['chicken tenders', 'flour', 'eggs', 'bread crumbs', 'spices']),
        ('Garlic Butter Shrimp', ['shrimp', 'butter', 'garlic', 'lemon juice', 'parsley']),
        ('Caprese Pasta Salad', ['pasta', 'tomatoes', 'mozzarella cheese', 'basil', 'balsamic dressing']),
        ('Veggie Burger', ['veggie patty', 'buns', 'lettuce', 'tomato', 'onion', 'mayonnaise']),
        ('Lemonade', ['lemons', 'sugar', 'water']),
        ('Cucumber Dill Salad', ['cucumbers', 'dill', 'onion', 'sour cream']),
        ('Tofu Scramble', ['tofu', 'bell pepper', 'onion', 'turmeric', 'spinach']),
        ('Cauliflower Rice', ['cauliflower', 'olive oil', 'garlic', 'spices']),
        ('Pulled Pork Sandwich', ['pork shoulder', 'buns', 'barbecue sauce', 'coleslaw']),
        ('Shrimp and Grits', ['shrimp', 'grits', 'bacon', 'cheese', 'green onions']),
        ('Ratatouille', ['eggplant', 'zucchini', 'tomatoes', 'bell pepper', 'garlic']),
        ('Stuffed Bell Peppers', ['bell peppers', 'ground beef', 'rice', 'tomato sauce', 'onion']),
        ('Garlic Knots', ['pizza dough', 'butter', 'garlic', 'parsley']),
        ('Peanut Butter and Jelly Sandwich', ['bread', 'peanut butter', 'jelly']),
        ('Scrambled Tofu', ['tofu', 'turmeric', 'black salt', 'pepper']),
        ('Vegetable Omelette', ['eggs', 'bell pepper', 'onion', 'mushrooms', 'cheese']),
        ('Pasta with Garlic and Olive Oil', ['spaghetti', 'garlic', 'olive oil', 'red pepper flakes']),
        ('Cereal with Milk', ['cereal', 'milk']),
        ('Fried Rice', ['cooked rice', 'vegetables', 'soy sauce', 'eggs']),
        ('Tomato Soup', ['tomatoes', 'onion', 'garlic', 'vegetable broth', 'cream']),
        ('Mashed Potatoes', ['potatoes', 'butter', 'milk']),
        ('Classic BLT Sandwich', ['bread', 'bacon', 'lettuce', 'tomato']),
        ('Oatmeal', ['oats', 'water', 'milk', 'sugar', 'cinnamon']),
        ('Chicken Noodle Soup', ['chicken broth', 'chicken', 'noodles', 'carrots', 'celery']),
        ('Greek Salad', ['cucumber', 'tomato', 'red onion', 'kalamata olives', 'feta cheese']),
    ]

def add_ingredients_to_file():
    """Allows the user to manually add ingredients to their ingredients.txt file."""
    print('Please enter the ingredients. Enter "exit" to stop.')

    ingredients_list = []
    with open(INGREDIENTS_LIST_FILE_PATH, 'a') as file:
        while True:
            user_input_ingredients = input('Ingredient name: ').strip()
            if user_input_ingredients.lower() in ['exit', 'close', 'stop']:
                break
            if user_input_ingredients:
                file.write(f"{user_input_ingredients}\n")
                ingredients_list.append(user_input_ingredients)
                print('Ingredient added!')
            else:
                print('Invalid ingredient name. Please try again.')

    print('Ingredients have finished being added.\n')
    return ingredients_list

def load_ingredients_from_file():
    if os.path.exists(INGREDIENTS_LIST_FILE_PATH):
        with open(INGREDIENTS_LIST_FILE_PATH, 'r') as file:
            ingredients_list = file.read().splitlines()
            return ingredients_list
    else:
        return []

def find_recipes(ingredients_list):
    found_food = False
    for food, recipe_ingredients in recipes:
        if all(ingredient.lower() in map(str.lower, ingredients_list) for ingredient in recipe_ingredients):
            print(food)
            found_food = True

    return found_food

def clear_ingredients_file():
    try:
        os.remove(INGREDIENTS_LIST_FILE_PATH)
        print('Ingredients file has been cleared successfully.')
    except FileNotFoundError:
        print('Ingredients file not found.')

def get_all_possible_ingredients():
    all_possible_ingredients = list(set(ingredient for recipe in recipes for ingredient in recipe[1]))
    return all_possible_ingredients

def main():
    while True:
        ingredients_list = load_ingredients_from_file()
        if not ingredients_list:
            print('Ingredients list is empty. Let\'s add some ingredients.')
            ingredients_list = add_ingredients_to_file()

        found_food = find_recipes(ingredients_list)

        choice = input('Press Enter to exit, enter "add" to add more ingredients, "clear" to clear the list, or "list" to view all ingredients: ')
        if choice.lower() == 'add':
            ingredients_list = add_ingredients_to_file()
        elif choice.lower() == 'clear':
            clear_ingredients_file()
        elif choice.lower() == 'list':
            all_possible_ingredients = get_all_possible_ingredients()
            print('List of All Possible Ingredients:')
            for i, ingredient in enumerate(all_possible_ingredients, start=1):
                print(f"{i}. {ingredient}")
        else:
            if not found_food:
                print('Sorry, no recipes can be created.')
            sys.exit()

if __name__ == '__main__':
    main()