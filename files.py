import tkinter
from tkinter import filedialog

#root = tkinter.Tk()

# file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
# if file != None:
#     data = file.read()
#     file.close()
#     print("I got %d bytes from this file", data)
def openfile():
	filename = filedialog.asksaveasfilename(initialdir = "/",finaldir="/pythoncode/project/", title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
	print(filename)

#root = tkinter.Tk()
#root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
openfile()
#print (root.filename)


