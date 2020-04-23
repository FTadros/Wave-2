import math

a = int(input("Please input a value for a: "))
b = int(input("Please input a value for b: ")) 
c = int(input("Please input a value for c: ")) 

discriminant = b ** 2 - (4 * a * c)
discriminant = int(discriminant)

root = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
root_2 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)

if discriminant == 0:
    num_roots = 1
elif discriminant > 0:
    num_roots = 2
elif discriminant < 0:
    num_roots = 0

print(num_roots, "real roots", root, root_2,)
