middle = 5 
lower =[] 
upper = []

for i in range(10):
    if i < middle: 
        lower.append(i)
    else: 
        upper.append(i)
        

print("lower:", lower)
print("upper:", upper)



print(type(lower))

##import numpy as np
##y = np.array([1, 2, 3])
##print (y, " is of type " , type(y))
##
##print("done!!!")
       
