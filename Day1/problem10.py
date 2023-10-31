'''
Days--->Years,months,days...
'''

givendays = 10000

years = givendays//365
months = (givendays-years*365)//30
days = (givendays-years*365-months*30)
print(f"Years : {years} , Months: {months} ,days: {days}")
