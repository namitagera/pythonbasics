import random 

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total
def main():
    player1 = input("Enter player 1 name:\n")
    player2 = input("Enter player 2 name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "total", roll1)
    print(player2, "total", roll2)


    if (roll1 > roll2):
        print(player1, "WON")
    elif (roll2 > roll1):
        print(player2, "WON")
    else:
        print("DRAW")

main()

