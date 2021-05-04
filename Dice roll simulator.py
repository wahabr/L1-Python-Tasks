import random
dice = [ 2, 3, 4, 5, 6, 8, 10, 12, 20, 100]
roll_dice = input("Would you like to roll a dice?").strip().lower()
if roll_dice == "yes":
    dice_type = input("These are the dice you have available: {} which type of dice would you like to roll?".format(dice))
    if dice_type == 2 or 3 or 4 or 5 or 6 or 8 or 10 or 12 or 20 or 100:
        dice_number = int(input("How many d{} dice would you like to roll?".format(dice_type)))
        for i in range (dice_number):
            result = random.randint(1,dice_type)
            print(result)
            i += 1
    else:
        print("{} is not available.".format(dice_type))



