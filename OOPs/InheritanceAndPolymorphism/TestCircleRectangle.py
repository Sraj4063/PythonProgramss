from CircleFromGeometryObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    circle = Circle(1.5)
    print("A circle", circle)
    print("the radius is ", circle.getRadius())
    print("the area is ", circle.getArea())
    print("the diameter is ", circle.getDiameter())

    rectangle = Rectangle(2 , 4)
    print("A rectangle ", rectangle)
    print("the area is ", rectangle.getArea())
    print("the perimeter is" , rectangle.getPerimeter())

main()
