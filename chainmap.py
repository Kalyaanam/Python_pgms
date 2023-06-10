from collections import ChainMap
A={1:'pen',2:'chalk piece'}
B={3:'paper',4:'blackboard'}
a=ChainMap(A,B)
print(a)