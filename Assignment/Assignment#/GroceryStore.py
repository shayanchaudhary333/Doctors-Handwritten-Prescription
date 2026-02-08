def calculate_total_bill(amount):
    if amount > 1000:
        discount = 0.10 *amount      # if the user/person buy's aabove 1,000 then aapply 10% discount...!!!!
        final_amount = amount - discount
    else:
        final_amount = amount    # if not then check out the bill....!!!
    return final_amount


# Taking input from user 
total = float(input("Enter total grocery amount: ₹"))

# Final payable amount from user......!!1
final_total = calculate_total_bill(total)
print(f"Final amount to pay: ₹{final_total:.2f}")