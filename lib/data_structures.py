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
    return[d.get("name") for d in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[d for d in spicy_foods if d.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    for d in spicy_foods:
        print(f'{d["name"]} ({d["cuisine"]}) | Heat Level: {"🌶" * d["heat_level"]}')
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for d in spicy_foods:
        if d["cuisine"] == cuisine:
            return d

def print_spiciest_foods(spicy_foods):
    return print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total = 0
    for d in spicy_foods:
        total+=d["heat_level"]
    return total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
