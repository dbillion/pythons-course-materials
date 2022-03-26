import time
import timeit 

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

def calcProd2():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %.4f seconds to calculate.' % (endTime - startTime))
#maybe the return was causing extra problem so I removed the return statment from the calcProd2()
#not much significant difference is observered in both outputs (minor)
#checking the execution time of a function. 
print(timeit.timeit('calcProd2()', setup='from __main__ import calcProd2', number=1))
