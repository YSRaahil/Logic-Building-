'''
Level 3: Mathematical & Logical Patterns 
1.	Print the squares of numbers from 1 to n. 
2.	Print cubes of numbers from 1 to n. 
3.	Print all numbers between a and b divisible by 7. 
4.	Find HCF (GCD) of two numbers using loops. 
5.	Find LCM of two numbers using loops. 
6.	Print all factors of a given number. 
7.	Find the sum of all factors of a number. 
8.	Check if a number is a strong number (sum of factorials of digits = number). 
9.	Print first n terms of an arithmetic progression (a, d). 
10.	Print first n terms of a geometric progression (a, r). 
'''

#1
'''n = int(input("Enter n value :"))
for i in range(1,n+1):
    print(i*i)'''

#2
'''n = int(input("Enter n value:"))
for i in range(1,n+1):
    print(i**3)'''

#3
'''a = int(input("Enter a-value: "))
b = int(input("Enter b-value: "))
for i in range(a,b+1):
    if(i % 7 == 0):
        print(i)   '''

#4
'''hcf=1
a = int(input("Enter the number"))
b = int(input("Enter the number"))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i

print(hcf)        '''

#5
'''a= int(input("Enter the number:"))
b= int(input("Enter the number:"))
for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        break
print("lcm = ",i)'''

#6
'''n = int(input("Enter the number:"))
for i in range(1,n+1):
    if n%i ==0:
        print(i)'''

#7
'''n = int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    if n%i ==0:
        sum+=i
print(sum)'''

#8
'''n = int(input("Enter the number"))
temp=n
sum_fact=0
while n>0:
    digit = n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum_fact=sum_fact+fact    
    n=n//10

if temp==sum_fact:
    print(temp,"is a strong number")'''  


#9
'''a = int(input("Enter the first value:"))
d = int(input("Enter the common difference:"))
n = int(input("Enter the n-value:"))
for i in range(n):
    print(a+i*d)'''

#10
'''a = int(input("Enter the first value :"))
r = int(input("Enter the common ratio:"))
n = int(input("Enter the n-value:"))
for i in range(1,n):
    print(a*(r**(i-1))) '''   

       

