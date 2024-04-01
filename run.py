import random

class BattleshipGame:
    def __init__(self, size=5, num_ships=3):
        self.size = size
        self.num_ships = num_ships
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.generate_ships()
    print("BattleshipGame")
    