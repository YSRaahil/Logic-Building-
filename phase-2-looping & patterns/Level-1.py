'''
Level-1
1. Print numbers from 1 to 10.
2. Print all even numbers between 1 and 100.
3. Print all odd numbers between 1 and 100.
4. Print numbers from 10 down to 1.
5. Print the table of a given number (n × 1 to n × 10).
6. Print the sum of first n natural numbers.
7. Print the sum of all even numbers up to n.
8. Print the sum of all odd numbers up to n.
9. Print the factorial of a given number.
10. Print the product of digits of a given number

'''
#1
for i in range(1, 11):
    print(i)

#2
for i in range(2, 101, 2):
    print(i)

#3
for i in range(1, 101, 2):  
    print(i)

#4
for i in range(10, 0, -1):
    print(i)

#5
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

#6
n = int(input("Enter a number: "))
sum_natural = sum(range(1, n + 1))
print("The sum of first", n, "natural numbers is:", sum_natural)

#7
n = int(input("Enter a number: "))
sum_even = sum(i for i in range(2, n + 1, 2))
print("The sum of all even numbers up to", n, "is:", sum_even)

#8
n = int(input("Enter a number: "))
sum_odd = sum(i for i in range(1, n + 1, 2))
print("The sum of all odd numbers up to", n, "is:", sum_odd)

#9
n = int(input("Enter a number: "))  
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)

#10
num = int(input("Enter a number: "))
product = 1
for digit in str(num):
    product *= int(digit)
print("The product of digits of", num, "is:", product)


