from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        if len(self._cells) != 0:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            exit_col = self._num_cols - 1
            exit_row = self._num_rows - 1
            self._cells[exit_col][exit_row].has_bottom_wall = False
            self._draw_cell(exit_col, exit_row)