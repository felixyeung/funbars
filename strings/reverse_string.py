while(True):
    my_string = raw_input("Enter string (Blank to terminate): ")
    if (my_string == ""):
        break;
    print "By list comprehension: {0}".format(my_string[::-1])

    reversed = ""
    for x in range(len(my_string) - 1, -1, -1):
        reversed += my_string[x]
    print "By looping from end: {0}".format(reversed)
