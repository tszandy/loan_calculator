cash = 16080.43
r = 0.0585
pay = 2276.28
R = (1+r/12)
month = 0

while cash>0:
    cash = cash *R-pay
    # print("month {0}".format(month))
    # print("cash {0}".format(cash))
    month+=1

# print()
# print("cash:{}".format(cash))
year = month//12
month = month%12
print("year:{}".format(year))
print("month:{}".format(month))
