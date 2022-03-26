import csv


file = open('sample.csv')
csvfile = csv.reader(file, delimiter=',')
for row in csvfile:
	print(row[2])
file.close()


##header = next(csvfile)
##data = [row for row in csvfile]
##print(header)
##print('............................')
##print(data)



##
##i = 0
##data = [] 
##for row in enumerate(csvfile):
##        data[i] = row
##        i = i + 1
##        
##
##print(data)

# import csv
# import io

# data = 'purple,red,green,blue,orange,black'
# reeder = csv.reader(io.StringIO(data))
# for row in reeder:
	# print(','.join(row))
