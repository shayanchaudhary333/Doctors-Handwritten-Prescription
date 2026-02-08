def calculate_grocery_total(amount):
    """Calculate total cost after discount if applicable"""
    if amount > 1000:
        amount *= 0.9  # Apply 10% discount
    return amount

def main():
    print("Grocery Store Discount Calculator")
    amount = float(input("Enter total amount of groceries: ₹"))
    total = calculate_grocery_total(amount)
    print(f"Final amount after discount (if any): ₹{total:.2f}")

if __name__ == "__main__":
    main()
