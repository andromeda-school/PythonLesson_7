from tkinter import *

block_size = 50
width = block_size * 8
height = block_size * 8
bg_black = "#000000"
bg_white = "#FFFFFF"

window = Tk()
window.title("Первое приложение")
window.geometry(str(width)+"x"+str(height))
window.config(bg=bg_black)

canvas = Canvas(
    window,
    width=width,
    height=height,
    bg=bg_white
)
canvas.pack()

white_turn = True
for i in range(8):
    for j in range(8):
        pos_x = block_size * j
        pos_y = block_size * i
        color = "black"
        if white_turn:
            color = "white"
        canvas.create_rectangle(
            pos_x, pos_y,
            pos_x + block_size, pos_y + block_size,
            fill=color)
        white_turn = not white_turn
    white_turn = not white_turn
            
window.mainloop()