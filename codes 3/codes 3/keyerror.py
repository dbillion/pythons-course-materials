t1 = (2, 3, 4)
t2 = (7, 8, 9)
t3 = (1, 5, 6)
t4 = (2, 3, 6)
table = {t1:'ABC', t2: 'KLM', t3: 'XYZ'}
try:
    print(table[t4])
except KeyError as err:
    print("Error class is: ", type(err))
    print("Error message is: ", err)
#
