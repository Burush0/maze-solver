from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        fill_color = "white"

        walls = [
            (self.has_left_wall, Line(Point(x1, y1), Point(x1, y2))),
            (self.has_top_wall, Line(Point(x1, y1), Point(x2, y1))),
            (self.has_right_wall, Line(Point(x2, y1), Point(x2, y2))),
            (self.has_bottom_wall, Line(Point(x1, y2), Point(x2, y2)))
        ]

        for has_wall, wall in walls:
            self._win.draw_line(wall, fill_color if not has_wall else None)
        
    
    def draw_move(self, to_cell, undo=False):
        self_center = Point(
            (self._x2 + self._x1) // 2, 
            (self._y2 + self._y1) // 2
            )
        to_center = Point(
            (to_cell._x2 + to_cell._x1) // 2, 
            (to_cell._y2 + to_cell._y1) // 2
            )
        
        fill_color = "gray" if undo else "red"

        line = Line(self_center, to_center)
        self._win.draw_line(line, fill_color)
