# dictionary based low level database of employees


record = list()
for i in range(3):
    data  = input('Enter name: ')
    data2 = input('Address: ')
    data3 = int(input('Age: '))
    temp = dict(Name = data, Address = data2, Age = data3)
    record.append(temp)
