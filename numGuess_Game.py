import random
def play_Game():
    target = random.randint(1,5)
    print("i am thinking of random number")

    while True:
        try:
            guess = int(input("enter a guess number"))

            if guess == target:
                print("correct guess!")
                break
            elif guess =<5:
                print("Invalid guess.pls choose 1,2,3,4,5")
            else:
                print("Try again")
        except ValueError:
            print("pls enter a valid whole number")

play_Game()            

            

  