from Book import Book
from Fruit import Fruit
from ShoppingCartVisitor import ShoppingCartVisitor


class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit(self, item):
        if isinstance(item, Book):
            cost = 0
            #apply 5$ discount if book price is greater than 50
            if item.get_price() > 50:
                cost = item.get_price() - 5
            else:
                cost = item.get_price()
            print("Book ISBN:: {} cost = {}".format(item.get_isbn(), cost))
            return cost
        elif isinstance(item, Fruit):
            cost = item.get_price() * item.get_weight()
            print("{} cost = {}".format(item.get_name(), cost))
            return cost