from tkinter import Tk, Canvas
from tkinter import SUNKEN
import sys
sys.path.append('app')
from enumerations import DrawMode
from config import BORDER_W, BLACK, LINE_W, CANVAS_COLOR


class MyCanvas(Canvas):
    def __init__(self,
                 master: Tk,
                 sizes: tuple[int, int],
                 pos: tuple[int, int]) -> None:
        super().__init__(master, width=sizes[0], height=sizes[1])
        self.place(x=pos[0], y=pos[1])
        self.config(relief=SUNKEN, borderwidth=BORDER_W, bg=CANVAS_COLOR)
        self.bind('<Button-1>', self.draw)
        self.color: str = BLACK
        self.line_w: int = LINE_W

        # Draw common
        self.mode: int = DrawMode.LINE
        self.points: list[tuple[int, int]] = []

    def draw(self, event) -> None:
        """Draws objects, depending on mode value"""
        if self.mode == DrawMode.NONE:
            self.points.clear()
            return
        pos: tuple[int, int] = event.x, event.y
        self.points.append(pos)
        if self.mode == DrawMode.LINE:
            self.draw_line()
        elif self.mode == DrawMode.CIRCLE:
            self.draw_circle()
        elif self.mode == DrawMode.RECT:
            self.draw_rect()
        else:
            self.points.clear()

    def draw_rect(self) -> None:
        """Draws rectangle on a creen"""
        if len(self.points) == 2:
            x0, y0, x1, y1 = self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1]
            self.create_rectangle(x0, y0, x1, y1, fill=self.color, width=self.line_w)
            self.points.clear()
        if len(self.points) > 2:
            self.points.clear()

    def draw_circle(self) -> None:
        """Draws oval on a screen"""
        if len(self.points) == 2:
            x0, y0, x1, y1 = self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1]
            self.create_oval(x0, y0, x1, y1, fill=self.color, width=self.line_w)
            self.points.clear()
        if len(self.points) > 2:
            self.points.clear()

    def draw_line(self) -> None:
        """Draws line on a canvas"""
        if len(self.points) == 2:
            x0, y0, x1, y1 = self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1]
            self.create_line(x0, y0, x1, y1, fill=self.color, width=self.line_w)
            self.points.clear()
        if len(self.points) > 2:
            self.points.clear()

