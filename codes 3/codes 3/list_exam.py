listy = [5, 4, 6, 3, 23, 16, 90, 33, 4, 5, 6, 3]
mmax = None
mmax2 = None

for v in listy:
    if mmax is None:
        mmax = v
    elif mmax > v:
        mmax2 = mmax
        mmax = v
    elif mmax2 is None:
        mmax2 = v
    elif mmax2 < v:
        mmax2 = v
    else:
        pass
    
print(mmax)
print(mmax2)