from cell import Cell
import time, random

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
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
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
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        if len(self._cells) != 0:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            exit_col = self._num_cols - 1
            exit_row = self._num_rows - 1
            self._cells[exit_col][exit_row].has_bottom_wall = False
            self._draw_cell(exit_col, exit_row)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(len(to_visit))
            to_cell = to_visit[direction]
            next_i, next_j = to_cell
            self._break_wall_between(i, j, next_i, next_j)
            self._break_walls_r(next_i, next_j) 

    
    def _break_wall_between(self, cur_i, cur_j, next_i, next_j):
        if next_i == cur_i + 1:
            self._cells[cur_i][cur_j].has_right_wall = False
            self._cells[next_i][cur_j].has_left_wall = False
        if next_i == cur_i - 1:
            self._cells[cur_i][cur_j].has_left_wall = False
            self._cells[next_i][cur_j].has_right_wall = False
        if next_j == cur_j + 1:
            self._cells[cur_i][cur_j].has_bottom_wall = False
            self._cells[cur_i][next_j].has_top_wall = False
        if next_j == cur_j - 1:
            self._cells[cur_i][cur_j].has_top_wall = False
            self._cells[cur_i][next_j].has_bottom_wall = False
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
