# passing by value and passing reference
def change(v1, v2):
    a = v1 + 10
    b = v2 * 1000

def change_list(list1, list2):
    list1.append('four')
    list2 = ['and', 'we', 'can', 'change', 'lists']

#out of function body

v1 = 5
v2 = 8
change(v1, v2)
print(v1, v2)

l1 = ['one', 'two', 'three' ]
l2 = ['we', 'like', 'python', ]
change_list(l1, l2)
print('list1: ', l1)
print('list2: ', l2)

