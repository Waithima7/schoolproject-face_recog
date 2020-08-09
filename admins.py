from tkinter import Frame, Button, Label, messagebox, Entry, StringVar, Menu, filedialog
import tkinter as tk
import sqlite3
# from recognizer import *
# from cryptography.fernet import Fernet
LARGE_FONT =("Verdana",14)
TEXT_FONT =("Verdana",12)

class MainAdmin(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self,'Gate Student Authentication System')
		container = tk.Frame(self)
		container.winfo_toplevel().geometry("1100x680")
		container.grid(sticky="n")
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}

		for F in(AdminStartPage, ADminViewStudents, EnrollGuard, RemoveGuard, ViewGuards):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(AdminStartPage)


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

		menubar = frame.menubar(self)
		self.configure(menu=menubar)


class AdminStartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)

		# self.frame1 = Frame(self,bg="white").pack()
		label = tk.Label(self, text="Gate Student Authentication System", height="5", anchor="center", font=LARGE_FONT)
		label.grid()

		# self.frame2 = Frame(self, bg="white").pack()

		button1 = Button(self, bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="Student Records",command=lambda: controller.show_frame(ADminViewStudents))
		button1.grid(row=1, column=1)
		button2 = Button(self,bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="View Guards",command=lambda: controller.show_frame(ViewGuards))
		button2.grid(row=1, column=2)
		button3 = Button(self,bd="2", activeforeground="red", anchor="w", bg="black", fg="white", height="3", text="New Guard",command=lambda: controller.show_frame(EnrollGuard))
		button3.grid(row=1, column=3)
		button4 = Button(self,bd="2", activeforeground="red",anchor="w", bg="black", fg="white", height="3", text="Remove Guard",command=lambda: controller.show_frame(RemoveGuard))
		button4.grid(row=1, column=4)


	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="View Students", activeforeground="red", command=lambda: controller.show_frame(ADminViewStudents))
		StudentMenu.add_command(label="View Guards", activeforeground="red", command=lambda: controller.show_frame(ViewGuards))
		StudentMenu.add_command(label="Add New Guard", activeforeground="red", command=lambda: controller.show_frame(EnrollGuard))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete Guard", activeforeground="red", command=lambda: controller.show_frame(RemoveGuard))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar



class ADminViewStudents(tk.Frame):
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
		StudentMenu.add_command(label="View Students", activeforeground="red", command=lambda: controller.show_frame(ADminViewStudents))
		StudentMenu.add_command(label="View Guards", activeforeground="red", command=lambda: controller.show_frame(ViewGuards))
		StudentMenu.add_command(label="Add New Guard", activeforeground="red", command=lambda: controller.show_frame(EnrollGuard))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete Guard", activeforeground="red", command=lambda: controller.show_frame(RemoveGuard))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


class ViewGuards(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)

		Label(self,height="3", font=TEXT_FONT, text="#", padx=10).grid(row=1, column=0)
		Label(self,height="3", font=TEXT_FONT, text="FullNames", padx=10).grid(row=1, column=1)
		Label(self,height="3", font=TEXT_FONT, text="Staff Number", padx=10).grid(row=1, column=2)
		Label(self,height="3", font=TEXT_FONT, text="Id Number", padx=10).grid(row=1, column=3)

		self.showallrecords()

	def showallrecords(self):
		Data = self.readfromdatabase()
		for index, dat in enumerate(Data):
			Label(self, text=dat[0]).grid(row=index+2, column=0)
			Label(self, text=dat[1]).grid(row=index+2, column=1)
			Label(self, text=dat[2]).grid(row=index+2, column=2)
			Label(self, text=dat[3]).grid(row=index+2, column=3)


	def readfromdatabase(self):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("SELECT * FROM guards")
		return c.fetchall()

	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="View Students", activeforeground="red", command=lambda: controller.show_frame(ADminViewStudents))
		StudentMenu.add_command(label="View Guards", activeforeground="red", command=lambda: controller.show_frame(ViewGuards))
		StudentMenu.add_command(label="Add New Guard", activeforeground="red", command=lambda: controller.show_frame(EnrollGuard))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete Guard", activeforeground="red", command=lambda: controller.show_frame(RemoveGuard))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()



