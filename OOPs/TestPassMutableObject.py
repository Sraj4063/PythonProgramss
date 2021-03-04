from Circle import Circle
def main():
    myCircle = Circle()
    n = 5
    printAreas(myCircle,n)
    # Display  myCircle.radius and times
    print("\nRadius is ",myCircle.radius)
    print("n is",n)

def printAreas(c,times):
    print("RAdius \t\t Area")
    while (times >= 1):
        print(c.radius, "\t\t",c.getArea())
        c.radius = c.radius + 1
        times = times - 1
main()