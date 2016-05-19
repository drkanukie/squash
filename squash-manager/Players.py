import string
import copy

"""
Code to maintain a list of squash players contained in players (a global variable) and saved to a text file players.txt
"""

# global players list & storage file
#
players = []
players_file = "../data/players.txt"

# players will be stored by division to make division tasks simpler
#
divisions = {}
#
# max size of a division
max_division = 6

# special codes for division_current values
#
div_unavailable = 0
div_absent = -1

# code for null edit value
#
edit_none = -2

##
## Print functions
##

def print_notice():
    """
    Print the noticeboard print out
    :return:
    """
    print_title()
    for t in range(1,7):
        # pretty print divisions tables
        print_table(t)
    print_points()
    print_rules()
    print_signup()

def print_table(division_number):
    """
    Prints out a players match table for the specified division
    :param division_number: the division table to print
    :return:
    """

    longest = 0
    letter = 65
    row = 0
    division = divisions[division_number]

    # table rows are preformatted - empty rows use the same values

    table_rows = ["| / |   |   |   |   |   |     |",
                  "|   | / |   |   |   |   |     |",
                  "|   |   | / |   |   |   |     |",
                  "|   |   |   | / |   |   |     |",
                  "|   |   |   |   | / |   |     |",
                  "|   |   |   |   |   | / |     |",
                  "|   |   |   |   |   | / |     |"]


    # find longest string length from names & emails in this division - use longest string for formatting space
    for player in division:
        # compare names and email for length
        name = len(player['forename']) + len(player['surname']) + 1
        if name > longest:
            # name longer
            longest = name

        name = len(player['email']) + 1
        if name > longest:
            # email longer
             longest = name

    # generate dynamic length divider
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
    print

def print_title():
    """
    Prints the title for the squash table print out
    :return:
    """
    print "                 STAFF SQUASH LEAGUE                     "
    print "  ALL GAMES MUST BE PLAYED BY 9 am Wed 27th APRIL 2016   "
    print "                 NEW PLAYERS WELCOME                     "
    print "JUST LEAVE CONTACT DETAILS ON THE BOTTOM PAGE (PEN ABOVE)\n"

def print_points():
    """
    Prints the points scoring table for the squash table print out
    :return:
    """
    print "Points scoring system - Play until one player has won three (3) games\n"
    print "\tPlayer 1\tPlayer 2\t Player 1\t Player 2"
    print "\tNo. wins\tNo. wins\t Points  \t Points"
    print "-------------------------------------------------"
    print "\tCompleted games "
    print "-------------------------------------------------"
    print "\t3       \t0        \t7        \t1"
    print "\t3       \t1        \t6        \t2"
    print "\t3       \t2        \t5        \t3"
    print "\tUnfinished games "
    print "-------------------------------------------------"
    print "\t2       \t2        \t4        \t4"
    print "\t2       \t1        \t5        \t3"
    print "\t2       \t0        \t6        \t2"
    print "\t1       \t1        \t4        \t4"
    print "\t1       \t0        \t5        \t3"
    print "\tOpponent doesn't turn up"
    print "-------------------------------------------------"
    print "\t0       \t0        \t4        \t0\n"



def print_rules():
    """
    Prints the squash league rules for the players sheet
    :return:
    """
    print("League rules\n============")
    print("1. If a player is unable to turn up to play, for any reason, by the end of the round date, their opponent can claim 4 points.")
    print("2. At least 2 matches must be played to stay in the divisions.")
    print("3. A player who has the maximum or near the maximum points after the finishing round date may be promoted.")
    print("4. ANYONE WISHING TO JOIN THE DIVISIONS SHOULD WRITE THEIR NAME IN THE BLANK SPACE OF DIVISIONS 4, 5 or 6")
    print("   AND PLAY AS MANY MATCHES AS POSSIBLE. IF THESE SPACES ARE FILLED OR IF TOO LITTLE TIME REMAINS BEFORE ")
    print("   THE END OF THE CURRENT ROUND PLEASE WRITE YOUR NAME AND CONTACT NUMBER BELOW OR CONTACT THE LEAGUE ")
    print("   ORGANISER, JOHN DOE AT j.doe@anemailaddress.com. IF POSSIBLE, INDICATE THE LEVEL AT WHICH YOU WOULD")
    print("   LIKE TO ENTER. ANY SUGGESTIONS ARE WELCOME. ENCOURAGE OLD HANDS OR NEW ARRIVALS TO JOIN.\n")

