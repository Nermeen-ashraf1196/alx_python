#for x in range (0,99):
#    print(x,'=',hex(x))
txt = "{0} = {0:X}"
for x in range(0,99):
    print(txt.format(x))