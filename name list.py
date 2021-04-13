name_list = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
#print list
print("This is a list of names: {}".format (name_list))
#print list in alphabetical order
print("This is a list in alphabetical order: {}".format(sorted(name_list)))
#ask name
name = input("What is your name?").strip().title()
#check if name in list
if name in name_list:
    print("{} is in the list".format(name))
else:
    print("{} is not in the list".format(name))
    #ask if want to replace name in list with their name
    answer = input("Would you like to replace a name from the list with {}?".format(name)).strip().lower()
    if answer == "yes":
        name_switch = input("Which name would you like to replace with {}?".format(name)).strip().title()
        if name_switch in name_list:


