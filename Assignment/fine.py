def create_product(name, price):
    """Create a product"""
    return {"name": name, "price": price}

def add_product(cart, product):
    """Add a product to the cart"""
    cart.append(product)

def remove_product(cart, product_name):
    """Remove a product from the cart"""
    return [product for product in cart if product["name"] != product_name]

def calculate_total(cart):
    """Calculate the total cost of the cart"""
    return sum(product["price"] for product in cart)

def display_cart(cart):
    """Display the contents of the cart"""
    print("Your Cart:")
    for product in cart:
        print(f"{product['name']}: {product['price']:.2f} rupees")
    print(f"Total: {calculate_total(cart):.2f} rupees")

def calculate_fine(days_late):
    """Calculate library fine based on days overdue"""
    fine_per_day = 5
    return days_late * fine_per_day

def main():
    cart = []

    while True:
        print("\nOptions:")
        print("1. Add product")
        print("2. Remove product")
        print("3. Display cart")
        print("4. Calculate Library Fine")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product = create_product(name, price)
            add_product(cart, product)
        elif choice == "2":
            name = input("Enter product name to remove: ")
            cart = remove_product(cart, name)
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            days = int(input("Enter number of days book is overdue: "))
            fine = calculate_fine(days)
            print(f"The total fine is: ₹{fine}")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