def print_signup():
    """
    Prints the sign up box for the league
    :return:
    """
    print("\nList of players wishing to join the league:")
    print("NAME		tel no.		email				 Division?")
    print("______________________________________________________\n")


##
## Email functions
##

def print_standing(division_number):
    division = divisions[division_number]
    if len(division) > 0:
        print "DIVISION %1d STANDING\n===================" % (division_number)
        # sort on points
        def getKey(item):
            return item['points_current']

        division = sorted(division, key=getKey, reverse=True)
        for player in division:
            print "%s %s %d points" % (player['forename'], player['surname'], player['points_current'])
        print

def print_division(division_number):
    """
    Prints a list of player names and emails for a specified division for emailing
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
    Prints list of all active players name and email address email - ordered by division
    :return: none
    """
    for d in range(1,7):
        print_division(d)

##
## Player operations
##

def update_divisions(number_promote):
    """
    Updates all the divisions and promotes the number of players provided
    :param number_promote: how many to promote or relegate
    :return:
    """

    # sort on points
    def getKey(item):
        return item['points_current']

    # deep copy divisions to stop churn as we edit
    edit_divisions = copy.deepcopy(divisions)
    for d in range(1,7):
        # debug print " d= %d " % (d)
        div = edit_divisions[d]
        # sort divisions for promotion & demotion so we can just take the first N up or down
        divp = sorted(div, key=getKey, reverse=True)
        divd = sorted(div, key=getKey)
        # debug print divp
        # debug print divd

        # promote top n up if not division 1
        if d != 1:
            # promoting n players up
            for p in range(0,number_promote):
                player = divp[p]
                #debug print "promote %s %s" % (player['forename'],player['surname'])
                edit_player(player['forename'],player['surname'],player['email'],player['phone_number'],d-1,0,d,player['points_current'])

        # demote top n down if not division 6
        if d != 6:
            # demoting n players down
            for p in range(0,number_promote):
                player = divd[p]
                #debug print "demote %s %s" % (player['forename'],player['surname'])
                edit_player(player['forename'],player['surname'],player['email'],player['phone_number'],d+1,0,d,player['points_current'])

        # reset points & division of players still in this division
        for player in div:
            # get canonical info that has been edited in previous passes
            info = get_player_info(player['forename'],player['surname'])
            if info['division_current'] == d:
                # still in the division save previous division and points and reset points
                #debug print "remains %s %s" % (player['forename'],player['surname'])
                edit_player(player['forename'],player['surname'],player['email'],player['phone_number'],d,0,d,player['points_current'])

def get_players():
    """
    Get the players list an array of player dictionaries
    :return: players list
    """
    return players

def get_none():
    """
    Get no edit code
    :return: edit_none global value for no edit
    """
    return edit_none

def edit_player(forename,surname,email,phone_number,division_current,points_current,division_previous,points_previous):
    """
    Edits specified player information
    :param forename: Player forename
    :param surname: Player surname
    :param email: Player email
    :param phone_number: Player phone number
    :param division_current: Players current division. Use div_unavailable or div_absent if player not in league this time
    :param points_current: Players current division points
    :param division_previous: Players previous division, 0 if no previous
    :param points_previous: Players previous division points, 0 if no previous
    :return:
    """

    for player in players:
        # lower case name match we assume player names are unique
        if (string.lower(player['forename'])==string.lower(forename)) and (string.lower(player['surname'])==string.lower(surname)):
            # only save valid edits ignore none
            if email != '':
                player['email'] = email
            if phone_number != '':
                player['phone_number'] = phone_number
            if division_current != edit_none:
                if player['division_current'] != division_current:
                    # division change need to shuffle divisions
                    divisions[player['division_current']].remove(player)
                    player['division_current'] = division_current
                    divisions[division_current].append(player)
            if points_current != edit_none:
                player['points_current'] = points_current
            if division_previous != edit_none:
                player['division_previous'] = division_previous
            if points_previous != edit_none:
                player['points_previous'] = points_previous

