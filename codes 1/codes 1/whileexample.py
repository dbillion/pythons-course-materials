import random

answer = random.randint(0, 5)
guess = 5
while True:
    userinput = int(input('gues the number'))
    if userinput == answer:
        print('you are correct')
        break
    elif guess < answer:
        continue
    else:
        print('something')
