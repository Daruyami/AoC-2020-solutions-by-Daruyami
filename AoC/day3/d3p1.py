tnbr=0
dnbr=0
wnbr=0
lplace = 0
mult=1
for slope in range(1, 8, 2):
    file = open("d3p1input.txt")
    for x in file:
        line = str(x)
        lmax = len(line)-1
        if(line[lplace] == "#"):
            tnbr+=1
        elif(line[lplace] == "."):
            dnbr+=1
        else:
            wnbr+=1
        lplace+=slope
        if(lplace >= (lmax)):
            lplace-=lmax
    file.close()
    print("For slope: ", slope)
    print("Trees: ", tnbr)
    print("Dots: ", dnbr)
    print("wtf's: ", wnbr)
    mult*=tnbr
    tnbr=0
    dnbr=0
    wnbr=0
    lplace=0
    
slope = 1
a=0
file = open("d3p1input.txt")
for x in file:
    a+=1
    if((a%2)==1):
        line = str(x)
        lmax = len(line)-1
        if(line[lplace] == "#"):
            tnbr+=1
        elif(line[lplace] == "."):
            dnbr+=1
        else:
            wnbr+=1
        lplace+=slope
        if(lplace >= (lmax)):
            lplace-=lmax
mult*=tnbr
file.close()
print("For slope: 1, 2")
print("Trees: ", tnbr)
print("Dots: ", dnbr)
print("wtf's: ", wnbr)

print("\nResult: ", mult)
