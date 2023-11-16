'''
count the vowels in a string
'''

vowels = ["a", "e", "i", "o", "u"]
myStr = "This is a string"
vowelsCount = 0
for x in myStr:
    if x in vowels:
        vowelsCount += 1

print("Vowels count ", vowelsCount)
