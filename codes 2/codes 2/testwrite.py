wfile = open('newfile.txt', 'w')

for line in range(0,15):
    wfile.write('this is '+ str(line + 1) + ' line in the text file.')
    wfile.write('\n')

wfile.close()
print('file written successfully ')

wfile = open('newfile.txt')

print(wfile.read())
wfile.close()








    
# 
# str1 = 'this is my first line of text in the text file. '
# wfile.write(str1)
# wfile.write('\n')
# wfile.write('this is my second line of string in the text file. ')
# wfile.seek(0,0)
# print(wfile.read())
# wfile.close()
# 
# readfile = open('newfile.txt')
# print(readfile.read(), end = '')
# readfile.close()
