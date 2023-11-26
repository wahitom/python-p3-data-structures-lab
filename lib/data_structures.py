spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    new_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            new_list.append(food)
    return new_list

def print_spicy_foods(spicy_foods):
    #new_list_emojis = []
    for food in spicy_foods:
        heat_level = food['heat_level']
        emoji = '🌶' * heat_level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None 

def print_spiciest_foods(spicy_foods):
    new_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level = food['heat_level']
            emoji = '🌶' * heat_level
            new_foods = f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji}"
            new_list.append(new_foods)
    print(new_list)

def get_average_heat_level(spicy_foods):
    total_num = 0
    num_spicy_foods = len(spicy_foods)
    for food in spicy_foods: 
        heat_level = food['heat_level']
        total_num += heat_level

    if num_spicy_foods > 0:
        average_heat = total_num / num_spicy_foods
        return average_heat
    else: 
        return 0

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = {
        'name': spicy_food['name'],
        'cuisine': spicy_food['cuisine'],
        'heat_level': spicy_food['heat_level']
    }

    spicy_foods.append(new_spicy_food)
    return spicy_foods

