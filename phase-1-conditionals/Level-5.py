'''
Level-5

1. Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.
2. Take three numbers and check if they can form a Pythagorean triplet.
3. Take day and month and check if it forms a valid calendar date (ignoring leap years).
4. Take time (hours and minutes) and print the smaller angle between the hour and minute hands.
5. Take three numbers and check if they are in arithmetic progression.
6. Take three numbers and check if they are in geometric progression.
7. Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.
8. Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.
9. Take two dates (day and month) and determine which one comes first in the calendar.
10. Take a year and print the corresponding century (e.g., “19th century”, “20th century”, etc.).
'''

#1
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point lies on the Y-axis.")  
elif y == 0:
    print("The point lies on the X-axis.")
else:
    print("The point is in the coordinate plane.")  

#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("The numbers form a Pythagorean triplet.")
else:
    print("The numbers do not form a Pythagorean triplet.")

#3
day = int(input("Enter day: "))
month = int(input("Enter month: ")).lower()
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    if 1 <= day <= 31:
        print("Valid date.")
    else:
        print("Invalid date.")
elif month in ["april", "june", "september", "november"]:
    if 1 <= day <= 30:
        print("Valid date.")
    else:
        print("Invalid date.")
elif month == "february":
    if 1 <= day <= 28:
        print("Valid date.")
    else:
        print("Invalid date.")
else:
    print("Invalid month.")

#4
hours = int(input("Enter hours (0-23): "))
minutes = int(input("Enter minutes (0-59): "))
if 0 <= hours < 24 and 0 <= minutes < 60:
    hour_angle = (hours % 12) * 30 + (minutes / 60) * 30
    minute_angle = minutes * 6
    angle = abs(hour_angle - minute_angle)
    smaller_angle = min(angle, 360 - angle)
    print("The smaller angle between the hour and minute hands is:", smaller_angle, "degrees.")                                


#5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if b - a == c - b or a - b == b - c or c - a == a - b and a != 0 and b != 0 and c != 0:
    print("The numbers are in arithmetic progression.")
else:
    print("The numbers are not in arithmetic progression.")

#6
a = int(input("Enter first number: "))    
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (b/a == c/b or a/b == b/c  or c/a == a/c)and a != 0 and b != 0 and c != 0:
    print("The numbers are in geometric progression.")
else:
    print("The numbers are not in geometric progression.")

#7
num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    sum_of_digits = (num // 100) + ((num // 10) % 10) + (num % 10)
    product_of_digits = (num // 100) * ((num // 10) % 10) * (num % 10)
    if sum_of_digits > product_of_digits:
        print("The sum of the digits is greater than the product of the digits.")
    else:
        print("The sum of the digits is not greater than the product of the digits.")
else:
    print("Please enter a valid 3-digit number.")

#8
num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    first_digit = num // 100
    middle_digit = (num // 10) % 10
    last_digit = num % 10
    if first_digit + last_digit == middle_digit:
        print("The sum of the first and last digit equals the middle digit.")
    else:
        print("The sum of the first and last digit does not equal the middle digit.")

#9
months=["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
d1 = int(input("Enter first date (day): "))
m1=input("Enter first month").lower()
m1=months.index(m1)+1
d2 = int(input("Enter second date (day): "))
m2 = input("Enter second month:")
m2=months.index(m2)+1
if m1 < m2 or (m1 == m2 and d1 < d2):
    print("The first date comes before the second date.")
elif m1 > m2 or (m1 == m2 and d1 > d2):
    print("The second date comes before the first date.")        
else:
    print("The dates are the same.")

#10
year = int(input("Enter a year: "))
if year > 0:
    century = (year - 1) // 100 + 1
    suffix = "th"
    if century % 10 == 1 and century % 100 != 11:
        suffix = "st"
    elif century % 10 == 2 and century % 100 != 12:
        suffix = "nd"
    elif century % 10 == 3 and century % 100 != 13:
        suffix = "rd"
    print(f"The year {year} is in the {century}{suffix} century.")
    