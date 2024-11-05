from tkinter import Tk, PhotoImage, Button, GROOVE
from PIL import Image, ImageGrab
from app.canv import MyCanvas
from app.colorm import ColorMaker
from app.drawset import DrawSettings
from app.saveset import SaveSettings
from app.config import WND_WIDTH, WND_HEIGHT, SIZE, FNT_SIZE, TITLE
from paths import*


class Sketch(Tk):
    def __init__(self) -> None:
        super().__init__()
        sizes: str = f'{WND_WIDTH}x{WND_HEIGHT}'
        self.geometry(sizes)
        self.resizable(False, False)
        self.title(TITLE)
        icon: PhotoImage = PhotoImage(file=ICON)
        self.iconphoto(True, icon)

        # Canvas
        cv_sizes: tuple[int, int] = SIZE * 30, SIZE * 30
        cv_pos: tuple[int, int] = 0, 0
        self.canvas: MyCanvas = MyCanvas(self, cv_sizes, cv_pos)

        # Color maker
        font: tuple[str, int, str] = FONT, FNT_SIZE, 'bold'
        cm_sizes: tuple[int, int] = WND_WIDTH - cv_sizes[0], SIZE * 10
        cm_pos: tuple[int, int] = cv_sizes[0], 0
        self.color_m: ColorMaker = ColorMaker(self, font, cm_sizes, cm_pos)

        # Draw settings
        ds_sizes: tuple[int, int] = cm_sizes[0], SIZE * 5
        ds_pos: tuple[int, int] = cv_sizes[0], cm_sizes[1]
        self.draw_s: DrawSettings = DrawSettings(self, ds_pos, ds_sizes, font)

        # Save settings
        ss_sizes: tuple[int, int] = cm_sizes[0], SIZE * 2
        ss_pos: tuple[int, int] = cv_sizes[0], ds_pos[1] + ds_sizes[1]
        self.save_s: SaveSettings = SaveSettings(self, ss_sizes, ss_pos, font)
        self.filename: str = self.save_s.filename
        
        # Button quit
        bq_pos: tuple[int, int] = cm_sizes[0] + SIZE * 19, ss_pos[1] + ss_sizes[1]
        bq_text: str = 'Quit'
        self.button_quit: Button = Button(self, text=bq_text, font=font, relief=GROOVE, command=self.destroy)
        self.button_quit.place(x=bq_pos[0], y=bq_pos[1])

        # Global binds
        self.canvas.bind('<Motion>', self.refresh)
        self.bind('<Motion>', self.save_image)

        self.mainloop()

    def refresh(self, event) -> None:
        """Updates canvas state"""
        self.change_color()
        self.change_width_mode()

    def change_color(self) -> None:
        """Changes color of the line"""
        if self.color_m.confirmed:
            self.canvas.color = self.color_m.color
            self.color_m.confirmed = False

    def change_width_mode(self) -> None:
        """Sets canvas line width and canvas draw mode it's new value"""
        if self.draw_s.changed:
            self.canvas.points.clear()
            self.canvas.line_w, self.canvas.mode = self.draw_s.width_mode
            self.draw_s.changed = False

    def save_image(self, event) -> None:
        """Saves an image from the canvas"""
        if self.save_s.saved:
            x: int = self.winfo_rootx() + self.canvas.winfo_x()
            y: int = self.winfo_rooty() + self.canvas.winfo_y()
            x1: int = x + self.winfo_width()
            y1: int = y + self.winfo_height()
            image = ImageGrab.grab().crop((x, y, x1, y1,))
            file: str = f'{self.filename}.png'
            image.save(file, format='png')
            self.save_s.saved = False


if __name__ == '__main__':
    Sketch()

