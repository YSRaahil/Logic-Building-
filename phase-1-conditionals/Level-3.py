'''
Level-3
1. Take a 3-digit number and check if all digits are distinct.
2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.
3. Take a 4-digit number and check if the first and last digits are equal.
4. Check whether a given integer is single-digit, double-digit, or multi-digit.
5. Check if a number is a multiple of 7 or ends with 7.
6. Take coordinates (x, y) and determine which quadrant the point lies in.
7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
8. Check if a number lies within the range [100, 999].
9. Take two angles of a triangle and compute the third angle.
10. Check whether a number is a perfect square (without using the square root function).'''

#1
number = int(input("Enter a 3-digit number: "))
if 100 <= number <= 999:
    digits = str(number)
    if len(set(digits)) == 3:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")
        

#2
number = int(input("Enter a 3-digit number: "))
if 100 <= number <= 999:
    digits = [int(d) for d in str(number)]
    middle_digit = digits[1]
    if middle_digit > digits[0] and middle_digit > digits[2]:
        print("The middle digit is the largest.")
    elif middle_digit < digits[0] and middle_digit < digits[2]:
        print("The middle digit is the smallest.")
    else:
        print("The middle digit is neither the largest nor the smallest.")


#3
number = int(input("Enter a 4-digit number: "))
if 1000 <= number <= 9999:
    digits = str(number)
    if digits[0] == digits[-1]:
        print("The first and last digits are equal.")
    else:
        print("The first and last digits are not equal.")
        

#4
integer = int(input("Enter an integer: "))
if -9 <= integer <= 9:  
    print("The number is a single-digit integer.")
elif -99 <= integer <= 99:
    print("The number is a double-digit integer.")
else:
    print("The number is a multi-digit integer.")

#5
number = int(input("Enter a number: "))
if number % 7 == 0 or str(number).endswith('7'):
    print("The number is a multiple of 7 or ends with 7.")

#6
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the first quadrant.")  
elif x < 0 and y > 0:
    print("The point lies in the second quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the third quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the fourth quadrant.") 
else:
    print("The point lies on an axis or at the origin.")


#7
amount = int(input("Enter the amount: "))
if amount % 2000 == 0 and amount % 500 == 0 and amount % 100 == 0:
    print("The amount can be evenly divided into 2000, 500, and 100 currency notes.")

#8
number = (input("Enter a number: "))
if 100 <= number <= 999:
    print("The number lies within the range [100, 999].")    

#9
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = 180 - (angle1 + angle2)
if angle3 > 0:  
    print(f"The third angle of the triangle is: {angle3} degrees.")

#10
number = int(input("Enter a number: "))
if number == int(number ** 0.5) ** 2:
    print("The number is a perfect square.")