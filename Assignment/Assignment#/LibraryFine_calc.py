# library_fine_calculator.py

def calculate_fine(days_late):
    """Calculate fine for late book returns"""
    fine_per_day = 5  # rupees
    fine = days_late * fine_per_day
    return fine

def main():
    print("Welcome to the Library Fine Calculator!")

    days_late = int(input("Enter number of days the book is overdue: "))
    fine = calculate_fine(days_late)

    print(f"Total fine: ₹{fine} rupees")

if __name__ == "__main__":
    main()
