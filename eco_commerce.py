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
    def __init__(self,code,discount_percent):
       self.code=code
       self.discount_percent=discount_percent

    def apply_discount(self, amount):
        discount = amount * (self.discount_percent / 100)
        return amount - discount


class PaymentProcessor:
      def __init__(self):
          pass

class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        print("\nProcessing Credit Card Payment...")
        print("Checking card details...")
        print(f"₹{amount} paid using Credit Card")

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        print("\nProcessing PayPal Payment...")
        print("Logging into PayPal account...")
        print(f"₹{amount} paid using PayPal")

class crypto(PaymentProcessor):
    def process_payment(self, amount):
        print("\nProcessing Crypto Payment...")
        print("Verifying blockchain transaction...")
        print(f"₹{amount} paid using Cryptocurrency")
   
class Order:
    def __init__(self, cart, payment_method):
        self.cart = cart
        self.payment_method = payment_method

    def place_order(self, coupon=None):
        total = self.cart.total_price()

        print("\n===== ORDER SUMMARY =====")
        print(f"Original Total: ₹{total}")

        if coupon:
            total = coupon.apply_discount(total)
            print(f"Coupon Applied: {coupon.code}")
            print(f"Discounted Total: ₹{total}")

        self.payment_method.process_payment(total)

        print("Order Placed Successfully!")

p1 = Product(101, "Laptop", 60000)
p2 = Product(102, "Headphones", 2000)
p3 = Product(103, "Mouse", 1000)

cart = ShoppingCard()


cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)


cart.show_cart()


coupon = Coupon("SAVE10", 10)


payment = crypto()

order = Order(cart, payment)


order.place_order(coupon)


