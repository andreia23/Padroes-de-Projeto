from MealAbstract import Meal

class HamburgerMeal(Meal):
    def prepare_ingredients(self):
        print("Getting burgers, buns, and french fries")

    def cook(self):
        print("Cooking burgers on grill and fries in oven")

    def clean_up(self):
        print("Throwing away paper plates")
