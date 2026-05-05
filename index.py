from abc import ABC, abstractmethod
ALL_PRODUCTS = []
# 1. Abstraction: Blueprint for products
class BaseProduct(ABC):
    @abstractmethod
    def display_info(self):
        pass
# 2. Encapsulation: Private __price and public property access
class Product(BaseProduct):
    def __init__(self, name, price):
        self.name = name
        self.__price = price # Private attribute
        ALL_PRODUCTS.append(self)
    @property
    def price(self):
        return self.__price 
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
    # 3. Polymorphism: Shared method name with unique behavior
    def display_info(self):
        return f"{self.name} - {self.price} TK"
# 4. Inheritance: WarrantyProduct inherits from Product
class WarrantyProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def display_info(self): # Method Overriding
        return f"{self.name} ({self.warranty}y Warranty) - {self.price} TK"
def show_all_products():
    if not ALL_PRODUCTS:
        print("\nInventory empty.")
        return False
    print("\n--- Products ---")
    for i, p in enumerate(ALL_PRODUCTS, 1):
        print(f"{i}. {p.display_info()}")
    return True
class Cart:
    def __init__(self):
        self.items = {}
    def add_item(self, product):
        self.items[product] = self.items.get(product, 0) + 1
        print(f"{product.name} added.")
    def show_cart(self):
        if not self.items:
            print("\nCart empty.")
            return False
        total = 0
        print("\n--- Cart ---")
        for p, qty in self.items.items():
            net = p.price * qty
            total += net
            print(f"{p.name} x{qty} = {net} TK")
        print(f"Total: {total} TK")
        return True
    def checkout(self):
        if self.show_cart():
            if input("\nCheckout? (y/n): ").lower() == 'y':
                print("Order processed. Thank you!")
                self.items = {}
def admin_menu():
    while True:
        print("\n--- Admin ---")
        print("1. Add Regular\n2. Add Warranty\n4. Update\n5. Delete\n99. Exit")
        c = input("Choice: ")
        if c == '1': Product(input("Name: "), float(input("Price: ")))
        elif c == '2': WarrantyProduct(input("Name: "), float(input("Price: ")), int(input("Warranty: ")))
        elif c in ['4', '5']:
            if show_all_products():
                idx = int(input("Index: ")) - 1
                if c == '4': ALL_PRODUCTS[idx].price = float(input("Price: "))
                else: ALL_PRODUCTS.pop(idx)
        elif c == '99': break
def customer_menu():
    cart = Cart()
    while True:
        print("\n--- Store ---")
        print("1. Browse\n2. Cart\n3. Checkout\n99. Exit")
        c = input("Choice: ")
        if c == '1':
            if show_all_products():
                cart.add_item(ALL_PRODUCTS[int(input("Index: ")) - 1])
        elif c == '2': cart.show_cart()
        elif c == '3': cart.checkout()
        elif c == '99': break
Product("Laptop", 50000)
WarrantyProduct("Neural Chip", 25000, "1")
while True:
    print("\n" + "===== E-commerce Menu =====")
    print("1. Admin\n2. Customer\n99. Exit")
    role = input("Access: ")
    if role == '1': admin_menu()
    elif role == '2': customer_menu()
    elif role == '99': break