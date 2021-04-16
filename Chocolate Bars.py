try:
    num_people = int(input("How many people are there?"))
    num_bars = int(input("How many bars of chocolate are there?"))
    num_pieces = int(input("How many pieces are in each bar?"))
    chocolate_pieces = num_bars * num_pieces
    if num_people > 0 and num_bars > 0 and num_pieces > 0:
        print("You have {} pieces of chocolate to share evenly among {} people.".format(chocolate_pieces, num_people))
        print("In total each person will get {} whole bars of chocolate, {} extra pieces, and there will be {} pieces left over".format(chocolate_pieces // num_people // num_pieces, chocolate_pieces // num_people % num_pieces, chocolate_pieces % num_people))
    else:
        print("You cannot have negative friends or negative chocolate!")
except ValueError:
    print("Please input a number greater than 0.")

