cash = 400000
r = 0.0723
R = 1+r/12
year = 15
denominator = sum(R**i for i in range(year*12))

print("denominator {0}".format(denominator))
print("total cash {0}".format(cash*R**(year*12)))
print(cash*R**(year*12)/denominator)
