gridSize = 10

def BattleShip(size):
    grid = [[0] * size for i in range(size)]
    for x in range(size):
        #aircraft carrier 5
        for i in range(1, 6):
            grid[1][i] = 5
        #submarine 1
        for i in range(2, 5):
            grid[i][9] = 6
        #submarine 2
        for i in range(1, 4):
            grid[7][i] = 9
        #torpido
        for i in range(7, 9):
            grid[9][i] = 2
        
        for i in range(1, 5):
            grid[5][i] = 4

        #Player
    playing = True
    ACsink = False
    SUB1sink = False
    SUB2sink = False
    TORsink = False
    Shipsink = False
    playerGrid = [['?'] * size for i in range(size)]
    while playing == True:
        x = int(input("Choose an x coordinate to fire: ")) - 1
        y = int(input("Choose a y coordinate to fire: ")) - 1
        
        
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("you didn't even hit the ocean, coordinates must be between 1 and 10...")
        elif playerGrid[y][x] == "H":
            print("You already shot there, try again")
        elif grid[y][x] > 1:
            for i in range(size):
                playerGrid[y][x] = "H"
                print(playerGrid[i])
            print("hit")
        
        elif x > 9 or x < 0 or y > 9 or y < 0:
            print("you didn't even hit the ocean, coordinates must be between 1 and 10...")
        else:
            for i in range(size):
                playerGrid[y][x] = "M"
                print(playerGrid[i])
            print("MISSED")
        

        #Check aircarft carrier sink
        if ACsink == False:
            if playerGrid[1][1] == "H" and playerGrid[1][2] == "H" and playerGrid[1][3] == "H" and playerGrid[1][4] == "H" and playerGrid[1][5] == "H":
                print("You sank the aircraft carrier!")
                ACsink = True
    
        #Check SUB1 sink
        if SUB1sink == False:
            if playerGrid[2][9] == "H" and playerGrid[3][9] == "H" and playerGrid[4][9] == "H":
                print("You sank a submarine!") 
                SUB1sink = True
        #Check SUB2 sink
        if SUB2sink == False:
            if playerGrid[7][1] == "H" and playerGrid[7][2] == "H" and playerGrid[7][3] == "H":
                print("You sank a submarine!") 
                SUB2sink = True
        #Check TOR sink
        if TORsink == False:
            if playerGrid[9][7] == "H" and playerGrid[9][8] == "H":
                print("You sank the torpedo boat!") 
                TORsink = True
        #Check Ship sink
        if Shipsink == False:
            if playerGrid[5][1] == "H" and playerGrid[5][2] == "H" and playerGrid[5][3] == "H" and playerGrid[5][4] == "H":
                print("You sank the ship!") 
                Shipsink = True

        #check if game is won
        Hcount = 0
        for i in range(size):
            for j in range(size):
                if playerGrid[i][j] == "H":
                    Hcount += 1
                    if Hcount == 17:
                        print("----YOU WON!!!----")
                        playing = False
    
BattleShip(gridSize)
    
