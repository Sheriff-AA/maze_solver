from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.color = "black"
        self.width = 1

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)