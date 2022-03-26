print('Tax Calculator\n')
print('```````````````````')
RATE = 0.15
EXEMPTION_AMOUNT = 500.0
income = float(input('Please enter your income: '))
exemptions = int(input('Please enter the number of exemptions: '))
tax = max(0.0, (12*income - exemptions * EXEMPTION_AMOUNT) * RATE)
print('Your total tax is $%0.2f.' % tax)
