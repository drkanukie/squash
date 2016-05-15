import string
import players

data_file = "../data/players.txt"
modified = 0; # if anything has changed the data then prompt

# always load the players.txt file
players.load_players(data_file)

# using dictionaries to control data
while True:
    print "\n  - Please choose from the following options:\n"
    print "\t1 - To Print out the list of players and all relevant information for notive board\n"
    print "\t2 - To Print out list of players e-mail addresses\n"
    print "\t3 - To print a list of players from division (1-6) \n"
    print "\t4 - To add players to division\n"
    print "\t5 - To delete players from a division\n"
    print "\t6 - To edit information on players\n"
    print "\t7 - To see division standings\n"
    print "\t8 - Enter player points\n"
    print "\t9 - Rollup divisions\n"
    print "Or enter 'q' to quit\n"
    option = raw_input("\t: ")
   #8 possible outcomes

    if option == "1":
        # TODO title and points systems
        #
        players.print_title()
        for t in range(1,7):
            # pretty print divisions
            players.print_table(t)
        players.print_points()
        players.print_rules()
        players.print_signup()
    elif option == "2":
        players.print_emails()
    elif option == "3":
        division = raw_input("\n\t\tPlease enter the division number: ")
        try:
            players.print_division(int(division))
        except:
            print("Division not found")
    elif option == "4":
        # enter new player
        forename = ''
        surname = ''
        email = ''
        phone = ''
        division = 0

        print ("* required values")
        while forename == '':
            forename = raw_input("\n\t\t*First name: ")
        while surname == '':
            surname = raw_input("\n\t\t*Surname name: ")
        while email == '':
            email = raw_input("\n\t\t*Email: ")

        phone = raw_input("\n\t\tPhone: ")
        try:
            div = int(raw_input("\n\t\t*Division (1-6): "))
        except:
            div = 0
        while (div < 1) or (div > 6):
            try:
                div = int(raw_input("\n\t\t*Division (1-6): "))
            except:
                div = 0
        players.add_player(forename,surname,email,phone,division)
        # trigger save on exit
        modified = 1

    elif option == "5":
        # delete player
        forename = ''
        surname = ''
        print ("* required values")
        while forename == '':
            forename = raw_input("\n\t\t*First name: ")
        while surname == '':
            surname = raw_input("\n\t\t*Surname name: ")
        players.delete_player(forename,surname)
        # trigger save on exit
        modified = 1

    elif option == "6":
        # edit player
        forename = ''
        surname = ''
        email = ''
        phone_number = ''
        division_current = 0
        points_current = 0
        division_previous = 0
        point_previous = 0

        print ("* required values")
        while forename == '':
            forename = raw_input("\n\t\t*First name: ")
        while surname == '':
            surname = raw_input("\n\t\t*Surname name: ")
        # use names as key as easier to remember than emil but that is unique
        info = players.get_player_info(forename,surname)

        # no found
        if len(info) > 0:

            # prompt showing current values
            # null string '' no changes
            # -2 no changes
            email = raw_input("\n\t\tEmail ("+ info['email']  +") : ")
            phone_number = raw_input("\n\t\tPnone number  ("+ info['phone_number']  +") : ")

            # catch exceptions for blank input
            try:
                print "use 0 for unavailable this round"
                print "use -1 as away until further notice"
                division_current = int(raw_input("\n\t\tCurrent division ("+ str(info['division_current'])  +") : "))
            except:
                # null value pass -2 as 0 & -1 are valid inputs
                division_current = -2

            try:
                points_current = int(raw_input("\n\t\tCurrent points ("+ str(info['points_current'])  +") : "))
            except:
                points_current = -2

            try:
                division_previous = int(raw_input("\n\t\tPrevious division ("+ str(info['division_previous'])  +") : "))
            except:
                division_previous = -2

            try:
                points_previous = int(raw_input("\n\t\tPrevious points ("+ str(info['points_previous'])  +") : "))
            except:
                points_previous = -2

            players.edit_player(forename,surname,email,phone_number,division_current,points_current,division_previous,points_previous)
            # trigger save on exit
            modified = 1

        else:
            print "\nPLAYER %s %s NOT FOUND\n" % (forename, surname)

    elif option == "8":
        # update points player
        points = 0
        player_list = players.get_players()
        for player in player_list:
            while points == 0:
                try:
                    points = int(raw_input("\n\t\tPoints this round for " + player['forename'] + " " + player['surname'] + ": "))
                except:
                    points = 0
            players.edit_player(player['forename'],player['surname'],'','',-2,points+player['points_current'],-2,-2)
            points = 0

        modified = 1

    elif option == "9":
        # update divisons
        try:
            num_promote = int(raw_input("\n\t\tNumber players to promote: "))
        except:
            num_promote = 2
        print "\nUpdate divisions y/n?\n"
        option = raw_input("\t: ")
        if string.lower(option) == "y":
            players.update_divisions(num_promote)

        modified = 1

    elif option == "q":
        # if the data has changed then prompt to save file
        if modified > 0:
            print "\nSave players changes y/n?\n"
            option = raw_input("\t: ")
            if string.lower(option) != "n":
                players.save_players("../data/players.txt")
        break

