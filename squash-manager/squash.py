import string
import players

data_file = "players.txt"
modified = 0; # if anything has changed the data then prompt

# always load the players.txt file
players.load_players(data_file)

# using dictionaries to control data
while True:
    print "\n  - Please choose from the following options:\n"
    print "\t1 - To Print out the list of players and all relevant information \n"
    print "\t2 - To Print out list of players e-mail addresses\n"
    print "\t3 - To print a list of players from division (1-6) \n"
    print "\t4 - To add players to division\n"
    print "\t5 - To delete players from a division\n"
    print "\t6 - To edit information on players\n"
    print "\t7 - To see division standings\n"
    print "Or enter 'q' to quit\n"
    option = raw_input("\t: ")
   #8 possible outcomes

    if option == "1":
        players.print_players()
    elif option == "2":
        players.print_emails()
    elif option == "3":
        division = raw_input("\n\t\tPlease enter the division number: ")
        players.print_division(division)
    elif option == "4":
        filename = raw_input("\n\t\tPlease enter the file name to write to: ")
        #marklist.write_modules(filename)
    elif option == "5":
        #marklist.reset_marklist()
        print "\n\tMarklist reset.\n"
    elif option == "q":
        # if the data has changed then prompt to save file
        if modified > 0:
            print "\nSave players changes y/n?\n"
            option = raw_input("\t: ")
            if string.lower(option) != "n":
                players.save_players(data_file)
        break

