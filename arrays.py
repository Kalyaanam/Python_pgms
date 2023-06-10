#import array
#a=array.array('i ',[1,2,3,4,5,6,7,9,10])
#print(a)

#import array as arr
#a=arr.array('i',[1,2,3])
#print(a)

#from array import *
#a=array('i',[1,2,3])
#print(a)

from array import *
a=array('i',[1,23,434,545])
print(a)
a.append(234)
print("Append example array:",a)
b=array('i',[312,41234,35545,32])
b.extend([123,23423,5425])
print(b)
print("extend example array:",b)
c=array('i',[4435,4556,456,2313556,3242])
c.insert(3,345)
print(c)
print("insert example array:",c)