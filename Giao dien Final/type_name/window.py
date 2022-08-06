from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    624.0, 358.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    647.5, 357.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 291.0, y = 282,
    width = 713.0,
    height = 149)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 503, y = 555,
    width = 290,
    height = 98)

window.resizable(False, False)
window.mainloop()
