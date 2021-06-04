from ItemElement import ItemElement


class Book(ItemElement):
    def __init__(self, cost, isbn):
        self.price = cost
        self.isbn = isbn

    def get_price(self):
        return self.price

    def get_isbn(self):
        return self.isbn

    def accept(self, visitor):
        return visitor.visit(self)