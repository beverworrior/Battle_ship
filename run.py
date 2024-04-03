import random


class BattleshipGame:
    def __init__(self, size=5, num_ships=3):
        self.size = size
        self.num_ships = num_ships
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.generate_ships()

    # This is for randomizing the location of the ships.
    def generate_ships(self):
        for _ in range(self.num_ships):
            ship_row = random.randint(0, self.size - 1)
            ship_col = random.randint(0, self.size - 1)
            while (ship_row, ship_col) in self.ships:
                ship_row = random.randint(0, self.size - 1)
                ship_col = random.randint(0, self.size - 1)
            self.ships.append((ship_row, ship_col))

    # Create the grid for the board.
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    # This is to check if I have hit or missed my target.
    def check_guess(self, guess_row, guess_col):
        if (guess_row, guess_col) in self.ships:
            print("Congratulations! You sunk my battleship!")
            self.board[guess_row][guess_col] = 'X'
            self.ships.remove((guess_row, guess_col))
        else:
            print("You missed my battleship!")
            self.board[guess_row][guess_col] = 'M'

    def play(self):
        print("Let's play Battleship! You have 10 Guesses to sink my 3 ship!")
        self.print_board()
        num_guesses = 0
        while self.ships:
            guess_row = int(input("Guess Row: ")) - 1
            guess_col = int(input("Guess Col: ")) - 1
            if guess_row < 0 or guess_row >= self.size:
                print("Oops, that's not even in the ocean.")
            elif (self.board[guess_row][guess_col] == 'X' or
                  self.board[guess_row][guess_col] == 'M'):
                print("You guessed that one already.")
            else:
                num_guesses += 1
                self.check_guess(guess_row, guess_col)
                self.print_board()
                if num_guesses >= 2 * self.size:
                    print("Game Over! You've reach the max number of guess")
                    break
        if not self.ships:
            print("Congratulations! You've sunk all the battleships!")


# Run the game
if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
