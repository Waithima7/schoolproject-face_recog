

class ViewStudents(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = Label(self, text="Gate Student Authentication System", height="5", font=LARGE_FONT, pady=10,padx=10)
		label.grid(row=0,column=0)

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
		# StudentMenu.add_command(label="Authenticate",bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		StudentMenu.add_command(label="View", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		# StudentMenu.add_command(label="Add New", bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		# StudentMenu.add_separator()
		# StudentMenu.add_command(label="Delete",bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit",activeforeground="red", command=exit)
		menubar.add_cascade(label="Exit",activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()


