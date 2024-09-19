import unittest
from scsi.grid import Grid

class TestGrid(unittest.TestCase):
    def test_grid_initialization(self):
        grid = Grid(levels=3)
        self.assertIsNotNone(grid)
        # Additional assertions

# Run the tests
if __name__ == '__main__':
    unittest.main()
