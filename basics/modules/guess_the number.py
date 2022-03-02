import random as rnd

mini = int(input("Please enter the minimum value: \n"))
maxi = int(input("Please enter the maximum value: \n"))
num = rnd.randrange(mini,maxi)

while(True):

    print(f"I am thinking of a number between {mini} and {maxi}. Can you guess what it is? ")
    num_guess = int(input())

    avg = (mini + maxi) / 2

    if num_guess == num:
        print("Congratulations! You guessed my number!")
        break
    elif num_guess > avg:
        print("Guess is too high")
    else:
        print("Guess is too low")

print("Game over")
