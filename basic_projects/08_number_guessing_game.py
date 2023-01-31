import random
num = random.randrange(1, 100)
guess = int(input("Enter a number you guessed: "))
count = 0
while True:
    count += 1
    if guess == num:
        print(
            f"Correct! it was the right number and it takes you {count} guesses")
        break
    elif guess < num:
        print("Too low")
        guess = int(input("Guess again: "))
    elif guess > num:
        print("Too high")
        guess = int(input("Guess again: "))
