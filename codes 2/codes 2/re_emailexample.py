import re

txt = 'if you wish to contact me on my emails, '\
'you can contact me on uniID, first_name.second_name@eek.ee, '\
'or personal ID, my_email_id123@gmail.com'

# email = re.compile(r'\w+@\w+\.[a-z]{3}')
# print(email.findall(txt))

# email2 = re.compile(r'\w+\.\w+@\w+\.[a-z]{2,3}')
# print(email2.findall(txt))





emails = re.compile('\w+@\w+\.[a-z]{3}|\w+\.\w+@\w+\.[a-z]{2,3}')
print(emails.findall(txt))
##
##
# emails2 = re.compile(r'\S+@\S+')
# emails2.findall(txt)
