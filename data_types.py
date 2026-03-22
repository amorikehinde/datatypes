'''hospital_name="saint Lauren Hospital"
hospital_address="54 Maple street,Denver,Co 80202"
head_doctor_name="Dr Beckley Lauren"
numbers_of_good_doctors="35"
numbers_of_nurse="70"
numbers_of_wards="43"
numbers_of_hospital_bed="150"
numbers_of_operating_theatre="5"
numbers_of_patients="123"
numbers_of_emergency_cases="48"
numbers_of_ambulances= 17
location="No4 odo street"
wards="5 wards"
beds="40 beds"
security="5 security"
patients="100"
print(hospital_name.upper())
print(location.count('o'))
'''
animal="elephant"
first_three=(animal[:3])
print(first_three) #displaying first 3 characters using negative index
last_three=(animal[-3:])
print(last_three) #displaying last 3 characters using positive index
combine_to_capital_letter=((first_three+last_three).upper())
print(combine_to_capital_letter) #making them one word and convert to capital
reverse_n_exclude_last=(combine_to_capital_letter)[::-1]
print(reverse_n_exclude_last)#reverse with the last alphabet excluded 
x='i love python'
print(x.title())
lecture="o1.presentation.pdf"
reduce=lecture[:-4]
print(reduce)
a,b=lecture.split('.')
print(a,b)