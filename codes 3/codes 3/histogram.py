'''
Build a function that creates histograms.
Every bar needs to be on a new line and its length
corresponds to the numbers in the list passed as an argument.
The second argument of the function represents the character
that needs to be used.
'''
##
##import random
##
##def histogram(alist, char):
##    hist = ''
##    for i in alist:
##        hist = hist + i * char + '\n'
##    #print(hist)
##    return hist
##
##
l = [2, 5, 6, 6, 4, 2]
##l = random.sample(range(0, 21), 10)
##h = histogram(l, '*')
##print(h)

## xy graph
length = len(l)
i = 0
while True:
    if sum(l) != 0:
        if l[i] != 0:
            print('|', end = ' ')
            l[i] -= 1
            i += 1
            if i < len(l):
                continue
            else:
                print('\n')
                i = 0
                continue
        else:
            print('\n')
            i = 0
            continue
    else:
        break
print(l)
    
        
        

