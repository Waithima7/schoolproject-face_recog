from tkinter import *

class Window:
    def __init__(self, master):
        #Browse Bar
        csvfile=Label(root, text="File").grid(row=1, column=0)
        bar=Entry(master).grid(row=1, column=1) 
        #Buttons 
        y=7
        self.cbutton= Button(root, text="OK", command=master.destroy)       #closes window
        y+=1
        self.cbutton.grid(row=10, column=3, sticky = W + E)
        self.bbutton= Button(root, text="Browse", command=self.browsecsv)
        self.bbutton.grid(row=1, column=3)

#-------------------------------------------------------------------------------------#
    def browsecsv(self):
        from filedialog import askopenfilename
        Tk().withdraw() 
        filename = askopenfilename()

#-------------------------------------------------------------------------------------#
        import csv

        with open('filename', 'rb') as csvfile:
            logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            rownum=0
            for row in logreader:
                NumColumns = len(row)
                rownum += 1

            Matrix = [[0 for x in xrange(NumColumns)] for x in xrange(rownum)]
            csvfile.close()


root = Tk()
window=Window(root)
root.mainloop()