from tkinter import Frame, Button, Label, messagebox, Entry, StringVar, Menu, filedialog
import tkinter as tk
import sqlite3
from cryptography.fernet import Fernet
LARGE_FONT =("Verdana",14)


class MainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self,'Gate Student Authentication System')
		container = tk.Frame(self)
		container.winfo_toplevel().geometry("1100x680")
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}

		for F in(StartPage, RemoveStudent):#Authenticate, ViewStudents, EnrollStudent, RemoveStudent
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
		menubar = Menu(self)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		# StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		# StudentMenu.add_command(label="View",  activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		#StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		# StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students",activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit",activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)


		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		# button1 = Button(self, bd="2", activeforeground="red", bg="black", fg="white", height="3", text="Authenticate",command=lambda: controller.show_frame(Authenticate))
		# button1.pack()
		# button2 = Button(self,bd="2", activeforeground="red", fg="white", height="3", text="View Students",command=lambda: controller.show_frame(ViewStudents))
		# button2.pack()
		# button3 = Button(self,bd="2", activeforeground="red", fg="white", height="3", text="Enroll New",command=lambda: controller.show_frame(EnrollStudent))
		# button3.pack()
		button4 = Button(self, activeforeground="red", height="3", text="Remove Student",command=lambda: controller.show_frame(RemoveStudent))
		button4.pack()


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		#StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		# StudentMenu.add_command(label="View", bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		# StudentMenu.add_command(label="Add New", bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		# StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete",activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students",activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit",activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)


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
		# StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		# StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		# StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		# StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students",  activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit",  activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()



app = MainApp()
app.mainloop()