#local and global variables
count = 0

def counter():
    global count
    count = 1
    list1 = list(range(1, 3))
    for _ in list1:
        count += 1
    print('local', count)

#out of function body
print('Before function call: ', count)
counter()
print('After function call: ', count)
