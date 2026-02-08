# taxi_fare_calculator.py

def calculate_fare(distance):
    """Calculate taxi fare based on distance"""
    if distance <= 1:
        return 10
    else:
        return 10 + (distance - 1) * 5

def main():
    print("Welcome to the Taxi Fare Calculator!")

    distance = float(input("Enter distance travelled (in km): "))
    fare = calculate_fare(distance)

    print(f"Total fare: ₹{fare:.2f}")

if __name__ == "__main__":
    main()
