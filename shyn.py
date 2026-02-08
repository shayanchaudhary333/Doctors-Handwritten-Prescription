#BMI calculator
weight = float(input("Enter your weight i kg: "))
height = float(input("Enter your height in meters:"))
bmi = weight / (height ** 2)
print("Your BMI is:",bmi)
if bmi <18.4:
   print("Underweight")
elif 18.5 <= bmi < 24.9:
   print("Normal weight")
elif 25 <= bmi < 29.9:
   print("Overweight")
elif  bmi >= 30:
   print("Obesity")

   