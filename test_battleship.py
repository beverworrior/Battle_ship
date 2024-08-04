# test_battleship.py
import unittest
from battleship import BattleshipGame

class TestBattleshipGame(unittest.TestCase):

    def setUp(self):
        # Create an instance of the game with a known state
        self.game = BattleshipGame(grid_size=5, num_ships=3, max_guesses=10)
        self.game.ships = [(0, 0), (1, 1), (2, 2)]  # Preset ships for testing

    def test_generate_ships(self):
        # Test that ships are generated within the grid and are unique
        self.game.generate_ships()
        for ship in self.game.ships:
            self.assertTrue(0 <= ship[0] < self.game.grid_size)
            self.assertTrue(0 <= ship[1] < self.game.grid_size)
        self.assertEqual(len(self.game.ships), self.game.num_ships)
        self.assertEqual(len(set(self.game.ships)), self.game.num_ships)  # Check uniqueness

    def test_check_guess_hit(self):
        # Test that a correct guess returns True and removes the ship
        result = self.game.check_guess(0, 0)
        self.assertTrue(result)
        self.assertNotIn((0, 0), self.game.ships)

    def test_check_guess_miss(self):
        # Test that an incorrect guess returns False
        result = self.game.check_guess(3, 3)
        self.assertFalse(result)
        self.assertEqual(len(self.game.ships), 3)  # No ships should be removed

    def test_play(self):
        # Simulate a playthrough to test the main loop
        self.game.ships = [(0, 0), (1, 1)]  # Set known ship locations for testing
        guesses = [(0, 0), (2, 2), (1, 1), (3, 3)]
        results = [self.game.check_guess(row, col) for row, col in guesses]
        self.assertEqual(results, [True, False, True, False])  # Expect hit, miss, hit, miss
        self.assertEqual(len(self.game.ships), 0)  # All ships should be sunk

if __name__ == "__main__":
    unittest.main()
