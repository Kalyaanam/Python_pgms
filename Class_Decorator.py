class sqr:
    def __init__(self,side):
        self._side=side
    @property#decorator
    def side(self):
        return self._side
    @side.setter#decorator
    def side(self,value):
        if value>=0:
            self._side=value
        else:
            print("error")
    @property#decorator
    def area(self):
        return self._side**2
    @classmethod
    def unit_Sqr(cls):
        return cls(1)
s=sqr(5)
print(s.side)
print(s.area)