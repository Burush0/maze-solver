from graphics import Window
from maze import Maze

def main():
    num_rows = 30
    num_cols = 40
    margin = 50
    screen_x = 1200
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    maze.solve()

    win.wait_for_close()

main()