f0 = 0
f1 = 1
fn = 0
ratio = [] 
n = int(input('Enter the number of fibonacci numbers to calculate, n = ' ))
print(f0, end = ' ')
print(f1, end = ' ')

while n > -1:
    fn = f0 + f1
    print(fn, end = ' ')
    f0 = f1
    f1 = fn
    n = n - 1
