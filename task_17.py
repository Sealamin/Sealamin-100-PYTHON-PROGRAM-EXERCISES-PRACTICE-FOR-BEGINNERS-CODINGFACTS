a = int(input("Enter the size of a: "))
b = int(input("Enter the size of b: "))
c = int(input("Enter the size of c: "))

s = (a + b + c)/2

area_triangle = float(round(((s*(s - a) * (s - b) * (s - c))**(1/2)),2))
area_triangle_2 = format (area_triangle, '.2f')

a = print(f"\na = {a}")
b = print(f"b = {b}")
c = print(f"c = {c}")

print(f"\nThe area of the triangle is {area_triangle_2}.")