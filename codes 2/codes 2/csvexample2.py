import csv 
data = [['Braveheart', '1995', 'History'], 
['Good Bad and Ugly', '1970', 'Westren'],
['True Lies', '1998', 'Action']]

##with open('sample3.csv', 'w', newline= '') as csvfile:
##    riter = csv.writer(csvfile, delimiter=',')
##    riter.writerow(['Movies', 'Years', 'Genre'])
##    riter.writerows(data)
##
##csvfile.close()


csvfile = open('sample2.csv', 'w', newline = '')
riter = csv.writer(csvfile, delimiter = ',')
riter.writerow(['Movies', 'Years', 'Genre'])
riter.writerows(data)
csvfile.close()
