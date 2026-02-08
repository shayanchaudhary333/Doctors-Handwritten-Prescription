# bank_interest_calculator.py

def calculate_interest(principal, rate, time):
    """Calculate simple interest"""
    interest = (principal * rate * time) / 100
    return interest

def main():
    print("Welcome to the Bank Interest Calculator!")

    principal = float(input("Enter the principal amount (₹): "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (in years): "))

    interest = calculate_interest(principal, rate, time)
    print(f"Simple Interest: ₹{interest:.2f}")

if __name__ == "__main__":
    main()
