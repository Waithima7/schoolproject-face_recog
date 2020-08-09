import os
from tkinter import Frame, Button, Label, messagebox, Entry, StringVar, Menu, filedialog
import tkinter as tk
import sqlite3
from recognizer import *
from cryptography.fernet import Fernet
LARGE_FONT =("Verdana",14)

from admins import *

class MainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self,'Gate Student Authentication System')
		container = tk.Frame(self)
		container.winfo_toplevel().geometry("1100x680")
		container.grid(sticky="n")
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}

		for F in(StartPage, Authenticate, ViewStudents, EnrollStudent, RemoveStudent):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

		menubar = frame.menubar(self)
		self.configure(menu=menubar)



class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)

		# self.frame1 = Frame(self,bg="white")
		# self.frame1.pack()
		label = tk.Label(self, text="Gate Student Authentication System", height="5", anchor="center", font=LARGE_FONT)
		label.grid(row=0, column=1)

		button1 = Button(self, bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="Authenticate",command=lambda: controller.show_frame(Authenticate))
		button1.grid(row=1, column=1)
		button2 = Button(self,bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="View Students",command=lambda: controller.show_frame(ViewStudents))
		button2.grid(row=1, column=2)
		button3 = Button(self,bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="Enroll New",command=lambda: controller.show_frame(EnrollStudent))
		button3.grid(row=1, column=3)
		button4 = Button(self,bd="2", activeforeground="red",anchor="w", bg="black", fg="white", height="3", text="Remove Student",command=lambda: controller.show_frame(RemoveStudent))
		button4.grid(row=1, column=4)


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar



