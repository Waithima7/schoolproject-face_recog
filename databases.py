import sqlite3
from sqlite3 import Error
from cryptography.fernet import Fernet


conn = sqlite3.connect('studentauth.db')

c = conn.cursor()


def createUserstable():
	c.execute("create table students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, regno TEXT NOT NULL, faculty TEXT NOT NULL,yrofadm INTEGER NOT NULL, course TEXT NOT NULL, natidno  INTEGER, photo TEXT NOT NULL)")

	conn.commit()

def createsecurity():
	c.execute('create table guards(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, staffid TEXT, idno INTEGER NOT NULL, password TEXT NOT NULL)')
	conn.commit()

def deleteq():
	student=6
	c.execute('DELETE FROM students WHERE id =? ',(student,))
	conn.commit()
	print('The student was deleted')


def makeinnitioalentry():
	#key = Fernet.generate_key()
	ewk = b'TXa2Mi9_AnSptso1m9tWx7UE9bBP8WMvTwloah8672E='
	f = Fernet(ewk)
	token = f.encrypt(b"Moses Waithima")
	utu = f.decrypt(token)
	print(token)
	print(utu)

def insertingwithencryption():
	ewk = b'TXa2Mi9_AnSptso1m9tWx7UE9bBP8WMvTwloah8672E='
	f = Fernet(ewk)
	newpass = f.encrypt(b"@!waithima")
	name = "Moses Waithima"
	idno = 32391868
	c.execute('INSERT INTO guards(name, idno, password) VALUES (?,?,?)',(name, idno, newpass))
	conn.commit()
	print('This is done')

def selectingall():
	# ewk = b'TXa2Mi9_AnSptso1m9tWx7UE9bBP8WMvTwloah8672E='
	# f = Fernet(ewk)
	# newpass = f.encrypt(b"@!waithima")
	# print(newpass)
	# print(f.decrypt(newpass))
	kall = c.execute('SELECT * FROM guards')
	print(c.fetchall())

def fetchingfrominserted():
	ewk = b'TXa2Mi9_AnSptso1m9tWx7UE9bBP8WMvTwloah8672E='
	f = Fernet(ewk)
	entered = "@!waithima"
	newpass = f.encrypt(b"@!waithima")
	name = "Moses Waithima"
	c.execute("SELECT password FROM guards WHERE name=? ",(name,))
	kall = c.fetchone()
	passw = kall[0]
	if f.decrypt(passw) != b"@!waithima":
		print("string comparison failing")
	else:
		print("comparison accepted")

	if str(f.encrypt(b"@!waithima")) == kall:
		print('the two are identically home')
	else:
		print('not identicall at all')
	print(kall)
	print(f.decrypt(passw))

	# if c.fetchone() is not None:
	# 	print('Authentication successful')
	# else:
	# 	print('There was a mistake. Please check with the username or password')


# createUserstable()
# createsecurity()

#selectingall()
def executer():
	c.execute("SELECT * FROM guards")
	print(c.fetchall())

def mainsz():
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    for index, dat in enumerate(students):
        print(dat[1])# = face_recognition.load_image_file("studentphotos/"+dat[7])
        print(dat[6])# = face_recognition.face_encodings(dat[1]+"image")[0]

def insertintostudents():
	c.execute("INSERT INTO students(name, regno, faculty,yrofadm, course, natidno, photo) VALUES('Leah Wanjiku', 'CIT-223-047/2014','CIT',2014, 'Bsc. Computer Science', 32105465,'Leah Wanjiku.jpg')")

	conn.commit()

executer()