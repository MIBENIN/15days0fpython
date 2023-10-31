'''
compound interest

SI=(ptr)/100
CI=Amount-Principal

Amount=Principal(1+Rate of Interest/100)**No of years
'''


def compoundInterest(p, r, t):
    Amount = p*(pow(1+r/100, t))
    CI = Amount-p
    return CI


print("CI:", compoundInterest(3000, 5, 3))
