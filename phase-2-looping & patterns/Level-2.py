'''
Level-2
1. Count the number of digits in a given number.
2. Print the reverse of a given number.
3. Check if a number is a palindrome.
4. Find the sum of digits of a number.
5. Check if a number is an Armstrong number.
6. Check if a number is a perfect number.
7. Print all prime numbers between 1 and 100.
8. Check if a number is prime or not.
9. Print Fibonacci series up to n terms.
10. Print sum of first n terms of Fibonacci series.
'''

#1
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

#2
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print("Reverse of the number:", reverse)

#3
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

#4
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
    print("Sum of digits:", sum_digits)

#5
num = int(input("Enter a number: "))
original = num
sum_powers = 0
count = 0

# Count the number of digits
while num > 0:
    count += 1
    num //= 10

# Calculate the sum of powers
num = original
while num > 0:
    digit = num % 10
    sum_powers += digit ** count
    num //= 10

if sum_powers == original:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")


#6
num = int(input("Enter a number: "))
sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i
if sum_divisors == num:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")

#7
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


#8
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")

#9
n = int(input("Enter the number of terms: "))       
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#10
n = int(input("Enter the number of terms: "))
sum_fib = 0
a, b = 0, 1
for _ in range(n):
    sum_fib += a
    a, b = b, a + b
print("Sum of first", n, "terms of Fibonacci series:", sum_fib)