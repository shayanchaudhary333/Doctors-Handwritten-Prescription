# atm_withdrawal_fee.py

def calculate_total_withdrawn(amount):
    """Calculate total withdrawn amount including ₹20 fee"""
    fee = 20
    total = amount + fee
    return total

def main():
    print("Welcome to the ATM Withdrawal Fee Calculator!")

    amount = float(input("Enter the amount you want to withdraw: "))
    total = calculate_total_withdrawn(amount)

    print(f"Total amount debited including fee: ₹{total:.2f}")

if __name__ == "__main__":
    main()
