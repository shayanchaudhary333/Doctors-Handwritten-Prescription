def atm_withdrawal(amount):
    """Calculate total withdrawal including ₹20 ATM fee."""
    fee = 20
    total = amount + fee
    return total

# Example usage
withdrawal = int(input("Enter the amount you want to withdraw: ₹"))
total_amount = atm_withdrawal(withdrawal)
print(f"Total amount deducted including ATM fee: ₹{total_amount}")