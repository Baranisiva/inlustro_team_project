# Simple E-Commerce Cart Simulator

# Sample product data (Product Name : Price)
product_data = {
    "laptop": 50000,
    "phone": 20000,
    "headphones": 1500,
    "keyboard": 700,
    "mouse": 400
}

# Cart to store items
cart = {}

def show_products():
    print("\nAvailable Products:")
    for product, price in product_data.items():
        print(f"- {product.title()} : ₹{price}")

def add_to_cart(product, quantity):
    if product in product_data:
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        print(f"{quantity} {product}(s) added to cart.")
    else:
        print("Product not found!")

def remove_from_cart(product):
    if product in cart:
        del cart[product]
        print(f"{product} removed from cart.")
    else:
        print("Product not in cart!")

def search_product(product):
    if product in product_data:
        print(f"{product.title()} is available at ₹{product_data[product]}")
    else:
        print(f"{product.title()} is not available.")

def view_cart():
    print("\nYour Cart:")
    if not cart:
        print("Cart is empty.")
    else:
        total = 0
        for product, qty in cart.items():
            price = product_data[product]
            subtotal = price * qty
            total += subtotal
            print(f"- {product.title()} x{qty} = ₹{subtotal}")
        print(f"Total Amount: ₹{total}")

# Menu
while True:
    print("\n==== E-Commerce Cart Menu ====")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. Search Product")
    print("5. View Cart")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        show_products()
    elif choice == '2':
        prod = input("Enter product name to add: ").lower()
        qty = int(input("Enter quantity: "))
        add_to_cart(prod, qty)
    elif choice == '3':
        prod = input("Enter product name to remove: ").lower()
        remove_from_cart(prod)
    elif choice == '4':
        prod = input("Enter product name to search: ").lower()
        search_product(prod)
    elif choice == '5':
        view_cart()
    elif choice == '6':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice! Try again.")