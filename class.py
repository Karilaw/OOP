class Item:
    pay_rate = 0.8
    all = []
    # This is like java constructer, You are passing attributes of this objects dynamically

    def __init__(self, name: str, price, quantity):
        self.price = price
        self.quatity = quantity
        self.name = name

        # Actions to execute
        Item.all.append(self)

        # self parameter is used to refer to the instance of the class and to access its attributes and methods.

    def calcutate_total_cost(self):
        return self.price * self.quatity

    def apply_discount(self):
        return self.price * self.pay_rate * self.quatity

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.price}, {self.quatity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
