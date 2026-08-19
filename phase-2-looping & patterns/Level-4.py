'''Logical Loop Combinations
1.Print all numbers whose sum of digits is even (1–100). 
2.Count how many numbers between 1–500 are divisible by 7 but not by 5. 
3.Print all numbers that are palindromes between 1–500. 
4.Print numbers between 1–100 whose digits add up to a multiple of 3. 
5.	Find the smallest and largest digit in a given number. 
6.	Print all numbers from 1–n whose binary representation has an even number of 1s. 
7.	Print a pattern where each row i prints i*i. 
8.	Print factorial of each number from 1 to n. 
9.	Print the sum of all odd digits and even digits separately in a number. 
10.Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered.
'''

#1
'''for i in range(1,101):
    temp=i
    sum=0
    while (i>0):
        digit = i%10
        d_sum=d_sum+digit
        i=i//10
    if(d_sum %2 == 0):
        print(temp)    '''

#2
'''count = 0
for i in range(1,501):
    if(i%7==0 and i%5!=0):
        count+=1'''


#3
'''for i in range(1,500):
    rev=0
    temp=i
    while(i>0):
        digit=i%10
        rev=rev*10+digit
        i=i//10
    if(temp==rev):
        print(temp)    '''

#4
for i in range(1,100):
    d_sum=0
    temp=i
    while(i>0):
        digit=i%10
        d_sum+=digit
        i=i//10
    if d_sum%3==0:
        print(temp)            


#5
'''digit=[]
n = int(input("Enter a number:"))
while n>0:
    digit.append(n%10)
    n=n//10

print(min(digit),max(digit))) '''   

#6
n = int(input("Enter n: "))

for i in range(1, n + 1):
    temp = i
    count = 0

    while temp > 0:
        digit = temp % 2

        if digit == 1:
            count += 1

        temp = temp // 2

    if count % 2 == 0:
        print(i)


#7
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i * i)



#8
n = int(input("Enter n-value:"))
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)    


#9
even_digit=0
odd_digit=0
n = int(input("Enter the number:"))
while n>0:
    digit=n%10
    if digit%2==0:
        even_digit+=digit
    else:
        odd_digit+=digit
    n=n//10

print("Sum of even digits =",even_digit)
print("Sum of odd digits =",odd_digit)


#10
total = 0

for i in range(5):
    n = int(input("Enter a value: "))

    if n == 0:
        continue

    total += n

print(total)

