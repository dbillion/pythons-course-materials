# fibonaci series

f0 = 0
f1 = 1

def fibb(num):
    if num == 1 :
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibb(num - 1) + fibb(num + 2)


print (fibb(5), end = ' ')

        
    
