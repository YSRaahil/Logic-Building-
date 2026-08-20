'''Level 2: Number-based Recursive Thinking 
1.	Count the number of digits in a number recursively. 
2.	Reverse a number recursively
3.	Check if a number is a palindrome using recursion. 
4.	Find product of digits of a number recursively. 
5.	Find GCD (HCF) of two numbers using Euclid’s algorithm recursively. 
6.	Convert a number to binary recursively. 
7.	Print digits of a number in words recursively (e.g., 123 → “one two three”). 
8.	Calculate the sum of first n even numbers recursively. 
9.	Calculate the sum of first n odd numbers recursively. 
10.	Find nCr (Combination formula) recursively using Pascal’s relation. 
'''
#1
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

#2
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)   

#3
def is_palindrome(n):
    def helper(n, rev=0):
        if n == 0:
            return rev
        else:
            return helper(n // 10, rev * 10 + n % 10)
    
    return n == helper(n)   

#4
def product_of_digits(n):
    if n == 0:
        return 1
    else:
        return (n % 10) * product_of_digits(n // 10)

#5                   
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)    

#6
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)   

#7
def digits_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if n == 0:
        return ""
    else:
        return digits_to_words(n // 10) + words[n % 10] + " "   

#8
def sum_of_first_n_even(n):
    if n == 0:
        return 0
    else:
        return 2 * n + sum_of_first_n_even(n - 1)

#9
def sum_of_first_n_odd(n):
    if n == 0:
        return 0
    else:
        return (2 * n - 1) + sum_of_first_n_odd(n - 1)  

#10
def nCr(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)                    