'''Level 4: String-based Recursion 
1.	Reverse a string using recursion. 
2.	Check if a string is palindrome using recursion. 
3.	Count vowels in a string recursively. 
4.	Remove all spaces from a string recursively. 
5.	Replace all occurrences of a character (say ‘a’ → ‘x’) recursively. 
6.	Remove all occurrences of a character from a string recursively. 
7.	Print all characters of a string one by one recursively. 
8.	Print the string in reverse order recursively (without using loops). 
9.	Convert a string to uppercase recursively. 
10.	Count consonants and vowels separately using recursion. 
'''

#1
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])   

#2
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])   

#3
def count_vowels(s):
    if len(s) == 0:
        return 0
    count = 1 if s[0].lower() in 'aeiou' else 0
    return count + count_vowels(s[1:])  

#4
def remove_spaces(s):
    if len(s) == 0:
        return s
    if s[0] == ' ':
        return remove_spaces(s[1:])
    return s[0] + remove_spaces(s[1:])  

#5
def replace_character(s, old_char, new_char):
    if len(s) == 0:
        return s
    if s[0] == old_char:
        return new_char + replace_character(s[1:], old_char, new_char)
    return s[0] + replace_character(s[1:], old_char, new_char)

#6
def remove_character(s, char_to_remove):
    if len(s) == 0:
        return s
    if s[0] == char_to_remove:
        return remove_character(s[1:], char_to_remove)
    return s[0] + remove_character(s[1:], char_to_remove)   

#7
def print_characters(s, index=0):
    if index == len(s):
        return
    print(s[index])
    print_characters(s, index + 1)          

#8
def print_reverse(s, index=None):
    if index is None:
        index = len(s) - 1
    if index < 0:
        return
    print(s[index])
    print_reverse(s, index - 1) 

#9
def to_uppercase(s):
    if len(s) == 0:
        return s
    return s[0].upper() + to_uppercase(s[1:])   

#10
def count_consonants_and_vowels(s):
    if len(s) == 0:
        return (0, 0)
    vowels, consonants = count_consonants_and_vowels(s[1:])
    if s[0].lower() in 'aeiou':
        return (vowels + 1, consonants)
    elif s[0].isalpha():
        return (vowels, consonants + 1)
    else:
        return (vowels, consonants)     
