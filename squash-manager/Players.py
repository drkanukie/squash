import string
'''
Code to maintain a list of players contained in players (a global variable)
'''
# global players list
#
players = []
# players will be stored by division to make division tasks simpler
#
divisions = {}
#
# max size of a division
max_division = 6

#
# codes for division_current values
#
div_unavailable = 0
div_absent = -1

def print_table(division_number):
    """
    :param division_number: the division table to print
    :return:
    """

    longest = 0
    letter = 65
    row = 0
    division = divisions[division_number]

    # find longest string

    table_rows = ["| / |   |   |   |   |   |     |",
                  "|   | / |   |   |   |   |     |",
                  "|   |   | / |   |   |   |     |",
                  "|   |   |   | / |   |   |     |",
                  "|   |   |   |   | / |   |     |",
                  "|   |   |   |   |   | / |     |",
                  "|   |   |   |   |   |   |     |"]


    # find longest string length from names & emails
    for player in division:
        name = len(player['forename']) + len(player['surname']) + 1

        if name > longest:
            longest = name

        name = len(player['email']) + 1
        # debug print "%s %d" % (name, longest)

        if name > longest:
             longest = name

    divider = ''.ljust(longest, '-')
    print "%s--------------------------------------" % (divider)
    print "|     %-*s                               |" % (longest,"DIVISION " + str(division_number))
    print "%s--------------------------------------" % (divider)
    print "|   | %-*s | A | B | C | D | E | F | TOT |" % (longest,"NAME")
    print "%s--------------------------------------" % (divider)


    for player in division:
        name = player['forename']+ ' ' + player['surname']
        print "| %s | %-*s %s" % (chr(letter),longest,name,table_rows[row])
        print "|   | %-*s %s" % (longest,player['email'],table_rows[row])
        print "%s--------------------------------------" % (divider)
        letter = letter + 1
        row = row + 1

    # print out blank rows for partial divisions
    if len(division) < max_division:
        # debug print " missing %d" % (len(division))
        for i in range(len(division),max_division):
            print "| %s | %-*s %s" % (chr(letter),longest,' ',table_rows[6])
            print "|   | %-*s %s" % (longest,' ',table_rows[6])
            print "%s--------------------------------------" % (divider)
            letter = letter + 1


def print_division(division_number):
    """
    Prints a list of player names and emails for a specified division
    :param division_number the division to print the players from
    """
    if len(divisions[division_number]) > 0:
        if division_number == div_unavailable:
            print("UNAVAILABLE\n===========")
        elif division_number == div_absent:
            print("ABSENT\n======")
        else:
            print "DIVISION %1d\n==========" % (division_number)
        try:
            for player in divisions[division_number]:
                if division_number >= 1:
                    print "%s %s\n%s\n" % (player['forename'], player['surname'], player['email'])
                else:
                    print "%s %s" % (player['forename'], player['surname'])
            print ""
        except KeyError:
            print "Division not loaded :(\n"

def print_emails():
    """
    List players name and email address email - better if printed by division
    :return: none
    """
    for d in range(1,7):
        print_division(d)


def reset_players():
    del players[0:len(players)]
    divisions.clear()

def add_player(forename,surname,email,phone,division):
    """
    Adds a player to the league
    :param forename: Players forname
    :param surname: Players surname
    :param email: Players email
    :param phone: Players email
    :param division: Players division
    :return:
    """
    print ("add player stub")
    player = {'forename':'','surname':'','phone_number':'','email':'','division_current':0,'division_previous':0,'points_previous':0,'points_current':0}
    player['forename'] = forename
    player['surname'] = surname
    player['email'] = email
    player['phone_number'] = phone
    player['division_current'] = division
    #
    # add to player and divisions lists
    players.append(player)
    divisions[division].append(player)

def delete_player(forename,surname):
    """
    Delete a player from the players and divisions - assumes names are unique
    :param forename: Players forename to delete
    :param surname: Players surname to delete
    :return:
    """
    print ("delete player stub")
    for player in players:
        # lower case name match
        if (string.lower(player['forename'])==string.lower(forename)) and (string.lower(player['surname'])==string.lower(surname)):
            # delete this player from players list and divisions list
            div = player['division_current']
            players.remove(player)
            divisions[div].remove(player)


def print_players():
    """
    Prints the global list of players
    """
    print "PLAYERS\n=======\n"
    for player in players:
        print "forename: %s" % (player['forename'])
        print "surname: %s" % (player['surname'])
        print "email: %s" % (player['email'])
        print "phone_number: %s" % (player['phone_number'])
        print "division_current: %1d" % (player['division_current'])
        print "points_current: %2d" % (player['points_current'])
        print "division_previous: %1d" % (player['division_previous'])
        print "points_previous: %2d\n" % (player['points_previous'])

