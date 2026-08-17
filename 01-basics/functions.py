
#Refactor your BMI calculator into a function calculate_bmi(weight, height) that returns the BMI value. Call it and print the result.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi} ({bmi_category(bmi)})")


#Refactor FizzBuzz into a function fizzbuzz(n) that returns "Fizz", "Buzz", "FizzBuzz", or the number itself (as a string) — don't print inside the function, return the value. Then loop from 1 to 50 and print fizzbuzz(i) for each.
def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)

print(fizzbuzz(12))

#Write is_even(number) that returns True or False (a boolean) instead of printing text.
def is_even(num):
    return num % 2 == 0

print(is_even(50))

#Write factorial(n) that calculates n! (n × (n-1) × (n-2) × ... × 1) using a loop. E.g., factorial(5) should return 120.
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

print(factorial(5))  # print when you CALL it, not inside the function


#Write is_prime(n) that returns True if n is a prime number, False otherwise. (Hint: check if any number from 2 to n-1 divides evenly into n.)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if is_prime(71):
    print("The number is prime")
else:
    print("The number is not prime")

#Challenge — temperature converter: Write two functions, celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f). Formula: F = C * 9/5 + 32.

def celsius_to_fahrenheit(c):
    F = c * 9/5 + 32
    return F

print(celsius_to_fahrenheit(72))

#def fahrenheit_to_celsius(f):
