import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_large(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m1._cells[0][0]
        exit_col = num_cols - 1
        exit_row = num_rows - 1
        exit_cell = m1._cells[exit_col][exit_row]
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)
    
    def test_maze_reset_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()