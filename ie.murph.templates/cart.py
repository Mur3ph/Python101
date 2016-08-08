__author__ = 'Paul'
from string import Template
from product import Product

class Cart(Product):

    def __init__(self, Product):
        self.cart = []
        self.Product = Product

    def add_to_cart(self):
        self.cart.append(dict(item=self.Product.name, price=self.Product.price, qty=self.Product.quantity))

    def create_template(self):
        t = Template("$qty x $item = $price")
        total = 0
        print("Cart")
        for data in self.cart:
            print(t.substitute(data))
            total += data["price"]
        print("Total: ", str(total))

