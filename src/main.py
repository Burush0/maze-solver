from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell2.draw(300, 300, 500, 500)

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.draw(125, 125, 225, 225)

    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.has_right_wall = False
    cell4.draw(250, 250, 275, 275)

    cell2.draw_move(cell3)

    cell3.draw_move(cell4, True)
    
    win.wait_for_close()

main()