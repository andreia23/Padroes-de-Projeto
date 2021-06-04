from Book import Book
from Fruit import Fruit
from ShoppingCartVisitorImpl import ShoppingCartVisitorImpl


def calculate_price(items):
    visitor = ShoppingCartVisitorImpl()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum

if __name__ == '__main__':
    items = [
        Book(20, "1234"),
        Book(100, "5678"),
        Fruit(10, 2, "Banana"),
        Fruit(5, 5, "Apple")
    ]

    total = calculate_price(items)
    print("Total Cost = {}".format(total))