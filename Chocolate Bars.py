num_people = 5
num_pieces = 7
chocolate_pieces = 18 * num_pieces
print("You have {} pieces of chocolate to share evenly among {} people.".format(chocolate_pieces, num_people))
print("In total each person will get {} bars of chocolate, {} pieces, and there will be {} pieces left over".format(chocolate_pieces // num_people // num_pieces, chocolate_pieces // num_people, chocolate_pieces % num_people))

