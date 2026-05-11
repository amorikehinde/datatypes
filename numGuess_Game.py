import random

target = random.randint(1,10)
max_trial = 3

print("Guess the number between 1 and 10.You have 3 attempts.")

for attempt in range(1,max_trial + 1):
    try:
        guess_number = int(input(f"Enter a guess number {attempt}:"))

        if guess_number == target:
            print(f"You win! The number was {target}.")
            break
        elif guess_number <target:
            print("Too low!")
        else:
            print("Too high!")

    except ValueError:
        print("Please enter a valid number.")
        continue
else:
    print(f"Game over! The number was {target}. ")        
           

            

  