def primefactors(n):

    p = 2
    psq = pow(2, 2) # 2*2, 2**2


    while True:
        if n >= psq:
            if n % p == 0:
                print (p, ' x ', end = ' ')
            else:
                p += 1
                continue
        else:
            print(n)
            break
        n = n//p
        continue 
    #end of loop
