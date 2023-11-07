'''
Given a list of numbers,find the sum and average
'''

list1 = [3, 6, 2, 5, 7, 23, 56, 32, 1, 4]
sum = 0
for x in list1:
    sum += x
print("Sum :", sum)
print("Average :", sum/len(list1))
