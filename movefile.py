import os
from tkinter import filedialog
#from filedialog import askopenfilename


def browsecsv():
	# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	# filename = filedialog.askopenfilename(initialdir = "/", title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
	# print(filename)
	# print(os.path.dirname(filename))
	# print(BASE_DIR)
	# os.rename(filename,BASE_DIR)

	item = filedialog.askopenfilename(initialdir = "/",title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	filename, file_extension = os.path.splitext(item)
	fileName = os.path.basename(item)
	newname = "Newname" + file_extension
	print(newname)
	image_dir = os.path.join(BASE_DIR,"studentphotos")
	os.rename(item,image_dir + '/' + newname)


browsecsv()