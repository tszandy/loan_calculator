# cash = 200000
# r = 0.02375
# pay = 1322
# year = 15

# for i in range(year * 12):
#     cash = cash *(1+r/12)-pay
#     print("i {0}".format(i))
#     print("cash {0}".format(cash))
# print(cash)

# cash = 200000
# r = 0.03
# pay = 843
# year = 30

# for i in range(year * 12):
#     cash = cash *(1+r/12)-pay
#     print("i {0}".format(i))
#     print("cash {0}".format(cash))
# print(cash)


cash = 200000
r = 0.02375
R = 1+r/12
year = 15
denominator = sum(R**i for i in range(year*12))

print("denominator {0}".format(denominator))
print("total cash {0}".format(cash*R**(year*12)))
print(cash*R**(15*12)/denominator)

cash = 200000
r = 0.03
R = 1+r/12
year = 30
denominator = sum(R**i for i in range(year*12))

print("denominator {0}".format(denominator))
print("total cash {0}".format(cash*R**(year*12)))
print(cash*R**(year*12)/denominator)