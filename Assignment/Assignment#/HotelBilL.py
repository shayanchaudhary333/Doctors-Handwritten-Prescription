def hotel_bill(nights, rate_per_night):
    amount = nights * rate_per_night
    if nights > 5:
        amount -= amount * 0.1  # This Line gives you Discount of 10%...!! 
    return amount


# Taking Input from the person...!!!
nights = int(input(" How many nights will you stay ? :-  "))
rate_per_night = int(input("Enter the rate of 1 night"))

total_amount = hotel_bill(nights,rate_per_night)
print(f"Your total hotel bill is: ₹{total_amount}")
