from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point1 = Point(20, 40)
    point2 = Point(100, 400)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()