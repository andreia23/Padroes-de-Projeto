from ItemElement import ItemElement


class Fruit(ItemElement):
    def __init__(self, price, wt, nm):
        self.price = price
        self.weight = wt
        self.name = nm

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def accept(self, visitor):
        return visitor.visit(self)
