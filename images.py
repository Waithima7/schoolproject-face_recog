from PIL import Image, ImageTk
from tkinter import Label, Tk

def showImg():
	window = Tk()
	newload = Image.open('obama.jpg')
	print(newload.size)
	load = newload.resize((300,300))
	render = ImageTk.PhotoImage(load)

	label = Label(window, image=render)
	label.image = render
	label.place(x=0, y=0)

	window.mainloop()


showImg()

