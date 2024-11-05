from tkinter import Tk, Frame, Label, Scale, Button, GROOVE
from tkinter.ttk import Combobox
import sys
sys.path.append('app')
from config import SIZE, LINE_W, BORDER_W
from enumerations import DrawMode


class DrawSettings(Frame):
    def __init__(self,
                 master: Tk,
                 pos: tuple[int, int],
                 sizes: tuple[int, int],
                 font: tuple[str, int, str]) -> None:
        super().__init__(master, width=sizes[0], height=sizes[1], borderwidth=BORDER_W, relief=GROOVE)
        self.place(x=pos[0], y=pos[1])
        self.width_mode: tuple[int, int] = LINE_W, DrawMode.LINE
        self.changed: bool = False

        # Line width
        max_line_w: int = LINE_W * 100
        lbl1_txt: str = 'Line width'
        lbl1_pos: tuple[int, int] = 0, 0
        self.lbl_l: Label = Label(self, text=lbl1_txt, font=font, relief=GROOVE)
        self.lbl_l.place(x=lbl1_pos[0], y=lbl1_pos[1])
        sb_pos: tuple[int, int] = SIZE * 5, lbl1_pos[1]
        sb_length: int = SIZE * 14
        self.slider: Scale = Scale(self, from_=0, to=max_line_w, orient='horizontal', relief=GROOVE, font=font)
        self.slider.place(x=sb_pos[0], y=sb_pos[1])
        self.slider.config(length=sb_length)

        # Draw mode
        self.modes: list[str] = ['none', 'line', 'circle', 'rect'] 
        lbl2_txt: str = 'Draw mode'
        dy: int = int(SIZE * 2.5)
        lbl2_pos: tuple[int, int] = lbl1_pos[0], dy
        self.lbl_m: Label = Label(self, text=lbl2_txt, font=font, relief=GROOVE)
        self.lbl_m.place(x=lbl2_pos[0], y=lbl2_pos[1])
        cb_pos: tuple[int, int] = SIZE * 5, lbl2_pos[1]
        cb_w: int = int(SIZE * .3)
        self.cb: Combobox = Combobox(self, state='readonly', font=font, values=self.modes)
        self.cb.set(self.modes[1])
        self.cb.place(x=cb_pos[0], y=cb_pos[1])
        self.cb.config(width=cb_w)

        # Confirm button
        btn_txt: str = 'Confirm'
        btn_pos: tuple[int, int] = SIZE * 15, lbl2_pos[1]
        self.btn_confirm: Button = Button(self, text=btn_txt, font=font, relief=GROOVE, command=self.get_width_mode)
        self.btn_confirm.place(x=btn_pos[0], y=btn_pos[1])

    def get_width_mode(self) -> None:
        """Sets width of a line and draw mode to width_mode variable"""
        width: int = int(self.slider.get())
        cb_value: str = self.cb.get()
        mode: int = self.modes.index(cb_value)
        self.width_mode = width, mode
        self.changed = True

