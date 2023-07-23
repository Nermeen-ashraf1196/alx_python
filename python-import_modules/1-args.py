#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len (sys.argv)-1
    if count == 0:
        print ("0 arguments")
    elif count ==1:
        print ("1 arguments")
    else:
        print ("{} arguments".format(count))
    for i in range (count):
        print ("{}: {}".format(i + 1, sys.argv[i + 1]))
        
    # arg = sys.argv
    #size = len(arg) - 1

   # if size > 1:
        #print("{} arguments:".format(size))
        #for i in range(1, size + 1):
            #print("{}: {}".format(i, arg[i]))

    #elif size == 0:
        #print("{} arguments.".format(size))

    #else:
        #print("{} argument:".format(size))
        #print("{}: {}".format(size, arg[1]))
