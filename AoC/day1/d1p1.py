#aoc 2020 d1p1
#wczytuje plik do arraya input
file = open("d1p1input.txt")
input = []
for x in file:
    input.append(x)
#usuwa ostatnią pustą linijke
input.pop()
#start wyszukiwania
for x in range(0, len(input), 1):
    for y in range(0, len(input), 1):
        a = int(input[x])
        if( ( int(a+ int(input[y]))) == int(2020) ):
            print( "Wynik to: ", int(a*int(input[y])) )
            
            

for x in range(0, len(input), 1):
    for y in range(0, len(input), 1):
        for z in range(0, len(input), 1):
            a = int(input[x])
            if( (int(a + int(input[y]) + int(input[z]))) == int(2020) ):
                print("Drugi wynik to: ", int(a * int(input[y]) * int(input[z])))
