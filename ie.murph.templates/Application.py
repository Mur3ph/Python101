__author__ = 'Paul'
from cart import Cart
from product import Product

class App():

    def Main(self):
        prod_1 = Product("Bananas", 1.89, 6)
        prod_2 = Product("Milk", 5.99, 2)
        prod_3 = Product("Bread", 2.89, 1)

        cart_1 = Cart(prod_1)
        cart_2 = Cart(prod_2)
        cart_3 = Cart(prod_3)

        cart_1.add_to_cart()
        cart_2.add_to_cart()
        cart_3.add_to_cart()

        cart_1.create_template()
        cart_2.create_template()
        cart_3.create_template()


x = App()
if __name__ == "__main__":
    x.Main()


