from pathlib import Path
#from game_window import SolitareGameWindow
# from tkinter import *
import  os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\College\2. Second Year\SEM 3\2. Labs\CS261\Project\Ace-Arena\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Ace-Arena")
window.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + "/resources/icon.ico")

window.geometry("1000x563")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 563,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def button_click():
    print("hello")
    #window = SolitareGameWindow()
    #window.mainloop()

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    281.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=176.0,
    y=308.0,
    width=199.0,
    height=56.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_2.place(
    x=183.0,
    y=415.0,
    width=184.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_click,
    relief="flat"
)
button_3.place(
    x=152.0,
    y=201.0,
    width=247.0,
    height=56.0
)
window.resizable(False, False)
window.mainloop()

