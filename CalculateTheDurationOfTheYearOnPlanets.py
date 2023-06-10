from math import pi
r=input("Radious of the orbit(million km):")
v=input("Orbital Speed")
r=float(r)
v=float(v)
r=r*1000000
year=2*pi*r/v
year=year/(60*60*24)
print(round(year))
