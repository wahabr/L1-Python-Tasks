gift_card = 50
initial_game = 35
weapon_rapier = 2
weapon_shortbow = 2
weapon_dagger = 2
armour_chainmail = 5
print("Opening Balance: ${}".format(gift_card))
gift_card = gift_card - weapon_rapier - weapon_dagger - weapon_shortbow - armour_chainmail - initial_game
print("Dungeons and Dragons: ${}, Rapier: ${}, Dagger: ${}, Shortbow: ${}, Chainmail: ${}".format(initial_game, weapon_rapier, weapon_dagger, weapon_shortbow, armour_chainmail))
print("Closing Balance: ${}".format(gift_card))
