x = 10

def f():
    x = 3
    print('local x', x)
    return print('hello')
    

f()
#print('global x: ', x)
