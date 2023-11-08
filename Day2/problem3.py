'''
Check a given string is palindrome or not
'''

givenStr = input("Enter a string : ")

givenStrReversed = givenStr[::-1]

if (givenStr == givenStrReversed):
    print(f"{givenStr} is a palindrome")
else:
    print(f"{givenStr} is not a palindrome")
