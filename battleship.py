import random


import random

class BattleshipGame:
    def __init__(self, grid_size=5, num_ships=3, max_guesses=10):
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.max_guesses = max_guesses
        self.board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ships = []
        self.generate_ships()

    def generate_ships(self):
        while len(self.ships) < self.num_ships:
            ship_location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            if ship_location not in self.ships:
                self.ships.append(ship_location)

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def check_guess(self, row, col):
        if (row, col) in self.ships:
            self.board[row][col] = 'X'
            self.ships.remove((row, col))
            return True
        else:
            self.board[row][col] = 'M'
            return False

    def play(self):
        guesses = 0
        while guesses < self.max_guesses and len(self.ships) > 0:
            self.print_board()
            try:
                row = int(input("Enter row (1-5): ")) - 1
                col = int(input("Enter col (1-5): ")) - 1
                if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                    print("Invalid input. Please enter numbers between 1 and 5.")
                    continue
                if self.check_guess(row, col):
                    print("Hit!")
                else:
                    print("Miss.")
                guesses += 1
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        if len(self.ships) == 0:
            print("Congratulations! You've sunk all the ships!")
        else:
            print("Game over! You've used all your guesses.")