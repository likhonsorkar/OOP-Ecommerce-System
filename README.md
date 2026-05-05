# OOP E-Commerce System

![Application Screenshot](https://github.com/likhonsorkar/OOP-Ecommerce-System/blob/main/img/screenshot.PNG)

*Note: Please run the app, take a screenshot, and save it as `screenshot.png` inside the `img/` folder to display it here.*

This project is a terminal-based E-commerce application that demonstrates the core principles of **Object-Oriented Programming (OOP)** 
## 🚀 Key Features

### 🛒 Customer Experience
- **Browse Inventory:** View real-time product availability.
- **Add to Cart:** Select items to build a shopping cart.
- **Checkout:** Finalize orders.

### 🛠️ Admin Management
- **Add Products:** Support for regular and warranty-backed items.
- **Update Inventory:** Dynamically modify product prices.
- **Delete Products:** Remove items from the store inventory.

## 🏗️ OOP Concepts Demonstrated

The application is structured using four fundamental OOP pillars:

1.  **Abstraction:** Uses the `BaseProduct` abstract class (from `abc.ABC`) to define a blueprint that ensures all products implement a `display_info` method.
2.  **Encapsulation:** Protects sensitive data like product prices using private attributes (`__price`) and provides controlled access through `@property` getters and setters.
3.  **Inheritance:** The `WarrantyProduct` class inherits from the base `Product` class, extending its functionality while reusing existing code.
4.  **Polymorphism:** Demonstrates method overriding where different product types (Regular vs. Warranty) use the same `display_info` method call but output uniquely formatted details.


## 💻 How to Run
Ensure you have Python installed, then execute:
```bash
python index.py
```

## 🛠️ Usage
1.  **Select Role:** Choose between Admin (1) or Customer (2).
2.  **Admin:** Add your inventory first to see the system in action.
3.  **Customer:** Browse products, add them to your cart, and proceed to checkout.
