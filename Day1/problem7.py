'''
sum of all +ve numbers
'''

list1 = [-4, 5, 78, -23, 42, 12, 0, 6, -54]
sum = 0
for x in list1:
    if x > 0:
        sum += x
print("sum of all +ve numbers:", sum)
