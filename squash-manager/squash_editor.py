# import marklist
# using dictionaries to control data
while True:
    print "\nPlease choose from  the following options:\n"
    print "\t1 - Print out the current mark list\n"
    print "\t2 - Add marks from file\n"
    print "\t3 - Add a mark from the keyboard\n"
    print "\t4 - Write marks to file\n"
    print "\t5 - Empty the mark list\n"
    print "Or enter 'q' to quit\n"
    option = raw_input("\t: ")
    if option == "1":
        #marklist.list_modules()
        1print "1"
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

