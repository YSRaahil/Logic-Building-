'''
Level-4
1. Take a character and check if it is a letter, a digit, or neither.
2. Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both.
3. Take three numbers and print the median value (neither maximum nor minimum).
4. Take 24-hour time (hours and minutes) and print whether it is AM or PM.
5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L).
6. Take two numbers and check if both are positive and their sum is less than 100.
7. Take a single digit (0–9) and print its word form (“Zero” to “Nine”).
8. Take a weekday number (1–7) and determine if it is a weekday or weekend.
9. Take electricity units consumed and calculate the bill as per slabs (using if-else).
10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit)'''

#1
char = input("Enter a character: ")
if char.isalpha():
    print("It is a letter.")
elif char.isdigit():
    print("It is a digit.")
else:
    print("It is neither a letter nor a digit.")

#2
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by 3 or 5.")

#3
numbers = [int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))]
median = a+b+c - max(numbers) - min(numbers)
print("The median value is:", median)

#4
hours = int(input("Enter hours (24-hour format): "))
if 0 <= hours < 24:
    if hours < 12:
        print("AM")
    else:
        print("PM")

#5
age = int(input("Enter your age: "))
income = float(input("Enter your income in lakhs: "))
if age > 18 and income > 500000:
    print("Eligible for tax.")
else:
    print("Not eligible for tax.")

#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > 0 and b > 0 and (a + b) < 100:
    print("Both numbers are positive and their sum is less than 100.")  

#7
digit = int(input("Enter a single digit (0-9): "))
digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
if 0 <= digit <= 9:
    print("The word form is:", digit_words[digit])      

#8
weekday = int(input("Enter a weekday number (1-7): "))  
if 1 <= weekday <= 7:
    if weekday in [6, 7]:
        print("It is a weekend.")
    else:
        print("It is a weekday.")

#9
units = float(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10            
print("The electricity bill is:", bill)

#10
password = input("Enter a password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long and contain at least one digit.")