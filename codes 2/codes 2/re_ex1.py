import re
def ser(text):
    result = re.search(r'm.e', text)
    return result != None


print(ser('academie')) # True
print(ser('aerial')) # False
print(ser('paramedic')) # False
