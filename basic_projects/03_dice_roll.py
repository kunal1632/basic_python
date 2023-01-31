import random

roll_again = True
while roll_again:
    value = random.randint(1, 6)
    print("Rolling the dice...")
    print(f"The value is: {value}")
    asking = input("Roll the dice again: ").lower()
    if asking != 'yes' and asking != 'y':
        roll_again = False
        print("Stoping")
