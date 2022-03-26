class A:

    c = []

    def __init__(self):
        global c
        self.v = 0
        c.append(1)

    def getC():
        global c
        print(c)

a = A()
A.getC()
