'''
Code to maintain a list of players contained in players (a global variable)
'''
# empty players list
#
players = []
# players will be stored by division to make division tasks simpler
#
divisions = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[]}

keys = ["surname","forename","phone_number","email","division_previous","division_current","points_previous","points_current"]
unavailable = 0
absent = -1


def print_division(division_number):
    """
    :param division_number the division to print the players from
    """
    div = divisions[division_number]
    for player in div:
       print "%11s %11s %11s" % (player['forename'], player['surname'], player['email'])

def print_emails():
    """
    List players name and email address email - better if printed by division
    :return: none
    """
    for player in players:
        print "%11s %11s %11s" % (player['forename'], player['surname'], player['email'])

def reset_players():
    del players[0:len(players)]

def print_players():
    """
    Prints the global list of players
    """
    print "Players"
    for player in players:
        print "forename:%11s" % (player['forename'])
        print "surname:%11s" % (player['surname'])
        print "email:%11s" % (player['email'])
        print "phone_number:%11s" % (player['phone_number'])
        print "division_current:%9d" % (player['division_current'])
        print "points_current:%9d" % (player['points_current'])
        print "division_previous:%9d" % (player['division_previous'])
        print "points_previous:%9d" % (player['points_previous'])
        print

def load_players(filename):
    """
    :param filename: the filename to load
    :return: players
    """
    player = {'forename':'','surname':'','phone_number':'','email':'','division_current':'','division_previous':'','points_previous':0,'points_current':0}
    f = open(filename,'r')
    for line in f:
        line = line.strip()
        line = line.split(':')
        if line[0] == "forename":
            print "found new record " + line[1]
            if player['forename'] != '':
                players.append(player)
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
        players.append(player)
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


# This tests all the code modules if players.py is run directly rather than as an import
if __name__=="__main__":

    print __name__

    # test load print and save single players file
    load_players("../data/players.txt")
    print_players()
    save_players("../data/players_backup.txt")

