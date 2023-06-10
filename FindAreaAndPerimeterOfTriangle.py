import math
AB=input("length of the first leg:")
AC=input("length of the second leg:")
AB=float(AB)
AC=float(AC)
BC=math.sqrt(AB**2+AC**2)
S=(AB*AC)/2
P=AB+AC+BC
print("area of triangle is:%.2f"%S)
print("Perimeterr of the triangle is:%.2f"%P)
print(BC)
