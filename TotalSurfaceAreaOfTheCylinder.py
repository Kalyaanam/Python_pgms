from math import pi
h=float(input('h= '))
r=float(input('r= '))
circles=2*(pi*r**2)
side=2*pi*r*h
area=circles+side
print('a= ',round(area,2))
print(circles)
print(side)
print(area)