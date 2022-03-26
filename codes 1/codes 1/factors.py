# prime factorization
# question 1 (week 1)


n = int(input('enter the number > '))
p = 2

while n >= p*p :
    if n % p == 0:
        print( p , end =' x ')
        n = int(n / p)
    else:
        p = p + 1

print(n)

