# The central storage for our active orders
order_queue = []

# Available products and prices
MENU = {
    "Espresso": 3.00,
    "Latte": 4.50,
    "Cappuccino": 4.00
}

print("QuickBrew System Initialized.")
def show_menu():
    print("\n--- QuickBrew Menu ---")
    for drink, price in MENU.items():
        print(f"{drink}: ${price:.2f}")