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
def take_order(customer_name, drink_choice):
    if drink_choice in MENU:
        order = {"customer": customer_name, "drink": drink_choice, "status": "Brewing"}
        order_queue.append(order)
        print(f"Order placed for {customer_name}!")
    else:
        print("Sorry, we don't serve that.")
def view_queue():
    if not order_queue:
        print("Queue is empty. Time to clean the counters!")
        return
    
    print("\n--- Current Orders ---")
    for index, order in enumerate(order_queue, 1):
        print(f"{index}. {order['customer']} - {order['drink']} [{order['status']}]")