def add_player(forename,surname,email,phone,division):
    """
    Adds a player to the league division specified
    :param forename: Players forname
    :param surname: Players surname
    :param email: Players email
    :param phone: Players phone
    :param division: Players division to add them to, Use div_unavailable or div_absent if player not in league this time
    :return:
    """

    # Build player dictionary
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

def get_player_info(forename,surname):
    """
    Get the players info - assumes names are unique
    :param forename: Players forename to get info
    :param surname: Players surname to get info
    :return: player info as dict or empty dict if not found
    """

    # create a deep copy
    info = {}
    for player in players:
        # lower case name match
        if (string.lower(player['forename'])==string.lower(forename)) and (string.lower(player['surname'])==string.lower(surname)):
            # get info for this player
            info['forename'] = player['forename']
            info['surname'] = player['surname']
            info['email'] = player['email']
            info['phone_number'] = player['phone_number']
            info['division_current'] = player['division_current']
            info['points_current'] = player['points_current']
            info['division_previous'] = player['division_previous']
            info['points_previous'] = player['points_previous']

    return info

def delete_player(forename,surname):
    """
    Delete a player from the players and divisions - assumes names are unique
    :param forename: Players forename to delete
    :param surname: Players surname to delete
    :return:
    """
    for player in players:
        # lower case name match
        if (string.lower(player['forename'])==string.lower(forename)) and (string.lower(player['surname'])==string.lower(surname)):
            # delete this player from players list and divisions list
            div = player['division_current']
            players.remove(player)
            divisions[div].remove(player)

##
## File storage
##

def load_players(filename):
    """
    Load the players from the specified filename into the global players and divisions
    :param filename: The filename to load
    :return:
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
            #debug print "found new record " + line[1]
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
    Save the players list to the specified file
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

##
## Test
##
def print_players():
    """
    Test function prints the global list of players
    """
    print "PLAYERS\n=======\n"
    for player in players:
        print "forename: %s surname: %s" % (player['forename'],player['surname'])
        print "email: %s" % (player['email'])
        print "phone_number: %s" % (player['phone_number'])
        print "division_current: %1d" % (player['division_current'])
        print "points_current: %2d" % (player['points_current'])
        print "division_previous: %1d" % (player['division_previous'])
        print "points_previous: %2d\n" % (player['points_previous'])

def reset_players():
    """
    Test function to clear players list
    :return:
    """
    del players[0:len(players)]
    divisions.clear()

# This tests all the code modules if players.py is run directly rather than as an import
if __name__=="__main__":

    print __name__

    # test load print and save single players file
    load_players(players_file)
    print_players()
    #
    # Test print functions
    #
    print_emails()
    print_division(1)
    print_notice()
    #
    # Add points to division to test rollup and player edits
    #
    points = 12
    for player in players:
        edit_player(player['forename'],player['surname'],"","",edit_none,points,edit_none,edit_none)
        points = points - 2
        if points < 0:
            points = 12

    # check players are ranked
    print_standing(1)
    print_standing(2)
    print_standing(3)
    print_standing(4)
    print_standing(5)
    print_standing(6)
    #
    # Test read functions
    #
    # dict array
    print get_players()
    # -2
    print get_none()
    # dict
    print "%s" % get_player_info("John","Brown")['phone_number']
    print "%s" % get_player_info("Sarah","Brown")['email']

    # Edit functions
    add_player("Mickey","Mouse","mickey@gmail.com","01234567890",4)
    print_standing(4)
    delete_player("Mickey","Mouse")
    print_standing(4)

    print_standing(1)
    print_standing(2)
    print_standing(3)
    print_standing(4)
    print_standing(5)
    print_standing(6)
    # promote 2 up & down
    update_divisions(2)
    # two up from div 2
    print_standing(1)
    print_standing(2)
    print_standing(3)
    print_standing(4)
    print_standing(5)
    print_standing(6)
    # don't write to main file go and check new file for correct saved data
    save_players("../data/players_test.txt")

