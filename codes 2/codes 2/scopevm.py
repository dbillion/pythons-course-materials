g = 10

def fun():
    global g
    print('hello')
    g = 1
    x = 30
    print('inside g ', g)


fun()
print('outside g ', g)
print(x)
print(g)
