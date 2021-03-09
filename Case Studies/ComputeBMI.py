weight = eval(input("enter your weight in kilograms"))
height = eval(input("enter your height in Meters"))

bmi = weight / (height * height)
print("BMI IS ",format(bmi,".2f"))
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else :
    print("obese")