class Authenticate(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = Button(self, activeforeground="red",  height="3", text="Authenticate",command=self.authenticate)
		button1.pack()

	def authenticate(self):
		recognize()
		# messagebox.showinfo('Authenticate', 'This is for authentication of the students')


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar


class ViewStudents(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)

		Label(self, text="#").grid(row=1, column=0)
		Label(self, text="FullNames").grid(row=1, column=1)
		Label(self, text="Registration Number").grid(row=1, column=2)
		Label(self, text="Id Number").grid(row=1, column=3)
		Label(self, text="Course").grid(row=1, column=4)
		Label(self, text="Faculty").grid(row=1, column=5)
		Label(self, text="Year Of Admission").grid(row=1, column=6)
		Label(self, text="Photo").grid(row=1, column=7)

		self.showallrecords()

	def showallrecords(self):
		Data = self.readfromdatabase()
		for index, dat in enumerate(Data):
			Label(self, text=dat[0]).grid(row=index+2, column=0)
			Label(self, text=dat[1]).grid(row=index+2, column=1)
			Label(self, text=dat[2]).grid(row=index+2, column=2)
			Label(self, text=dat[6]).grid(row=index+2, column=3)
			Label(self, text=dat[5]).grid(row=index+2, column=4)
			Label(self, text=dat[3]).grid(row=index+2, column=5)
			Label(self, text=dat[4]).grid(row=index+2, column=6)
			Label(self, text=dat[7]).grid(row=index+2, column=7)


	def readfromdatabase(self):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("SELECT * FROM students")
		return c.fetchall()

	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


class EnrollStudent(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)
		Label(self,text='Full Names',fg='black').grid(row=1,column=1)
		Label(self, text='Registration No', fg='black').grid(row=2,column=1)
		Label(self, text='ID Number', fg='black').grid(row=3,column=1)
		Label(self, text='Course', fg='black').grid(row=4,column=1)
		Label(self, text='Faculty', fg='black').grid(row=5,column=1)
		Label(self, text='Year of Admission', fg='black').grid(row=6,column=1)
		Label(self, text='Photo', fg='black').grid(row=7,column=1)

		self.fullname=StringVar()
		fullname_entry=Entry(self,textvariable=self.fullname).grid(row=1,column=2)
		self.studid=StringVar()
		studid_entry=Entry(self, textvariable=self.studid).grid(row=2,column=2)
		self.idnumber=StringVar()
		idnumber_entry=Entry(self, textvariable=self.idnumber).grid(row=3,column=2)
		self.course=StringVar()
		course_entry=Entry(self, textvariable=self.course).grid(row=4,column=2)
		self.faculty=StringVar()
		faculty_entry=Entry(self, textvariable=self.faculty).grid(row=5,column=2)
		self.yrofadm=StringVar()
		yrofadm_entry=Entry(self, textvariable=self.yrofadm).grid(row=6,column=2)

		photo = Button(self, text="Select File", command=self.browse).grid(row=7,column=2)

		button4 = Button(self,text="Save",fg='red',command=lambda: self.savedata(self.fullname.get(),
		 self.studid.get(), self.idnumber.get(),self.course.get(), self.faculty.get(), self.yrofadm.get(), self.item)).grid(row=7,column=0)
		button5 = Button(self,text="Exit",fg='red',command=self.exit).grid(row=9,column=0)

	def browse(self):
		self.item = filedialog.askopenfilename(initialdir = "/",title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
		if self.item != None:
			return self.item


	def savedata(self,fullname,studid,idnumber,course,faculty, yrofadm, photo):
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		image_dir = os.path.join(BASE_DIR,"studentphotos")
		filename, file_extension = os.path.splitext(photo)
		#fileName = os.path.basename(photo)
		newname = fullname + file_extension
		image_dir = os.path.join(BASE_DIR,"studentphotos")
		os.rename(photo,image_dir + '/' + newname)

		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		try:
			c.execute(
	                "INSERT INTO `students` (name, regno, faculty, yrofadm, course, natidno, photo) VALUES(?, ?, ?, ?, ?,?, ?)",
	                (fullname,studid,idnumber,course,faculty, yrofadm, newname))
			conn.commit()
			messagebox.showinfo("Success!",'You have successfully created a new student Record!')
		except:
			messagebox.showerrormessage('error')

	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


class RemoveStudent(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)

		numLabel = Label(self, text="#", width=10).grid(row=1, column=0)
		fullnameLabel = Label(self, text="FullNames", width=10).grid(row=1, column=1)
		stfIdLabel = Label(self, text="Registration Number", width=10).grid(row=1, column=2)
		IdNumberLabel = Label(self, text="Id Number", width=10).grid(row=1, column=3)
		courseLabel = Label(self, text="Course", width=10).grid(row=1, column=4)
		faculyLabel = Label(self, text="Faculty", width=10).grid(row=1, column=5)
		year_of_admissionLabel = Label(self, text="Adm Yr", width=10).grid(row=1, column=6)
		year_of_admissionLabel = Label(self, text="Photo", width=10).grid(row=1, column=7)
		Action = Label(self, text="Action",fg="red",activeforeground="red", width=6).grid(row=1, column=8)
		self.showallrecords()

	def showallrecords(self):
		Data = self.readfromdatabase()
		for index, dat in enumerate(Data):
			Label(self, text=dat[0]).grid(row=index+2, column=0)
			Label(self, text=dat[1]).grid(row=index+2, column=1)
			Label(self, text=dat[2]).grid(row=index+2, column=2)
			Label(self, text=dat[6]).grid(row=index+2, column=3)
			Label(self, text=dat[5]).grid(row=index+2, column=4)
			Label(self, text=dat[3]).grid(row=index+2, column=5)
			Label(self, text=dat[4]).grid(row=index+2, column=6)
			Label(self, text=dat[7]).grid(row=index+2, column=7)
			Button(self, text="Delete", fg="red", activeforeground="red", command=lambda:self.deletestudent(dat[0])).grid(row=index+2, column=8)


	def readfromdatabase(self):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("SELECT * FROM students")
		return c.fetchall()

	def deletestudent(self,student):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("DELETE FROM students WHERE id =?",(student,))
		conn.commit()
		messagebox.showinfo('You have deleted the student record from the database')


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()

#the system has been redesigned to accomodate for both the administrator and the security guard
#adding the modules for the admin




# Coming up with the login area




def login(event=None):
	if USERNAME.get() == "" or PASSWORD.get() == "":
		lbl_text.config(text="Please complete the required field!", fg="red")
	else:
		ewk = b'TXa2Mi9_AnSptso1m9tWx7UE9bBP8WMvTwloah8672E='
		f = Fernet(ewk)
		# entered = f.encrypt(PASSWORD.get())
		#cursor.execute("SELECT password FROM `guards` WHERE `username` = ?", (USERNAME.get()))
		#kall = cursor.fetchone()
		#passw = kall[0]
		# if cursor.fetchone() is not None:

		# 	root.destroy()
		# 	messagebox('Success','You have successfully logged in as a Security officer')

		if USERNAME.get() == "Moses Waithima" and PASSWORD.get() == "@!waithima":
			root.destroy()
			app = MainAdmin()
			app.mainloop()

		else:
			conn = sqlite3.connect('studentauth.db')
			c = conn.cursor()
			c.execute("SELECT * FROM `guards` WHERE `name` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
			if c.fetchone() is not None:
				root.destroy()
				conn.close()
				app = MainApp()
				app.mainloop()

			else:
				lbl_text.config(text="Invalid username or password", fg="red")
				USERNAME.set("")
				PASSWORD.set("")



root = tk.Tk()
root.title("Student Authentication System")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

USERNAME = StringVar()
PASSWORD = StringVar()

Top = Frame(root, bd=2)
Top.pack(side="top")
Form = Frame(root, height=200)
Form.pack(side="top", pady=20)

lbl_title = Label(Top, text = "Security Login", font=('arial', 15))
lbl_title.pack()
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

btn_login = Button(Form, text="Login", width=45, command=login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', login)


if __name__ == '__main__':
    root.mainloop()


#Main Classes

