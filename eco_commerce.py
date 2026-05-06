class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display_product(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")


class ShoppingCard:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self, product_name):
        for item in self.products:
            if item.name == product_name:
                self.products.remove(item)
                print(f"{product_name} removed from cart")
                return
        print("Product not found")
   
    def show_cart(self):
        print("\n===== SHOPPING CART =====")
        if len(self.products) == 0:
            print("Cart is empty")
        else:
            for item in self.products:
                print(f"{item.name} - ₹{item.price}")

    def total_price(self):
        total = 0
        for item in self.products:
            total += item.price
        return total


class Coupon:
   def __init__(self):
   
class Order:
   def __init__(self):

class PaymentProcessor:
      def __init__(self):
          pass

class CreditCard(PaymentProcessor):

class PayPal(PaymentProcessor):

class crypto(PaymentProcessor):
