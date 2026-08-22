'''Pattern & Printing Problems
Print a line of n stars recursively. 
Print a square of stars recursively (n×n). 
Print a triangle of stars recursively (top-down). 
Print a triangle of stars recursively (bottom-up). 
5.	Print pattern of numbers recursively (1 to n each row). 
6.	Print reverse triangle pattern recursively. 
7.	Print multiplication table of n recursively. 
8.	Print numbers in increasing and decreasing order in same function. 
9.	Print sum of series 1 + 2 + 3 + ... + n recursively and display each step. 
10.	Print pattern of characters (A, AB, ABC, ...) recursively.'''

#1
def print_line_of_stars(n):
    if n == 0:
        return
    print("*", end="")
    print_line_of_stars(n - 1)

#2
def print_square_of_stars(n, i=0):
    if i == n:
        return
    print_line_of_stars(n)
    print()
    print_square_of_stars(n, i + 1) 

#3
def print_triangle_top_down(n, i=0):
    if i == n:
        return
    print_line_of_stars(i + 1)
    print()
    print_triangle_top_down(n, i + 1)   

#4
def print_triangle_bottom_up(n, i=0):
    if i == n:
        return
    print_triangle_bottom_up(n, i + 1)
    print_line_of_stars(i + 1)
    print() 

#5
def print_number_pattern(n, i=1):
    if i > n:
        return
    for j in range(1, i + 1):
        print(j, end="")
    print()
    print_number_pattern(n, i + 1)  

#6
def print_reverse_triangle(n, i=0):
    if i == n:
        return
    print_line_of_stars(n - i)
    print()
    print_reverse_triangle(n, i + 1)

#7
def print_multiplication_table(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n * i}")
    print_multiplication_table(n, i + 1)

#8
def print_increasing_decreasing(n, i=1):
    if i > n:
        return
    print(i, end=" ")
    print_increasing_decreasing(n, i + 1)
    print(i, end=" ")   

#9
def print_sum_series(n, i=1, total=0):  
    if i > n:
        print(f"Sum: {total}")
        return
    total += i
    print(f"Adding {i}, Total so far: {total}")
    print_sum_series(n, i + 1, total)

#10
def print_character_pattern(n, i=0):
    if i == n:
        return
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()
    print_character_pattern(n, i + 1)   

