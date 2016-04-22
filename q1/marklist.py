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
