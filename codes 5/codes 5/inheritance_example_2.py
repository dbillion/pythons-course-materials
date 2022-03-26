class A:
    i = 1

class B:
    pass

class X(A, B):
    pass

class Y(X):
    pass

##end of the class definitions
x = X()
y = Y()
