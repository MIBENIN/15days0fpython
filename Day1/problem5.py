'''
Palindrome 
'''
st = input("Enter the string:")
str_reverse = st[::-1]
if st == str_reverse:
    print("String is palindrome")
print("Not palindrome")
