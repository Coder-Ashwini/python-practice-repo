weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)
your_bmi = round(bmi, 2)
print(f"Your BMI is {your_bmi}")
if your_bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= your_bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= your_bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.") 
