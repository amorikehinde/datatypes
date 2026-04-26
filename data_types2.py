'''lecture="01.presentation.pdf"
remove=lecture[:-4]
print(remove)
separate=remove.split('.')
print(separate)
a,b=separate
print(a,b)'''
'''first_name= input('Enter Firstname:')
sur_name= input('Enter Surname:')
access_1= first_name[::2]
access_2= sur_name[:3]

import random
otp= random.randint(1,10000)
password= access_1 + access_2 +str(otp)
print('Password:',password)
'''
#checking for palindrome in the following
pal1="racecar"
check1=pal1[::-1]
if pal1==check1:
    print('palindrome')
else:
    print("not palindrome")
pal2="hello"
check2=pal2[::-1]
if pal2==check2:
    print('palindrome')
else:
    print("not palindrome")
pal3="Nuel"
check3=pal3[::-1]
if pal3==check3:
    print('palindrome')
else:
     print("not palindrome")
pal4="madam"
check4=pal4[::-1]
if pal4==check4:
    print('palindrome')
else:
    print("not palindrome")
pal5="level"
check5=pal5[::-1]
if pal5==check5:
     print('palindrome')
else:
     print("not palindrome")

#code to generate username
email=input("enter your email:")
clean_email=email.strip().lower().replace(' ','')
locate=clean_email.find('@')
if locate == -1:
    print('wrong email ')
else:
    slice1=clean_email[:locate]
    print(f'Your username is:{slice1}')












