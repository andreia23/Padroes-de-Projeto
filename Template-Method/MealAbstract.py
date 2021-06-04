from abc import ABC, abstractmethod

class Meal(ABC):

    # template method
    def do_meal(self):
        self.prepare_ingredients()
        self.cook()
        self.eat()
        self.clean_up()

    def eat(self):
        print("Mmm, that's good")

    @abstractmethod
    def prepare_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass

