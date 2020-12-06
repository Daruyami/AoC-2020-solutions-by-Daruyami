import re

file = open("d4p1input.txt")

reqid=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
lid=""
idc = 0
cidc = 0
for x in file:
    if(x != "\n"):
        lid += str(x)
        continue
    idc+=1
    line = re.split("\s", lid)
    lid = ""
    if(line[ (len(line)-1) ] == ""):
        line.pop( (len(line)-1) )
    
    cc = 0
    creqid = reqid[:]
    #print(line)
    #print(line[0][:3])
    for a in range(0, len(line), 1):
        if(str(line[a][:3]) == "cid"):
            continue
        for b in range(0, len(creqid), 1):
            if( str(line[a][:3]) == str(creqid[b]) ):
                cc+=1
                creqid.pop(b)
                break
    if(cc == 7):
        cidc+=1
    
    
    #abcabc
print(lid)
file.close()
print("Read ", idc, " ids")
print("Correct ids count is equal to: ", cidc)
