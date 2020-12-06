file = open("d2p1input.txt")
lcount = 0
for line in file:
    lcount+=1
file.close()
file = open("d2p1input.txt")

ccount = 0
nccount = 0
for x in range(0, lcount, 1):
    line = file.readline()
    lminstr = ""
    y = 0
    for y in range(0, len(line), 1):
        if (line[y] != "-"):
            lminstr += line[y]
        else:
            break
    lmin = int(lminstr)

    y+=1
    lmaxstr = ""
    z = 0
    for z in range(y, len(line), 1):
        if (line[z] != " "):
            lmaxstr += line[z]
        else:
            break
    lmax = int(lmaxstr)

    z+=1
    lchar = ""
    lchar = line[z]

    z+=3
    lstring = ""
    for w in range(z, len(line), 1):
        lstring += line[w]
    
    lsccount = 0
    for v in range(0, len(lstring), 1):
        if(str(lstring[v]) == str(lchar)):
            lsccount += 1
    if (lsccount >= lmin and lsccount <= lmax):
        ccount += 1
    
    #print("-----------------------\n", line, "\n", str((str(lmin)+"-"+str(lmax)+" "+lchar+": "+lstring)))
    
    if( (lstring[(lmin-1)] == lchar) ^ (lstring[(lmax-1)] == lchar) ):
        nccount += 1

print("Part 1 result: "+str(ccount))
print("Part 2 result: "+str(nccount))
