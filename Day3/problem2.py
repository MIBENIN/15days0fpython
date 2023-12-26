'''
Given a list of integers, find all the even numbers and
store them in a new list
'''
listOfNums = [34, 67, 12, 56, 32, 11, 3, 90]
listOfEvenNums = []
for x in listOfNums:
    if (x % 2 == 0):
        listOfEvenNums.append(x)
print("Even numbers:", listOfEvenNums)
