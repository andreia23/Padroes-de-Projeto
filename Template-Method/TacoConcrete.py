from MealAbstract import Meal

class TacoMeal(Meal):
    def prepare_ingredients(self):
        print("Getting ground beef and shells")

    def cook(self):
        print("Cooking ground beef in pan")

    def eat(self):
        print("The tacos are tasty")

    def clean_up(self):
        print("Doing the dishes")

