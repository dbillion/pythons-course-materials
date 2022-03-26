
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]


result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print('\n \n')
print("Matrix multiplication using Lists and loops..................")
for i in range(len(matrix1)):
	for j in range(len(matrix2[0])):
		for k in range(len(matrix2)):
			result[i][j] += matrix1[i][k] * matrix2[k][j]
#
for r in result:
	print(r)
#
