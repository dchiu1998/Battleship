from random import randint

def play():
    p1 = Player(ships, size)
    p2 = Player(ships, size)
    turn = 1
    exit = False
    print("***** Let's begin! *****")
    while(exit == False):
        print("\n***Turn %d***" %(turn))
        print("Enter <0> to quit any time")
        
        # Player 1 turn
        print("\n<Player 1>")
        print("Coordinates attacked so far:", p2.get_enemy_strikes())
        row = int(input("Enter Row: "))
        if(row == 0):
            print("Exiting...")
            break
        col = int(input("Enter Column: "))
        if(col == 0):
            print("Exiting...")
            break
        p2.hit(row,col)
        if(p2.is_out_of_ships() == True):
            print("Player 2 is out of ships. Player 1 wins!")
            exit = True
        
        # Player 2 turn
        if(exit != True):
            print("\n<Player 2>")
            print("Coordinates attacked so far:", p1.get_enemy_strikes())
            row = int(input("Enter Row: "))
            if(row == 0):
                print("Exiting...")
                break
            col = int(input("Enter Column: "))
            if(col == 0):
                print("Exiting...")
                break
            p1.hit(row,col)
            if(p1.is_out_of_ships() == True):
                print("Player 1 is out of ships. Player 2 wins!")
                exit = True
        turn += 1
    
class Player():
    
    def __init__(self, ships:int=5, length:int=10):
        self._numShips = ships
        self._gridLength = length
        self._grid = []
        self._enemy_attacks = []
        self._generate_ship_coords(self._numShips, self._gridLength)
        
    def _generate_ship_coords(self, ships:int, length:int):
        print("Generating ships...")
        count = 0
        while(count < ships):
            newShip = (randint(1,length),randint(1,length))
            if(newShip not in self._grid):
                self._grid.append(newShip)
                count += 1
        print("Done!")
    
    def _reveal(self):
        print(self._grid)
        
    def remove_ship(self, row:int, col:int):
        self._grid.remove((row,col))
        
    def add_ship(self, row:int, col:int):
        if ((row,col) not in self._grid):
            self._grid.append((row,col))
            return True
        else:
            return False
                              
    def hit(self, row:int, col:int):
        if((row,col) in self._grid):
            self.remove_ship(row,col)
            print("A ship has been sunken!")
        else:
            if((row,col) not in self._enemy_attacks):
                self._enemy_attacks.append((row,col))
            print("That was a miss...")
            
    def is_out_of_ships(self):
        return self._grid == []
    
    def get_enemy_strikes(self):
        return self._enemy_attacks
        
        
setup = False
size = 0
ships = 0
print("***** Welcome to Battleship! *****\n")
while(setup == False):
    size = int(input("Please enter length of the square grid (2 to 10): "))
    if (size < 2 or size > 10):
        print("Length must be between 2 and 10 ")
    else:
        setup = True

while(setup == True):
    ships = int(input("Please enter how many ships to be in the game: "))
    if (ships >= size*size):
        print("Please enter a number less than %d (You have a %s grid)" % (size*size, "%d x %d" % (size, size)))
    else:
        setup = False
# start game
play()
print("Game has ended.")