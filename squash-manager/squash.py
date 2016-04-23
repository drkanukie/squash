# import marklist
# using dictionaries to control data
while True:
    print "\n  - Please choose from  the following options:\n"
    print "\t1 - To Print out the list of  players and all relevant information \n"
    print "\t2 - To Print out list of players E-mail addresses\n"
    print "\t3 - To print a list of players from division (1-7) \n"
    print "\t4 - To add players to division\n"
    print "\t5 - To delete players from a division\n"
    print "\t6 - To edit information on players\n"
    print "\t7 - To see division standings\n"
    print "Or enter 'q' to quit\n"
    option = raw_input("\t: ")
    if option == "1":
        #marklist.list_modules()
        print "1"
    elif option == "2":
        filename = raw_input("\n\tPlease enter the file name to read from: ")
        #marklist.read_modules(filename)
        print "\n\tModules read in from file.\n"
    elif option == "3":
        module = raw_input("\n\t\tPlease enter the module code: ")
        credits = raw_input("\n\t\tPlease enter the credits for the module: ")
        mark = raw_input("\n\t\tPlease enter the mark for the module: ")
        #marklist.add_module(module,credits,mark)
        print "\n\tModule added.\n"
    elif option == "4":
        filename = raw_input("\n\t\tPlease enter the file name to write to: ")
        #marklist.write_modules(filename)
    elif option == "5":
        #marklist.reset_marklist()
        print "\n\tMarklist reset.\n"
    elif option == "q":
        break

