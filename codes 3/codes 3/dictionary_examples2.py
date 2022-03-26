people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
people[3]['married'] = 'yes'

##print(people)

##deleteing some particular entry
# del people[3]['married']
# del people[4]['married']

####deleting completely some records
####del people[3], people[4]
##
##traversing the dictionary
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])


