import random

class BattleshipGame:
    def __init__(self, size=5, num_ships=3):
        self.size = size
        self.num_ships = num_ships
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.generate_ships()

def generate_ships(self):
        for _ in range(self.num_ships):
            ship_row = random.randint(0, self.size - 1)
            ship_col = random.randint(0, self.size - 1)
            while (ship_row, ship_col) in self.ships:
                ship_row = random.randint(0, self.size - 1)
                ship_col = random.randint(0, self.size - 1)
            self.ships.append((ship_row, ship_col))
            print("Hello Ocean")
    
   