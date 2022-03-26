#try and  except: for exception handling 
print("Program to see exception handling")

while True:
    inpF = input('enter temperatur in F: ')
    try:
        frht = float(inpF)
        cel = (frht - 32.0) * (5.0/9.0)
        print(cel)
    except: 
        print ('finishing the program')
        break

# days = ['saturday', 'sunday', 'monday']
# for day in days:
    # print 'Good day today on ', day
