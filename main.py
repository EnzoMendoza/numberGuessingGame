import random

playing = True
ans = random.randint(1, 100)
guess = ''
while playing:
    try:
        guess = int(input("Guess the random number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please enter a valid number")
        elif guess > ans:
            print("Too high")
        elif guess < ans:
            print("Too low")
        else:
            print("Correct!")
            playing = False
    except ValueError:
        print("Please enter a valid number")




