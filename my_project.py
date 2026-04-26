'''use input()function to get a list of 5 numbers.
calculate the total sum,average,biggest and the smallest numbers.
'''
numbers = []

num1 = int(input("Enter first number:"))
numbers.append(num1)

num2 = int(input("Enter second numnber:"))
numbers.append(num2)

num3 = int(input("Enter first number:"))
numbers.append(num3)

num4 = int(input("Enter first number:"))
numbers.append(num4)

num5 = int(input("Enter first number:"))
numbers.append(num5)
print(f"Numbers:{numbers}")

total_sum = sum(numbers)
print(f"Total Sum:{total_sum}")

average = total_sum/len(numbers)
print(f"Average Number:{average}")

biggest_number = max(numbers)
print(f"Biggest Number:{biggest_number}")

smallest_number = min(numbers)
print(f"Smallest Number:{smallest_number}")

names = ["Alice","Bob","Charlie","Diana"]
#replace Bob with anything else
names[1] = "Kenny"
print(f"Modify Names:{names}")

#remove the last name
(names.pop())
print(f"After Removing Last Name:{names}")

