import players
import string

#
# default data file
data_file = "../data/players.txt"
#
# null edit value
edit_none = players.edit_none
#
# if anything has changed the data then prompt
modified = 0;

# always load the players.txt file
players.load_players(data_file)

# using dictionaries to control data
while True:
    print "\n  - Please choose from the following options:\n"
    print "\t1 - To Print out the list of players and all relevant information for notice board\n"
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
   #9 possible outcomes & quit

    if option == "1":
        #
        # Print the league tables for the notice board
        #
        players.print_notice()

    elif option == "2":
        #
        # Print all players names and emails
        #
        players.print_emails()

    elif option == "3":
        #
        # Print contact details for players for a division
        #
        division = raw_input("\n\t\tPlease enter the division number: ")
        try:
            players.print_division(int(division))
        except:
            print("Division not found")

    elif option == "4":
        #
        # Enter new player
        #
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
        #
        # Delete specified player
        #
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
        #
        # Edit player info
        #
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
        # use names as key as easier to remember than email but that is unique
        info = players.get_player_info(forename,surname)

        # no found
        if len(info) > 0:

            # prompt showing current values
            # null string '' no changes
            # edit_none no changes
            email = raw_input("\n\t\tEmail ("+ info['email']  +") : ")
            phone_number = raw_input("\n\t\tPnone number  ("+ info['phone_number']  +") : ")

            # catch exceptions for blank input
            try:
                print "use 0 for unavailable this round"
                print "use -1 as away until further notice"
                division_current = int(raw_input("\n\t\tCurrent division ("+ str(info['division_current'])  +") : "))
            except:
                # null value pass edit_none as 0 & -1 are valid inputs
                division_current = edit_none

            try:
                points_current = int(raw_input("\n\t\tCurrent points ("+ str(info['points_current'])  +") : "))
            except:
                points_current = edit_none

            try:
                division_previous = int(raw_input("\n\t\tPrevious division ("+ str(info['division_previous'])  +") : "))
            except:
                division_previous = edit_none

            try:
                points_previous = int(raw_input("\n\t\tPrevious points ("+ str(info['points_previous'])  +") : "))
            except:
                points_previous = edit_none

            players.edit_player(forename,surname,email,phone_number,division_current,points_current,division_previous,points_previous)
            # trigger save on exit
            modified = 1

        else:
            print "\nPLAYER %s %s NOT FOUND\n" % (forename, surname)

    elif option == "7":
        #
        # Print vision standings
        #
        division = raw_input("\n\t\tPlease enter the division number: ")
        try:
            players.print_standing(int(division))
        except:
            print("Division not found")

    elif option == "8":
        #
        # Update points for all players
        #
        points = 0
        player_list = players.get_players()
        for player in player_list:
            # get a valid points value
            while points == 0:
                try:
                    points = int(raw_input("\n\t\tPoints this round for " + player['forename'] + " " + player['surname'] + ": "))
                except:
                    # default to zero if bad input
                    points = 0
            players.edit_player(player['forename'],player['surname'],'','',edit_none,points+player['points_current'],edit_none,edit_none)
            points = 0
        # trigger save on exit
        modified = 1

    elif option == "9":
        #
        # Update divisions get the number of players to promote
        #
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
                # save the file if not answered n
                players.save_players(data_file)
        break