class EnrollGuard(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)
		Label(self,text='Full Names',fg='black').grid(row=1,column=1)
		Label(self, text='Staff No', fg='black').grid(row=2,column=1)
		Label(self, text='ID Number', fg='black').grid(row=3,column=1)
		Label(self, text='Password', fg='black').grid(row=4,column=1)

		self.fullname=StringVar()
		fullname_entry=Entry(self,textvariable=self.fullname).grid(row=1,column=2)
		self.staffid=StringVar()
		staff_entry=Entry(self, textvariable=self.staffid).grid(row=2,column=2)
		self.idnumber=StringVar()
		idnumber_entry=Entry(self, textvariable=self.idnumber).grid(row=3,column=2)
		self.password=StringVar()
		password_entry=Entry(self, show="*", textvariable=self.password).grid(row=4,column=2)

		button4 = Button(self,text="Save",fg='red',command=lambda: self.saveguarddata(self.fullname.get(),
		 self.staffid.get(), self.idnumber.get(),self.password.get())).grid(row=6,column=2)
		button5 = Button(self,text="Exit",fg='red',command=self.exit).grid(row=7,column=2)

				# app = MainApp()
				# app.mainloop()
	def saveguarddata(self,fullname,staffid,idnumber,password):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		try:
			c.execute(
	                "INSERT INTO `guards` (name, staffid, idno, password) VALUES(?, ?, ?, ?)",
	                (fullname,staffid,idnumber,password))
			conn.commit()
			messagebox.showinfo("Success!",'The Guard was succesfully added!')
		except:
			messagebox.showerrormessage('error')

	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="View Students", activeforeground="red", command=lambda: controller.show_frame(ADminViewStudents))
		StudentMenu.add_command(label="View Guards", activeforeground="red", command=lambda: controller.show_frame(ViewGuards))
		StudentMenu.add_command(label="Add New Guard", activeforeground="red", command=lambda: controller.show_frame(EnrollGuard))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete Guard", activeforeground="red", command=lambda: controller.show_frame(RemoveGuard))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()

class RemoveGuard(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT)
		label.grid(pady=10,padx=10)

		Label(self, text="#").grid(row=1, column=0)
		Label(self, text="FullNames").grid(row=1, column=1)
		Label(self, text="Staff Number").grid(row=1, column=2)
		Label(self, text="Id Number").grid(row=1, column=3)
		self.showguardsrecords()

	def showguardsrecords(self):
		Data = self.readfromguardstable()
		for index, dat in enumerate(Data):
			Label(self, text=dat[0]).grid(row=index+2, column=0)
			Label(self, text=dat[1]).grid(row=index+2, column=1)
			Label(self, text=dat[2]).grid(row=index+2, column=2)
			Label(self, text=dat[3]).grid(row=index+2, column=3)
			Button(self, text="Delete", fg="red", activeforeground="red", command=lambda:self.deleteguard(dat[0])).grid(row=index+2, column=8)


	def readfromguardstable(self):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("SELECT * FROM guards")
		return c.fetchall()

	def deleteguard(self,guard):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		c.execute("DELETE FROM guards WHERE id =?",(guard,))
		conn.commit()
		messagebox.showinfo("Deleted!",'Security Guard derelted from the records!')


	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		StudentMenu.add_command(label="View Students", activeforeground="red", command=lambda: controller.show_frame(ADminViewStudents))
		StudentMenu.add_command(label="View Guards", activeforeground="red", command=lambda: controller.show_frame(ViewGuards))
		StudentMenu.add_command(label="Add New Guard", activeforeground="red", command=lambda: controller.show_frame(EnrollGuard))
		StudentMenu.add_separator()
		StudentMenu.add_command(label="Delete Guard", activeforeground="red", command=lambda: controller.show_frame(RemoveGuard))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()

# app = MainAdmin()
# app.mainloop()