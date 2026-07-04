#Level 2: Nested If & Multiple Conditions
#1. Take three sides and check if they form a valid triangle.
#2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.
#3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).
#4. Check if one of two given numbers is a multiple of the other.
#5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.
#6. Check voting eligibility for a given age (18+).
#7. Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.
#8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.
#9. Take a day number (1–7) and print the corresponding day name.
#10. Take a month number (1–12) and print the corresponding month name.

#1&#2
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid triangle.")
    if a == b == c:
        print("It is an equilateral triangle.")
    elif a == b or b == c or a == c:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")

#3
marks = float(input("Enter your marks (0-100): "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
elif 60 <= marks < 70:
    print("Grade: D")
else:
    print("Grade: F")

#4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    print("The first number is a multiple of the second number.")
elif num2 % num1 == 0:
    print("The second number is a multiple of the first number.")
else:
    print("Neither number is a multiple of the other.")

#5
hour = int(input("Enter the hour of the day (0-23): "))
if 0 <= hour < 12:  
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")
                
#6
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#7
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")

#8
char = input("Enter an alphabet character: ").lower()
if 'a' <= char <= 'm':
    print("The character lies between 'a' and 'm'.")
elif 'n' <= char <= 'z':
    print("The character lies between 'n' and 'z'.")
else:
    print("Invalid input. Please enter a valid alphabet character.")

#9
day_number = int(input("Enter a day number (1-7): "))
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")     
elif day_number == 3:
    print("Wednesday")           
elif day_number == 4:  
    print("Thursday")
elif day_number == 5:   
    print("Friday") 
elif day_number == 6:   
    print("Saturday")       
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")  

#10
month_number = int(input("Enter a month number (1-12): "))
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")        
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")                                
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")            