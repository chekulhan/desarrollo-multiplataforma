class Recipe:
    def __init__(self, name, ingredients, calories):
        self.name = name
        self.ingredients = ingredients
        self.calories = calories

    def __str__(self):
        return f"{self.name} ({self.calories} kcal): {', '.join(self.ingredients)}"


recipes = [
    Recipe("Pasta", ["noodles", "tomato", "cheese"], ),
    Recipe("Salad", ["lettuce", "tomato", "cucumber"], 200),
    Recipe("Burger", ["bun", "beef", "cheese"], 800),
]

# mostrar las recetas con menos calorias
low_calorie_recipes = list(filter(lambda r: r.calories <= 500, recipes)) 
low_calorie_recipes = [r for r in recipes if r.calories <= 500]

# Introducir recetas
# Preguntar al usuario y rellenar los objetos
name = input("Enter recipe name: ")
