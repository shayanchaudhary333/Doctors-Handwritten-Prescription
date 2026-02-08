def calculate_bill(units):
    #Calculate electricity bill based on units consumed"""
    if units <= 100:
        return units * 7
    else:
        return (100 * 2) + ((units - 100) * 3)

def main():
    print("Welcome to the Electricity Bill Calculator!")

    units = int(input("Enter number of units consumed: "))
    bill = calculate_bill(units)

    print(f"Total electricity bill: ₹{bill}")

if __name__ == "_main_":
     main()