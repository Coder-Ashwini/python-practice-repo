weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)
your_bmi = round(bmi, 2)
print(f"Your BMI is {your_bmi}")