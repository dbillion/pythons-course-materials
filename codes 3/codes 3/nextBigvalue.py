a = 0
b = 0
c = 0
l = [5, 4, 5, 3, 4, 1, 5]
for i in range(len(l)-1):
    a = l[i]
    b = l[i+1]
    if b > a:
        c += 1

print(c)


# try a program which counts the unique elements and return
# count of unique values

