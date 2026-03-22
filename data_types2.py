'''lecture="01.presentation.pdf"
remove=lecture[:-4]
print(remove)
separate=remove.split('.')
print(separate)
a,b=separate
print(a,b)'''
first_name= input('Enter Firstname:')
sur_name= input('Enter Surname:')
access_1= first_name[::2]
access_2= sur_name[:3]

import random
otp= random.randint(1,10000)
password= access_1 + access_2 +str(otp)
print('Password:',password)