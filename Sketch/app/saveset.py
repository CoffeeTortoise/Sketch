from tkinter import Tk, Frame, Label, Button, Entry, GROOVE
import sys
sys.path.append('app')
from config import SIZE, BORDER_W


class SaveSettings(Frame):
    def __init__(self,
                 master: Tk,
                 sizes: tuple[int, int],
                 pos: tuple[int, int],
                 font: tuple[str, int, str]) -> None:
        super().__init__(master, width=sizes[0], height=sizes[1], relief=GROOVE, borderwidth=BORDER_W)
        self.place(x=pos[0], y=pos[1])
        self.filename: str = 'example'
        self.saved: bool = False

        # Label
        lbl_txt: str = 'Filename'
        lbl_pos: tuple[int, int] = 0, 0
        self.lbl: Label = Label(self, text=lbl_txt, font=font, relief=GROOVE)
        self.lbl.place(x=lbl_pos[0], y=lbl_pos[1])

        # Button
        btn_txt: str = 'Save'
        btn_pos: tuple[int, int] = sizes[0] - SIZE * 4, lbl_pos[1]
        self.btn: Button = Button(self, text=btn_txt, font=font, relief=GROOVE, command=self.save)
        self.btn.place(x=btn_pos[0], y=btn_pos[1])

        # Entry
        en_pos: tuple[int, int] = SIZE * 5, lbl_pos[1]
        self.entr: Entry = Entry(self, font=font, relief=GROOVE)
        self.entr.insert(0, self.filename)
        self.entr.place(x=en_pos[0], y=en_pos[1])

    def save(self) -> None:
        text: str = self.entr.get()
        filename = text.replace(' ', '')
        self.filename = filename.replace(',', '.')
        self.saved = True
