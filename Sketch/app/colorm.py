from tkinter import Frame, Label, Scale, Button, Canvas, Tk, GROOVE
import sys
sys.path.append('app')
from config import SIZE, BORDER_W, BLACK


class ColorMaker(Frame):
    def __init__(self,
                 master: Tk,
                 font: tuple[str, int, str],
                 sizes: tuple[int, int],
                 pos: tuple[int, int]) -> None:
        super().__init__(master, width=sizes[0], height=sizes[1], relief=GROOVE)
        self.place(x=pos[0], y=pos[1])
        self.config(borderwidth=BORDER_W)
        # self.config(bg='black')
        self.color: str = ''
        self.confirmed: bool = False

        # Red 
        lbl1_pos: tuple[int, int] = 0, 0
        self.label_r: Label = Label(self, text='R', font=font, relief=GROOVE)
        self.label_r.place(x=lbl1_pos[0], y=lbl1_pos[1])
        sb1_pos: tuple[int, int] = SIZE, lbl1_pos[1]
        sb_length: int = SIZE * 18
        self.slider1: Scale = Scale(self, from_=0, to=255, orient='horizontal', font=font, relief=GROOVE)
        self.slider1.place(x=sb1_pos[0], y=sb1_pos[1])
        self.slider1.config(length=sb_length)

        # Green
        lbl_dy: int = int(SIZE * 2.5)
        lbl2_pos: tuple[int, int] = lbl1_pos[0], lbl_dy
        self.label_g: Label = Label(self, text='G', font=font, relief=GROOVE)
        self.label_g.place(x=lbl2_pos[0], y=lbl2_pos[1])
        sb2_pos: tuple[int, int] = sb1_pos[0], lbl2_pos[1]
        self.slider2: Scale = Scale(self, from_=0, to=255, orient='horizontal', font=font, relief=GROOVE)
        self.slider2.place(x=sb2_pos[0], y=sb2_pos[1])
        self.slider2.config(length=sb_length)

        # Blue
        lbl3_pos: tuple[int, int] = lbl1_pos[0], lbl_dy * 2
        self.label_b: Label = Label(self, text='B', font=font, relief=GROOVE)
        self.label_b.place(x=lbl3_pos[0], y=lbl3_pos[1])
        sb3_pos: tuple[int, int] = sb1_pos[0], lbl3_pos[1]
        self.slider3: Scale = Scale(self, from_=0, to=255, orient='horizontal', font=font, relief=GROOVE)
        self.slider3.place(x=sb3_pos[0], y=sb3_pos[1])
        self.slider3.config(length=sb_length)

        # Button check
        btn1_pos: tuple[int, int] = lbl1_pos[0], lbl3_pos[1] + lbl_dy
        btn1_txt: str = 'Check'
        self.button_check: Button = Button(self, text=btn1_txt, font=font, relief=GROOVE, command=self.get_color)
        self.button_check.place(x=btn1_pos[0], y=btn1_pos[1])

        # Button confirm
        btn2_pos: tuple[int, int] = sizes[0] - SIZE * 5, btn1_pos[1]
        btn2_txt: str = 'Confirm'
        self.button_confirm: Button = Button(self, text=btn2_txt, font=font, relief=GROOVE, command=self.change)
        self.button_confirm.place(x=btn2_pos[0], y=btn2_pos[1])

        # Canvas check
        color: str = BLACK
        cv_sizes: tuple[int, int] = SIZE * 10, lbl_dy
        cv_pos: tuple[int, int] = btn1_pos[0] + SIZE * 4, btn1_pos[1]
        self.canvas_check: Canvas = Canvas(self, bg=color, width=cv_sizes[0], height=cv_sizes[1])
        self.canvas_check.place(x=cv_pos[0], y=cv_pos[1])

    def change(self) -> None:
        """Sets confirmed value to True. Used for changing line color on a canvas"""
        self.confirmed = True

    def get_color(self) -> None:
        """Sets color it's new value. color variable is used by the canvas object of the 
        main module to change the color of the line"""
        self.confirmed = False
        color: tuple[int, int, int] = self.get_rgb()
        self.color: str = '#%02x%02x%02x' % color
        self.canvas_check.config(bg=self.color)

    def get_rgb(self) -> tuple[int, int, int]:
        """Returns choosen color in rgb format"""
        r: int = int(self.slider1.get())
        g: int = int(self.slider2.get())
        b: int = int(self.slider3.get())
        return r, g, b
