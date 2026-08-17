#Print 1 to 20 using a for loop with range().

for i in range (21):
    print(i, end = " ")


print()
#Sum of numbers: Calculate the sum of all numbers from 1 to 100 using a loop (don't hardcode the formula — practice the loop).
sum = 0
for i in range(101):
    sum = sum+i
print(f"Total sum: {sum}")
print()
#Multiplication table: Take a number as input, print its multiplication table from 1 to 10 (e.g., 5 x 1 = 5, 5 x 2 = 10, ...).
Num = int(input("Enter a number: "))
for i in range(1,11):
    print (f" {i} * {Num} = {i*Num}")

print()

#FizzBuzz, but for a range: Loop from 1 to 50, applying the FizzBuzz logic (from the conditionals exercise) to every number in the range. This combines loops + conditionals — a very common real pattern.
for i in range(1,51):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    if i%5 == 0:
        print("Fizz")
    if i%3==0:
        print("Buzz")
#Countdown with while: Take a starting number, count down to 0 using a while loop, then print "Liftoff!" at the end.
num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num-=1
print("Liftoff!")
print()

#Challenge — password attempts: Simulate a login: use a while loop that keeps asking for a password (input()) until the user enters "python123" correctly, or until they've tried 3 times (whichever comes first). Use break and a counter.
password = "python123"
count = 0
while count <= 3: 
   u_pass = str(input("Enter a password: "))
   if password != u_pass:
        print("You have entered the wrong password")
        count+=1
   else:
       print("You have successfully loged in")
       break
   
       
