ALL_PRODUCTS = []
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        ALL_PRODUCTS.append(self)
class Cart:
    def __init__(self):
        self.items = {}
    def add_item(self, product):
        if product in self.items:
            self.items[product] += 1
        else:
            self.items[product] = 1
        print(f"{product.name} is added to cart")
    def show_cart(self):
        if not self.items:
            print("\nYour cart is empty!")
            return
        print("\n ============== YOUR CART ==============")
        print("SL - Product Name - Price - Quentity -Net  Price ")
        total = 0
        counter = 1
        for product in self.items:
            qty = self.items[product]
            net = product.price * qty
            total += net
            print(f"{counter}. {product.name} - {product.price} - {qty} - {net}")
            counter += 1
        print("------------------------------------------")
        print(f"Total: {total} TK")

def show_all_products():
    print("\n --------------- All Products List -----------------")
    print(f"SL NO. Product Name - Price ")
    counter = 1
    for product in ALL_PRODUCTS:
        print(f"{counter}. {product.name} - {product.price} TK ")
        counter += 1
    print("\n --------------- End Products List -----------------")

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1200)
p3 = Product("Keyboard", 2500)
my_cart = Cart()

while True:
    print("\n ---------------- E-commerce Menu ------------------ ")
    print("1. Add To Cart")
    print("2. Show Cart")
    print("99. Exit ")
    choice = input("Enter your choice: ")
    if choice == '99' :
        break
    elif choice == '1':
        show_all_products()
        try:
            pchoice = int(input("Enter your choice: "))
            if 1<= pchoice <= len(ALL_PRODUCTS):
                selectedproduct = ALL_PRODUCTS[pchoice - 1]
                my_cart.add_item(selectedproduct)
            else:
                print("Invalid product number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    elif choice == '2':
        my_cart.show_cart()

    