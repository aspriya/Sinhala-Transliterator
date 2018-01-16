from Tkinter import *

class SinhalaTransliterator(Frame):

	def __init__(self, master):
		#initializing the frame
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()


	def create_widgets(self):
		self.heading = Label(self, text="Sinhala Text Transliterator", font =("arial", 14, "bold"), fg="black")
		self.heading.grid(row=0, column=1, sticky=W)

		self.space_row1 = Label(self, text=" ")
		self.space_row1.grid(row=1, column=0, sticky=NW, columnspan=2, rowspan=2)

		self.label1 = Label(self, text="Enter a sinhala text string: ")
		self.label1.grid(row=4, column=0, sticky=NW)

		self.sinhala = Text(self, width = 50, height = 7, wrap=WORD)
		self.sinhala.grid(row=4, column=1, sticky=E)

		self.convert = Button(self, text="Convert", command=self.transliterate, width =10, height=1, bg="lightblue")
		self.convert.grid(row=5, column=1, sticky=E)

		self.space_row2 = Label(self, text=" ")
		self.space_row2.grid(row=6, column=0, sticky=NW, columnspan=2)

		self.label2 = Label(self, text="Transliterated string: ")
		self.label2.grid(row=7, column=0, sticky=NW)

		self.singlish = Text(self, width = 50, height = 7, wrap=WORD)
		self.singlish.grid(row=7, column=1, sticky=E)
		
	def transliterate(self):
		sin_text = self.sinhala.get(0.0, END)
		self.singlish.delete(0.0, END)
		self.singlish.insert(0.0, sin_text)


root = Tk()                      
root.title("Welcome to the System")
root.geometry("600x400")
app = SinhalaTransliterator(root)

root.mainloop()