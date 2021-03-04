from BMI import  BMI
def main():
    name  = input("your name")
    age = eval(input("enter your age"))
    weight = eval(input("enter your weight in KILOGRAM"))
    height = eval(input("enter your height IN METERS"))
    bmil = BMI(name , age, weight, height)
    print("the BMI FOR ", bmil.getName(), "is", bmil.getBMI(), bmil.getStatus())
main()