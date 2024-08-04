# Battleship Game

This is a simple implementation of the classic Battleship game in Python.

- [Repository](https://github.com/beverworrior/Battle_ship.git)
- [Play Online](https://battleship92-b8f2d624a056.herokuapp.com)

## Users

The goal of the game is for the player to sink three ships before reaching a maximum of 10 guesses.

## Getting Started

To play the game, follow these steps:

1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Run the game and follow the on-screen instructions.

## Gameplay Instructions

1. Upon starting the game, you will see the game board represented as a grid of cells.
2. Enter the row and column coordinates to make a guess. Enter a number between 1-5 for both the row and the column.
3. If your guess hits a battleship, you'll be notified, and the respective cell on the board will be marked as 'X'.
4. If your guess misses, you'll be notified, and the respective cell on the board will be marked as 'M'.
5. Continue guessing until you sink all the battleships or reach the maximum number of guesses.
6. The game ends when you either sink all the battleships or exceed the maximum number of guesses.

## Future Enhancements

Potential future improvements include:

- Expanding the grid size and adding more ships.
- Allowing players to enter their names before starting the game.
- Implementing a high score system to track how quickly players sink the ships.

## Code Structure

The code consists of the following components:

- `BattleshipGame` class: Implements the game logic, including board initialization, ship generation, and gameplay mechanics.
- Methods:
  - `__init__`: Initializes the game with default or custom parameters.
  - `generate_ships`: Generates battleships at random locations on the board.
  - `print_board`: Prints the current state of the game board.
  - `check_guess`: Checks if the guess hits a battleship or not.
  - `play`: Initiates the game loop and handles user input.

## Requirements

- Python 3

## Testing

![PEP8 Validation](Testing.png)

## Deployment to Heroku

To deploy this game on Heroku, follow these steps:

1. Create an account on Heroku or log in if you already have one.
2. Connect your GitHub repository to Heroku.
3. Create a new app and go to the settings where you can name your app and choose buildpacks: Python and Node.js (in that order).
4. Click the deploy button and wait for all settings to complete from Git. Enjoy your deployed app.
