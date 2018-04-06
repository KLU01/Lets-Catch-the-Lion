from graphics import *

def main():
    win = GraphWin('Face', 1000, 1000) # give title and dimensions
    c = Circle(Point(500,500), 100)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()
