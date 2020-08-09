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
		 self.studid.get(), self.idnumber.get(),self.course.get(), self.faculty.get(), self.yrofadm.get(),self.item)).grid(row=7,column=0)
		button5 = Button(self,text="Exit",fg='red',command=self.exit).grid(row=9,column=0)



	def browse(self):
		self.item = filedialog.askopenfilename(initialdir = "/",title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
		if self.item != None:
			return self.item


	def savedata(self,fullname, studid,idnumber,course,faculty, yrofadm, photo):
		conn = sqlite3.connect('studentauth.db')
		c = conn.cursor()
		try:
			c.execute(
				"INSERT INTO `students` (name, regno, faculty, yrofadm, course, natidno, photo) VALUES(?, ?, ?, ?, ?,?, ?)",
				(fullname,studid,idnumber,course,faculty, yrofadm, photo))
			conn.commit()
			messagebox.showinfo("Success!",'You have successfully registered a new student into the system')

		except:
			messagebox.showerrormessage('error')

	def menubar(self,parent):
		menubar = Menu(parent)
		StudentMenu = Menu(menubar)
		exitmenu = Menu(menubar)
		#StudentMenu.add_command(label="Authenticate", activeforeground="red", command=lambda: controller.show_frame(Authenticate))
		#StudentMenu.add_command(label="View", bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(ViewStudents))
		StudentMenu.add_command(label="Add New", activeforeground="red", command=lambda: controller.show_frame(EnrollStudent))
		StudentMenu.add_separator()
		#StudentMenu.add_command(label="Delete",bd="1", fg="white", activeforeground="red", command=lambda: controller.show_frame(RemoveStudent))
		menubar.add_cascade(label="Students", activeforeground="red", menu=StudentMenu)

		exitmenu.add_command(label="Exit", activeforeground="red", command=self.exit)
		menubar.add_cascade(label="Exit", activeforeground="red", menu=exitmenu)

		return menubar

	def exit(self):
		result = messagebox.askquestion("Exit", "Are You Sure You want to Exit?", icon='warning')
		if result == 'yes':
			self.destroy()
