'''
Code to maintain a list of marks contained in marklist (a global variable)
'''
marklist = []

def add_module(module_code,credits,mark):
    """
    Adds list [module_code,credits,mark] to marklist
        module_code = a module code (string), e.g. COF180
        credits = no. of credits (int), e.g. 10
        mark = mark in % (int), e.g. 57
    e.g. if marklist is [["CMF100",10,23]] then calling
    add_module("COF180",10,57) changes it to
    [["CMF100",10,23],["COF180",10,57]]
    """

    marklist.append([module_code,credits,mark])

def list_modules():
    """
    Prints a nicely formatted listing of the contents of marklist
    """

    print "module_code   credits     mark"
    for mark in marklist:
        print "%11s%10d%9d" % (mark[0],mark[1],mark[2])

def total_credits():
    """
    Returns the total number of credits (int)
    """
    total=0
    for mark in marklist:
        total = total + mark[1]
    return total

def average_mark():
    """
    Returns the average mark (float)
    """
    total=0
    for mark in marklist:
        total = total + mark[2]

    return float(total)/len(marklist)

def delete_module(module_code):
    """
        Deletes a module from marklist
            module_code = a module code (string), e.g. COF180
    """
    for mark in marklist:
        if mark[0] == module_code:
            del marklist[marklist.index(mark)]

def read_modules(filename):
    '''
        Opens a file in which a line is formatted as:
            module_code;credits;mark
        e.g.
            COF180;10;73
        Eah line is read and the data added to marklist.
        Finally the file is closed.
        Parameters:
            filename = the file to open (string)
    '''

    f = open(filename,'r')
    for line in f:
        line = line.strip()
        line = line.split(';')
        add_module(line[0], int(line[1]), int(line[2]))
    f.close()

def write_modules(filename):
    '''
        Opens a file for writing an writes out all the
        data contained in marklist in the format:
            module_code;credits;mark
        e.g.
            COF180;10;73
            COF181;10;81
        Finally the file is closed.
        Parameters:
            filename = the file to open (string)
        '''
    
    f = open(filename,'w')
    for mark in marklist:
        line = mark[0]+";"+str(mark[1])+";"+str(mark[2])+"\n"
        f.write(line)
    f.close()


def reset_marklist():
    '''
        Set marklist to be an empty list.
    '''
    del marklist[0:len(marklist)]

if __name__=="__main__":

    print __name__
    list_modules()
    add_module("CMF100",10,23)
    list_modules()
    add_module("COF180",10,57)
    list_modules()
    print total_credits()
    print average_mark()
    delete_module("COF180")
    list_modules()
    read_modules('marks.txt')
    list_modules()
    write_modules('marksNew.txt')
    reset_marklist()
    list_modules()