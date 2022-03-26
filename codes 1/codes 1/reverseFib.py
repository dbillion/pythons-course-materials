
def isSquare(num):
    x = int((num)**(0.5))
    return (x*x == num)


n = int(input('Enter the number to calculate the the Fibonacci series from: '))
 
while n >= 0:
    if isSquare(5*n*n + 4) or isSquare(5*n*n - 4):
        print(n, end = ' ')
        
    n = n - 1

                        
