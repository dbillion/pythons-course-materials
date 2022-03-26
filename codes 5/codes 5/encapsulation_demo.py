class A:
    def __init__(self, n):
        self.x = n
        self._y = 100
        self.__z = 2525
    
    def disp(self):
        print(self.x)
        print(self._y)
        print(self.__z)
