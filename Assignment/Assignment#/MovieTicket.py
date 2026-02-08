# movie_ticket_booking.py

def calculate_total_cost(tickets, price_per_ticket):
    """Calculate total cost with 10% discount if tickets > 5"""
    total = tickets * price_per_ticket
    if tickets > 5:
        discount = total * 0.10
        total = total - discount
    return total

def main():
    print("Welcome to the Movie Ticket Booking System!")

    tickets = int(input("Enter number of tickets: "))
    price = float(input("Enter price per ticket: "))

    total_cost = calculate_total_cost(tickets, price)

    print(f"Total cost: ₹{total_cost:.2f}")

if __name__ == "__main__":
    main()
