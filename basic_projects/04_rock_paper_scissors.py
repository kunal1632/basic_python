import random
choices = ['rock', 'paper', 'scissors']
player = ''
cpu_score = 0
player_score = 0
while True:
    computer = random.choice(choices)
    player = input(
        "Rock, paper or scissors ? or end the game by typing end: ").lower()
    if player == computer:
        print("TIE")
    elif player == 'rock':
        if computer == 'scissors':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your win!")
            player_score += 1
        else:
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your Lose!")
            cpu_score += 1
    elif player == 'paper':
        if computer == 'rock':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your win!")
            player_score += 1
        else:
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your Lose!")
            cpu_score += 1
    elif player == 'scissors':
        if computer == 'paper':
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your win!")
            player_score += 1
        else:
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("Your Lose!")
            cpu_score += 1
    elif player == 'end':
        print("Final score")
        print(f"Computer score:{cpu_score}")
        print(f"Player score:{player_score}")
        if cpu_score < player_score:
            print("Your win the match")
        else:
            print("You lose the match")
        break
    else:
        print("Invalid input plese try again")
