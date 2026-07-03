#Level 1: Simple Conditions (Getting started)
#1. Take a number and print whether it’s positive, negative, or zero.
#2. Check if a number is even or odd.
#3. Check if a number is divisible by 5.
#4. Check if a number is divisible by both 3 and 5.
#5. Check if a given year is a leap year.
#6. Take two numbers and print the larger one.
#7. Take three numbers and print the largest.
#8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
#9. Take a character and check if it’s a vowel or consonant.
#10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special character.

#1
n = int(input("Enter a number: "))
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#2
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#3
n = int(input("Enter a number: "))
if n % 5 == 0:  
    print("The number is divisible by 5.") 
else:
    print("The number is not divisible by 5.")     
    
#4
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")    

#5    
n = int(input("Enter a year: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")    

#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"The larger number is: {a}")
elif b > a:
    print(f"The larger number is: {b}")
else:
    print("Both numbers are equal.")            

#7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"The largest number is: {a}")
elif b >= a and b >= c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")3

#8
T = float(input("Enter the temperature in Celsius: "))
if T < 10:
    print("Cold")  
elif 10 <= T < 25:
    print("Warm")    
else:
    print("Hot")  

#9
vowel = ['a', 'e', 'i', 'o', 'u']
char = input("Enter a character: ").lower()
if char in vowel:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

#10
char = input("Enter a character: ")
if char.isupper():
    print("The character is uppercase.")
elif char.islower():
    print("The character is lowercase.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")

