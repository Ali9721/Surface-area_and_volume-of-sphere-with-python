# At first I use math module
import math

# Get input for radius 
r = float(input("Enter the radius of the sphere: "))
 
#Let's calculate the volume and surface 
# Obviously I use this equal "π" = "math.pi" in formula
volume = (4/3)*math.pi*r**3
surface_area = 4*math.pi*r**2 

print(f"Surface area of the sphere is: {surface_area:.2f}")
print(f"Volume of the sphere is: {volume:.2f}")