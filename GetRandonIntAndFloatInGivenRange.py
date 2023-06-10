from random import random, randint
print("Range of the integer:")
imin=int(input( ))
imax=int(input( ))
n=randint(imin, imax)
print(("%d"%n))
print("Range of the floats:")
fmin=float(input( ))
fmax=float(input( ))
n= random()*(fmax-fmin)+fmin
print("%3f"%n)
