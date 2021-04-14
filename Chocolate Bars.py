try:
    num_people = int(input("How many people?"))
    num_bars = int(input("How many bars of chocolate are there?"))
    num_pieces = int(input("How many pieces are in each bar?"))
    chocolate_pieces = num_bars * num_pieces
    print("You have {} pieces of chocolate to share evenly among {} people.".format(chocolate_pieces, num_people))
    print("In total each person will get {} whole bars of chocolate, {} extra pieces, and there will be {} pieces left over".format(chocolate_pieces // num_people // num_pieces, chocolate_pieces // num_people % num_pieces, chocolate_pieces % num_people))
