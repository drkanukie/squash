'''
Code to maintain a list of players contained in players (a global variable)
'''
players = ["tim","ed"]
keys = ["surname","forename","phone_number","email","division","points_previous","points_current"]

def print_players():
    """
    Prints the global list of players
    """
    print "Players"
    for player in players:
        print "%11s" % (player)

# This tests all the code modules if players.py is run directly rather than as an import
if __name__=="__main__":

    print __name__
    print_players()
