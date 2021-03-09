import sys

status = eval(input("0 - for single, 1 - for married jointly, 2 - married separately, 3 - for head of household, Enter the filling status"))

income = eval(input("Enter your salary"))

tax = 0

if status == 0:
    if 0 < income <= 250000:
        tax = 0

    elif 250000 < income <= 500000:
        tax = income * 0.05

    elif 500000 < income <= 750000:
        tax = income * 0.10

    elif 750000 < income <= 1000000:
        tax = income * 0.15

    elif 1000000 < income <= 1250000:
        tax = income * 0.20

    elif 1250000 < income <= 1500000:
        tax = income * 0.25

    elif income > 1500000:
        tax = income * 0.30

elif status == 1:
    print("go to the  incomeTaxDepartment office or consultant")
elif status == 2 :
    print("go to the  incomeTaxDepartment office or consultant")
elif status == 3 :
    print(" go to the  incomeTaxDepartment office or consultant")
else :
    print("Error  invalid status")
    sys.exit()
print("tax is :",format(tax, ".2f"))