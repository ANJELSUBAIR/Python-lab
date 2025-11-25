from Graphics.RectFunctions import*
from Graphics.CirFunctions import*
from Graphics.Dgraphics.SphereFunctions import*
from Graphics.Dgraphics.CuboidFunctions import*

#Rectangle
l=int(input("Enter the Length: "))
b=int(input("Enter the Breadth: "))
print("Area of Rectangle= ",RectArea(l,b))
print("Perimeter of Rectangle= ",RectPerimeter(l,b))

#circle
r=int(input("Enter the Radius of circle: "))
print("Area of circle= ",CirArea(r))
print("Perimeter of circle= ",CirPerimeter(r))

#sphere
r=int(input("Enter the Radius of sphere: "))
print("Area of Sphere= ",SpArea(r))
print("Perimeter of Sphere= ",SpPerimeter(r))

#cuboid
l=int(input("Enter the Length: "))
b=int(input("Enter the Breadth: "))
h=int(input("Enter the Height: "))
print("Area of Cuboid= ",CubArea(l,b,h))
print("Perimeter of Cuboid= ",CubPerimeter(l,b,h))
