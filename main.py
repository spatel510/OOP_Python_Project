from re import I

class Item:
    def __init__(self, name):
        print(f"{name}")
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone")

item1.price = 100
item1.quantity = 5
item1.total_price = item1.calculate_total_price(item1.price, item1.quantity)
print(item1.total_price)

item2 = Item("Laptop")

item2.price = 1000
item2.quantity = 3