def load_players(filename):
    """
    :param filename: the filename to load
    :return: players
    """

    # save players by divisions
    #
    # absent and unavailable
    divisions[-1] = []
    divisions[0] = []
    # normal divisions
    divisions[1] = []
    divisions[2] = []
    divisions[3] = []
    divisions[4] = []
    divisions[5] = []
    divisions[6] = []
    player = {'forename':'','surname':'','phone_number':'','email':'','division_current':'','division_previous':'','points_previous':0,'points_current':0}
    f = open(filename,'r')
    for line in f:
        line = line.strip()
        line = line.split(':')
        if line[0] == "forename":
            #DEBUG
            #print "found new record " + line[1]
            if player['forename'] != '':
                # add to players list
                players.append(player)
                # add to divisions list
                divisions[player['division_current']].append(player)
            player = {'forename':'','surname':'','phone_number':'','email':'','division_current':'','division_previous':'','points_previous':0,'points_current':0}
            player['forename'] = line[1]
        if line[0] == "surname":
            player['surname'] = line[1]
        if line[0] == "phone_number":
            player['phone_number'] = line[1]
        if line[0] == "email":
            player['email'] = line[1]
        if line[0] == "division_current":
            player['division_current'] = int(line[1])
        if line[0] == "division_previous":
            player['division_previous'] = int(line[1])
        if line[0] == "points_previous":
            player['points_previous'] = int(line[1])
        if line[0] == "points_current":
            player['points_current'] = int(line[1])

    if player['forename'] != '':
        # add last player
        players.append(player)
        # add to divisions list
        divisions[player['division_current']].append(player)
    f.close()


def save_players(filename):
    """
    :param filename: the filename to save players data to

    """
    f = open(filename,'w')
    for player in players:
        line = "forename:" + player['forename'] + "\n"
        f.write(line)
        line = "surname:" + player['surname'] + "\n"
        f.write(line)
        line = "email:" + player['email'] + "\n"
        f.write(line)
        line = "phone_number:" + player['phone_number'] + "\n"
        f.write(line)
        line = "division_current:" + str(player['division_current']) + "\n"
        f.write(line)
        line = "points_current:" + str(player['points_current']) + "\n"
        f.write(line)
        line = "division_previous:" + str(player['division_previous']) + "\n"
        f.write(line)
        line = "points_previous:"+str(player['points_previous']) + "\n"
        f.write(line)
        f.write("\n")
    f.close()

def print_rules():
    print("League rules\n============")
    print("1. If a player is unable to turn up to play, for any reason, by the end of the round date, their opponent can claim 4 points.")
    print("2. At least 2 matches must be played to stay in the divisions.")
    print("3. A player who has the maximum or near the maximum points after the finishing round date may be promoted.")
    print("4. ANYONE WISHING TO JOIN THE DIVISIONS SHOULD WRITE THEIR NAME IN THE BLANK SPACE OF DIVISIONS 4, 5 or 6")
    print("   AND PLAY AS MANY MATCHES AS POSSIBLE. IF THESE SPACES ARE FILLED OR IF TOO LITTLE TIME REMAINS BEFORE ")
    print("   THE END OF THE CURRENT ROUND PLEASE WRITE YOUR NAME AND CONTACT NUMBER BELOW OR CONTACT THE LEAGUE ")
    print("   ORGANISER, JOHN DOE AT j.doe@anemailaddress.com. IF POSSIBLE, INDICATE THE LEVEL AT WHICH YOU WOULD")
    print("   LIKE TO ENTER. ANY SUGGESTIONS ARE WELCOME. ENCOURAGE OLD HANDS OR NEW ARRIVALS TO JOIN.")

def print_signup():
    print("\nList of players wishing to join the league:")
    print("NAME		tel no.		email				 Division?")
    print("______________________________________________________")

# This tests all the code modules if players.py is run directly rather than as an import
if __name__=="__main__":

    print __name__

    # test load print and save single players file
    load_players("../data/players.txt")
    #add_player("Tim","Jones","drkanukie@gmog.com","01480411300",4)
    print_table(6)
    #print_players()
    #delete_player("Tim","Jones")
    #print_division(4)
    #print_players()
    #print_division(1)
    #print_emails()
    #print_division(div_absent)
    #print_division(div_unavailable)
    #print_rules()
    #print_signup()
    #print_division(3)
    #print_division(1)
    #print_division(2)
    #save_players("../data/players_backup.txt")

