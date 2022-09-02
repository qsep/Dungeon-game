
print("Welcome to the dungeon.\nUse WASD to move forward, left, back and right. \nOn the right of your screen, the map of the dungeon will be shown.\nThe map code is:\np = player (you)\no = empty tile\n▓ = wall\ne = enemy\ns = stairs(exit).\n\n")

playercoords = [0,0]
esc = 0

map0 = '\n\n▓soo▓\n▓▓▓o▓\n▓ooo▓\n▓o▓▓▓\npoo▓▓'
print(map0)
map0 = '\n\n▓soo▓\n▓▓▓o▓\n▓ooo▓\n▓o▓▓▓\nooo▓▓'

tempmap = list(map0)

def map_build(coordtype, coordchange):
    
    global map0 , esc
    tempmap = list(map0)
    
    playercoords[coordtype] += coordchange
    mult = 26-(6*playercoords[1]) + playercoords[0]

    if mult <= 30 and mult >= 0:
        if  tempmap[mult] == 'o':
            tempmap[mult] = 'p'
            tempmap2 ="".join(tempmap)
            print(tempmap2)

        elif tempmap[mult] == 's':
            tempmap[mult] = 'p'
            tempmap2 ="".join(tempmap)
            print(tempmap2)
            esc =  1
            return

        else: 
            playercoords[coordtype] -= coordchange
            print("You cant go there, a wall's in the way!")
            wallmult = 26-(6*playercoords[1]) + playercoords[0]
            tempmap[wallmult] = 'p'
            tempmap2 ="".join(tempmap)
            print(tempmap2)

    else: 
        playercoords[coordtype] -= coordchange
        print("You cant go there, you'll fall to the void!")
        wallmult = 26-(6*playercoords[1]) + playercoords[0]
        tempmap[wallmult] = 'p'
        tempmap2 ="".join(tempmap)
        print(tempmap2)



while playercoords[0] <5 and playercoords[1] < 5:
    
    keydown = input()
    
    if esc == 0:
        if keydown == 'w':map_build(1, 1)

        if keydown == 'a':map_build(0, -1)

        if keydown == 's':map_build(1, -1)
        
        if keydown == 'd':map_build(0, 1)

    elif esc == 1:
        print("Congratulations on beating the tutorial! Now, lets enter the real thing...")
        break

 