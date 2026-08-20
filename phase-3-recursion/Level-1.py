'''🟢 Level 1: Foundation of Recursion (Base + Recursive Case) 
1.	Print numbers from 1 to n using recursion. 
2.	Print numbers from n down to 1 using recursion. 
3.	Print only even numbers from 1 to n recursively. 
4.	Print only odd numbers from 1 to n recursively. 
5.	Print sum of first n natural numbers recursively. 
6.	Print factorial of a number recursively. 
7.	Calculate power of a number (xⁿ) using recursion. 
8.	Find nth Fibonacci number recursively. 
9.	Print Fibonacci series up to n terms recursively. 
10.	Find sum of digits of a number recursively. 
'''

#1
def print_numbers_1_to_n(n):
    if n > 0:
        print_numbers_1_to_n(n - 1)
        print(n)

print_numbers_1_to_n(5)  # Example usage  

#2
def print_numbers_n_to_1(n):
    if n > 0:
        print(n)
        print_numbers_n_to_1(n - 1)

print_numbers_n_to_1(5)  # Example usage  

#3
def print_even_numbers_1_to_n(n):
    if n > 0:
        print_even_numbers_1_to_n(n - 1)
        if n % 2 == 0:
            print(n)

print_even_numbers_1_to_n(5)  # Example usage  

#4
def print_odd_numbers_1_to_n(n):
    if n > 0:
        print_odd_numbers_1_to_n(n - 1)
        if n % 2 != 0:
            print(n)

#5
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


#6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#7
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

#8
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

#9
def fibonacci_series(n, a=0, b=1):
    if n > 0:
        print(a)
        fibonacci_series(n - 1, b, a + b)   

#10
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)                                                  