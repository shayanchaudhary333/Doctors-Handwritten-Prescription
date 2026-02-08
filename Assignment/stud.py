# student_grade_calculator.py

def calculate_grade(m1, m2, m3):
    """Calculate grade based on average marks of 3 subjects"""
    average = (m1 + m2 + m3) / 3

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Welcome to the Student Grade Calculator!")

    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))

    grade = calculate_grade(m1, m2, m3)
    print(f"Your grade is: {grade}")

if _name_ == "_main_":
    main()