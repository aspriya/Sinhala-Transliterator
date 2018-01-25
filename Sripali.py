# coding: utf-8

from tkinter import *

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
		sin_text = self.convert_to_phoneme(sin_text)	
		self.singlish.delete(0.0, END)
		self.singlish.insert(0.0, sin_text)


	def convert_to_phoneme(self, word):	
		word_in_phoneme = []
		for letter in word:
			if letter == u"ං":
				word_in_phoneme.append(u'ŋ')
			if letter == u"ඃ":
				word_in_phoneme.append(u'h')
			if letter == u"අ":
				word_in_phoneme.append(u'a')
			if letter == u"ආ":
				word_in_phoneme.append(u'a:')
			if letter == u"ඇ":
				word_in_phoneme.append(u'æ')
			if letter == u"ඈ":
				word_in_phoneme.append(u'æ:')
			if letter == u"ඉ":
				word_in_phoneme.append(u'i')
			if letter == u"ඊ":
				word_in_phoneme.append(u'i:')
			if letter == u"උ":
				word_in_phoneme.append(u'u')
			if letter == u"ඌ":
				word_in_phoneme.append(u'u:')
			if letter == u"ඍ":
				word_in_phoneme.append(u'ri')
			if letter == u"ඎ":
				word_in_phoneme.append(u'ru:')
			if letter == u"ඏ":
				word_in_phoneme.append(u'ilu')
			if letter == u"ඐ":
				word_in_phoneme.append(u'ilu:')
			if letter == u"එ":
				word_in_phoneme.append(u'e')
			if letter == u"ඒ":
				word_in_phoneme.append(u'e:')
			if letter == u"ඓ":
				word_in_phoneme.append(u'ai')
			if letter == u"ඔ":
				word_in_phoneme.append(u'o')
			if letter == u"ඕ":
				word_in_phoneme.append(u'o:')
			if letter == u"ඖ":
				word_in_phoneme.append(u'ou')
			if letter == u"ක":
				word_in_phoneme.append(u'k')
			if letter == u"ඛ":
				word_in_phoneme.append(u'k')
			if letter == u"ග":
				word_in_phoneme.append(u'ɡ')
			if letter == u"ඝ":
				word_in_phoneme.append(u'ɡ')
			if letter == u"ඞ":
				word_in_phoneme.append(u'ŋ')
			if letter == u"ඟ":
				word_in_phoneme.append(u'r')
			if letter == u"ච":
				word_in_phoneme.append(u'c')
			if letter == u"ඡ":
				word_in_phoneme.append(u'c')
			if letter == u"ජ":
				word_in_phoneme.append(u'ɟ')
			if letter == u"ඣ":
				word_in_phoneme.append(u'ɟ')
			if letter == u"ඤ":
				word_in_phoneme.append(u'ɲ')
			if letter == u"ඥ":
				word_in_phoneme.append(u'jɲ')
			if letter == u"ඦ":
				word_in_phoneme.append(u'ʄ')
			if letter == u"ට":
				word_in_phoneme.append(u'ʈ')
			if letter == u"ඨ":
				word_in_phoneme.append(u'ʈ')
			if letter == u"ඩ":
				word_in_phoneme.append(u'ɖ')
			if letter == u"ඪ":
				word_in_phoneme.append(u'ɖ')
			if letter == u"න":
				word_in_phoneme.append(u'n')
			if letter == u"ණ":
				word_in_phoneme.append(u'n')
			if letter == u"ඬ":
				word_in_phoneme.append(u'ɖ')
			if letter == u"ත":
				word_in_phoneme.append(u't')
			if letter == u"ථ":
				word_in_phoneme.append(u't')
			if letter == u"ද":
				word_in_phoneme.append(u'd')
			if letter == u"ධ":
				word_in_phoneme.append(u'd')
			if letter == u"ඳ":
				word_in_phoneme.append(u'ɗ')
			if letter == u"ප":
				word_in_phoneme.append(u'p')
			if letter == u"ඵ":
				word_in_phoneme.append(u'p')
			if letter == u"බ":
				word_in_phoneme.append(u'b')
			if letter == u"භ":
				word_in_phoneme.append(u'b')
			if letter == u"ම":
				word_in_phoneme.append(u'm')
			if letter == u"ඹ":
				word_in_phoneme.append(u'ɓ')
			if letter == u"ය":
				word_in_phoneme.append(u'j')
			if letter == u"ර":
				word_in_phoneme.append(u'r')
			if letter == u"ල":
				word_in_phoneme.append(u'l')
			if letter == u"ව":
				word_in_phoneme.append(u'w')
			if letter == u"ශ":
				word_in_phoneme.append(u'ʃ')
			if letter == u"ෂ":
				word_in_phoneme.append(u'ʃ')
			if letter == u"ස":
				word_in_phoneme.append(u's')
			if letter == u"හ":
				word_in_phoneme.append(u'h')
			if letter == u"ළ":
				word_in_phoneme.append(u'l')
			if letter == u"ෆ":
				word_in_phoneme.append(u'f')
			if letter == u"්":
				word_in_phoneme.append(u'_')
			if letter == u"ා":
				word_in_phoneme.append(u'a:')
			if letter == u"ැ":
				word_in_phoneme.append(u'æ')
			if letter == u"ෑ":
				word_in_phoneme.append(u'æ:')
			if letter == u"ි":
				word_in_phoneme.append(u'i')
			if letter == u"ී":
				word_in_phoneme.append(u'i:')
			if letter == u"ු":
				word_in_phoneme.append(u'u')
			if letter == u"ූ":
				word_in_phoneme.append(u'u:')
			if letter == u"ෘ":
				word_in_phoneme.append(u'ru')
			if letter == u"ෙ":
				word_in_phoneme.append(u'e')
			if letter == u"ේ":
				word_in_phoneme.append(u'e:')
			if letter == u"ෛ":
				word_in_phoneme.append(u'ai')
			if letter == u"ො":
				word_in_phoneme.append(u'o')
			if letter == u"ෝ":
				word_in_phoneme.append(u'o:')
			if letter == u"ෞ":
				word_in_phoneme.append(u'ou')
			if letter == u"ෟ":
				word_in_phoneme.append(u'ou')
			if letter == u"ෲ":
				word_in_phoneme.append(u'ru:')
			if letter == u"ෳ":
				word_in_phoneme.append(u'ou')
		
		word_in_phoneme = "".join(word_in_phoneme)
		return word_in_phoneme
		


root = Tk()                      
root.title("Welcome to the System")
root.geometry("600x400")
app = SinhalaTransliterator(root)

root.mainloop()