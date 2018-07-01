# coding : UTF-16
from tkinter import *
# from tkinter import tkk

vowel_list = [u"අ", u"ආ", u"ඇ", u"ඈ", u"ඉ", u"ඊ", u"උ", u"ඌ", u"ඍ", u"ඎ", u"ඏ", u"ඐ", u"එ", u"ඒ", u"ඓ", u"ඔ", u"ඕ", u"ඖ"]
sripali_list = [u"ං",u"ඃ",u"්",u"ා",u"ැ",u"ෑ",u"ි",u"ී",u"ු",u"ූ",u"ෘ",u"ෙ",u"ේ",u"ෛ",u"ො",u"ෝ",u"ෞ",u"ෟ",u"ෲ",u"ෳ","\u200d"]
big_list = vowel_list + sripali_list

special_character_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":", ";", ".", "-", ",", "/", " ", "\n"] #*** cant inseart u"\" to here ??? :o

unwanted_symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
unwanted_symbols = unwanted_symbols + ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "[", "]", "{", "}", "|", "	", "?", "<", ">"]

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

		self.sinhala = Text(self, width = 50, height = 7, wrap=WORD )
		self.sinhala.grid(row=4, column=1, sticky=E)

		self.convert = Button(self, text="Convert", command=self.transliterate,  width =10, height=1, bg="lightblue")
		self.convert.grid(row=5, column=1, sticky=E)

		self.space_row2 = Label(self, text=" ")
		self.space_row2.grid(row=6, column=0, sticky=NW, columnspan=2)

		self.label2 = Label(self, text="Transliterated string: ")
		self.label2.grid(row=7, column=0, sticky=NW)

		self.singlish = Text(self, width = 50, height = 7, wrap=WORD)
		self.singlish.grid(row=7, column=1, sticky=E)


	def transliterate(self):
		sin_text = self.sinhala.get(0.0, END)

		#remove english and unwanted symbols
		sin_text_temp_list = list(sin_text)
		sin_text_list = [x for x in sin_text_temp_list if x not in unwanted_symbols]
		print("original is: ", sin_text_temp_list)
		print("unwanted symbols removed list is ", sin_text_list)
		sin_text = "".join(sin_text_list)
		print("unwanted symbols removed sin_text is ", sin_text)


		#call convert_to_phoneme function and get the halfly transliterated string
		mapped_text_list = self.convert_to_phoneme(sin_text)
		print("mapped text list: ",mapped_text_list)


		a_inserted_list = self.insert_a(sin_text_list, mapped_text_list)
		print( "a inserted phoneme string:", a_inserted_list);
		print("\n");

		singlish_list = self.phoneme_to_english(a_inserted_list);
		print("singlish list", singlish_list);

		self.singlish.delete(0.0, END)
		self.singlish.insert(0.0, "".join(singlish_list))


	def convert_to_phoneme(self, word):
		word_in_phoneme_list = []
		for letter in word:
			if letter == u"ං":
				word_in_phoneme_list.append(u'ŋ')
			if letter == u"ඃ":
				word_in_phoneme_list.append(u'h')
			if letter == u"අ":
				word_in_phoneme_list.append(u'a')
			if letter == u"ආ":
				word_in_phoneme_list.append(u'a:')
			if letter == u"ඇ":
				word_in_phoneme_list.append(u'æ')
			if letter == u"ඈ":
				word_in_phoneme_list.append(u'æ:')
			if letter == u"ඉ":
				word_in_phoneme_list.append(u'i')
			if letter == u"ඊ":
				word_in_phoneme_list.append(u'i:')
			if letter == u"උ":
				word_in_phoneme_list.append(u'u')
			if letter == u"ඌ":
				word_in_phoneme_list.append(u'u:')
			if letter == u"ඍ":
				word_in_phoneme_list.append(u'ri')
			if letter == u"ඎ":
				word_in_phoneme_list.append(u'ru:')
			if letter == u"ඏ":
				word_in_phoneme_list.append(u'ilu')
			if letter == u"ඐ":
				word_in_phoneme_list.append(u'ilu:')
			if letter == u"එ":
				word_in_phoneme_list.append(u'e')
			if letter == u"ඒ":
				word_in_phoneme_list.append(u'e:')
			if letter == u"ඓ":
				word_in_phoneme_list.append(u'ai')
			if letter == u"ඔ":
				word_in_phoneme_list.append(u'o')
			if letter == u"ඕ":
				word_in_phoneme_list.append(u'o:')
			if letter == u"ඖ":
				word_in_phoneme_list.append(u'ou')
			if letter == u"ක":
				word_in_phoneme_list.append(u'k')
			if letter == u"ඛ":
				word_in_phoneme_list.append(u'k')
			if letter == u"ග":
				word_in_phoneme_list.append(u'ɡ')
			if letter == u"ඝ":
				word_in_phoneme_list.append(u'ɡ')
			if letter == u"ඞ":
				word_in_phoneme_list.append(u'ŋ')
			if letter == u"ඟ":
				word_in_phoneme_list.append(u'ɠ') # *** n දැමිය යුතු සඤ්ඥක අකුරක්
			if letter == u"ච":
				word_in_phoneme_list.append(u'c')
			if letter == u"ඡ":
				word_in_phoneme_list.append(u'c')
			if letter == u"ජ":
				word_in_phoneme_list.append(u'ɟ')
			if letter == u"ඣ":
				word_in_phoneme_list.append(u'ɟh')
			if letter == u"ඤ":
				word_in_phoneme_list.append(u'ɲ')
			if letter == u"ඥ":
				word_in_phoneme_list.append(u'jɲ')
			if letter == u"ඦ":
				word_in_phoneme_list.append(u'ʄ') # *** n දැමිය යුතු සඤ්ඥක අකුරක් - ඉඦු ඉඦු one an only word in sinhala that has ඦ
			if letter == u"ට":
				word_in_phoneme_list.append(u'ʈ')
			if letter == u"ඨ":
				word_in_phoneme_list.append(u'ʈ')
			if letter == u"ඩ":
				word_in_phoneme_list.append(u'ɖ')
			if letter == u"ඪ":
				word_in_phoneme_list.append(u'ɖ')
			if letter == u"න":
				word_in_phoneme_list.append(u'n')
			if letter == u"ණ":
				word_in_phoneme_list.append(u'n')
			if letter == u"ඬ":
				word_in_phoneme_list.append(u'ɖ_') # *** n දැමිය යුතු සඤ්ඥක අකුරක්
			if letter == u"ත":
				word_in_phoneme_list.append(u't')
			if letter == u"ථ":
				word_in_phoneme_list.append(u't')
			if letter == u"ද":
				word_in_phoneme_list.append(u'd')
			if letter == u"ධ":
				word_in_phoneme_list.append(u'd_')
			if letter == u"ඳ":
				word_in_phoneme_list.append(u'ɗ')  # *** n දැමිය යුතු සඤ්ඥක අකුරක් - e.g සඳතැන්න
			if letter == u"ප":
				word_in_phoneme_list.append(u'p')
			if letter == u"ඵ":
				word_in_phoneme_list.append(u'p')
			if letter == u"බ":
				word_in_phoneme_list.append(u'b')
			if letter == u"භ":
				word_in_phoneme_list.append(u'b_')
			if letter == u"ම":
				word_in_phoneme_list.append(u'm')
			if letter == u"ඹ":
				word_in_phoneme_list.append(u'ɓ') # *** m දැමිය යුතු සඤ්ඥක අකුර
			if letter == u"ය":
				word_in_phoneme_list.append(u'j')
			if letter == u"ර":
				word_in_phoneme_list.append(u'r')
			if letter == u"ල":
				word_in_phoneme_list.append(u'l')
			if letter == u"ව":
				word_in_phoneme_list.append(u'w')
			if letter == u"ශ":
				word_in_phoneme_list.append(u'ʃ')
			if letter == u"ෂ":
				word_in_phoneme_list.append(u'ʃ')
			if letter == u"ස":
				word_in_phoneme_list.append(u's')
			if letter == u"හ":
				word_in_phoneme_list.append(u'h')
			if letter == u"ළ":
				word_in_phoneme_list.append(u'l')
			if letter == u"ෆ":
				word_in_phoneme_list.append(u'f')
			if letter == u"්":
				word_in_phoneme_list.append(u'_')  # **** hal symbol
			if letter == "\u200d":
				word_in_phoneme_list.append(u'_')  # **** for rakaransaya
			if letter == u"ා":
				word_in_phoneme_list.append(u'a:')
			if letter == u"ැ":
				word_in_phoneme_list.append(u'æ')
			if letter == u"ෑ":
				word_in_phoneme_list.append(u'æ:')
			if letter == u"ි":
				word_in_phoneme_list.append(u'i')
			if letter == u"ී":
				word_in_phoneme_list.append(u'i:')
			if letter == u"ු":
				word_in_phoneme_list.append(u'u')
			if letter == u"ූ":
				word_in_phoneme_list.append(u'u:')
			if letter == u"ෘ":
				word_in_phoneme_list.append(u'ru')
			if letter == u"ෲ":
				word_in_phoneme_list.append(u'ru:')
			if letter == u"ෙ":
				word_in_phoneme_list.append(u'e')
			if letter == u"ේ":
				word_in_phoneme_list.append(u'e:')
			if letter == u"ෛ":
				word_in_phoneme_list.append(u'ai')
			if letter == u"ො":
				word_in_phoneme_list.append(u'o')
			if letter == u"ෝ":
				word_in_phoneme_list.append(u'o:')
			if letter == u"ෞ":
				word_in_phoneme_list.append(u'ou')
			if letter == u"ෟ":
				word_in_phoneme_list.append(u'ou')



			if letter == u"1":
				word_in_phoneme_list.append(u'1')
			if letter == u"2":
				word_in_phoneme_list.append(u'2')
			if letter == u"3":
				word_in_phoneme_list.append(u'3')
			if letter == u"4":
				word_in_phoneme_list.append(u'4')
			if letter == u"5":
				word_in_phoneme_list.append(u'5')
			if letter == u"6":
				word_in_phoneme_list.append(u'6')
			if letter == u"7":
				word_in_phoneme_list.append(u'7')
			if letter == u"8":
				word_in_phoneme_list.append(u'8')
			if letter == u"9":
				word_in_phoneme_list.append(u'9')
			if letter == u"0":
				word_in_phoneme_list.append(u'0')
			if letter == u".":
				word_in_phoneme_list.append(u'.')
			if letter == u"-":
				word_in_phoneme_list.append(u'-')
			if letter == u"/":
				word_in_phoneme_list.append(u'/')
			if letter == u" ":
				word_in_phoneme_list.append(u' ')
			if letter == u",":
				word_in_phoneme_list.append(u',')
			if letter == u"\n":
				word_in_phoneme_list.append(u'\n')
			if letter == u":":
				word_in_phoneme_list.append(u':')
			if letter == u";":
				word_in_phoneme_list.append(u':')
		# word_in_phoneme = "".join(word_in_phoneme) #converting to string
		return word_in_phoneme_list


	def insert_a(self, sin_text_list, mapped_text_list):
		sin_text_list.append("_") # Append a dummy non effecting symbol at end of sin_text_list to overcome error of length mis match of occuring in rule 2)
		a_inserted_list = []

		for i, letter in enumerate(mapped_text_list):
			a_inserted_list.append(letter)

			# rule 1 : dont insert /a/ after a wovel phoneme representative
			if sin_text_list[i] in big_list:
				continue

			# rule 2 : don't insert /a/ after a phoneme symbol, if the next relevent symbol in sin_text_list is in sripali_list.
			elif sin_text_list[i+1] in sripali_list:
				if sin_text_list[i+1] == u"ං": #to handle special cases like පංචිකාවත්ත where ං is just after a consonent
					a_inserted_list.append('a')
				continue

			# handdle spaces, commas and new line characters
			elif letter in special_character_list:
					continue

			# rule 3 : if the letter is not filtered by above rules, then append /a/
			else:
				a_inserted_list.append('a')

		return a_inserted_list


	def phoneme_to_english(self, word):
		word_in_singlish = []
		for letter in word:

			if letter == u"ɖ_":
				word_in_singlish.append(u'nd') # *** සඤ්ඥක අකුරු, so inseart n prior

			if letter == u"ɠ":
				word_in_singlish.append(u'ng') # *** සඤ්ඥක අකුරු, so inseart n prior

			if letter == u"ɗ":
				word_in_singlish.append(u'nd') # *** සඤ්ඥක අකුරු, so inseart n prior

			if letter == u"ʄ":
				word_in_singlish.append(u'nj') # *** සඤ්ඥක අකුරු, so inseart n prior

			if letter == u"ɓ":
				word_in_singlish.append(u'mb') # *** සඤ්ඥක අකුරු, so inseart n prior


			if letter == u"ŋ":
				word_in_singlish.append(u'n') #some times to "ng"
				continue;
			if letter == u"h":
				word_in_singlish.append(u'h')
				continue
			if letter == u"a":
				word_in_singlish.append(u'a')  #vowel
			if letter == u"a:":
				word_in_singlish.append(u'a') #vowel
			if letter == u"æ":
				word_in_singlish.append(u'e')  #This is special case. although it should be "a", in singlish we use "e"
				                              # For example ඇල්ල -> Ella
			if letter == u"æ:":
				word_in_singlish.append(u'e') # කුරුණෑගල -> kurunEgala
			if letter == u"i":
				word_in_singlish.append(u'i')
			if letter == u"i:":
				word_in_singlish.append(u'ee') #some times "ea"
			if letter == u"u":
				word_in_singlish.append(u'u')

			if letter == u"u:":
				word_in_singlish.append(u'u') # some times "ue"
			if letter == u"ri":
				word_in_singlish.append(u'ri')
			if letter == u"ru:":
				word_in_singlish.append(u'ruu')
			if letter == u"ilu":
				word_in_singlish.append(u'ilu')
			if letter == u"ilu:":
				word_in_singlish.append(u'ilue')
			if letter == u"e":
				word_in_singlish.append(u'e')
			if letter == u"e:":
				word_in_singlish.append(u'e')
			if letter == u"ai":
				word_in_singlish.append(u'ai')
			if letter == u"o":
				word_in_singlish.append(u'o')
			if letter == u"o:":
				word_in_singlish.append(u'o')  #ex: හෝමාගම  -> homagama
			if letter == u"k":
				word_in_singlish.append(u'k')
				continue
			if letter == u"k":
				word_in_singlish.append(u'k')
			if letter == u"ɡ":
				word_in_singlish.append(u'g')
				continue
			if letter == u"ɡ":
				word_in_singlish.append(u'g')
			if letter == u"ŋ":
				word_in_singlish.append(u'n')
			if letter == u"c":
				word_in_singlish.append(u'ch')
				continue
			if letter == u"c":
				word_in_singlish.append(u'ch')
			if letter == u"ɟ":
				word_in_singlish.append(u'j')
			if letter == u"ɟh":
				word_in_singlish.append(u'jh')
			if letter == u"ɲ":
				word_in_singlish.append(u'kn')
			if letter == u"jɲ":
				word_in_singlish.append(u'gn')
			if letter == u"ʈ":
				word_in_singlish.append(u't')
				continue
			if letter == u"ʈ":
				word_in_singlish.append(u't')
			if letter == u"ɖ":
				word_in_singlish.append(u'd')
				continue
			if letter == u"ɖ":
				word_in_singlish.append(u'd')
			if letter == u"n":
				word_in_singlish.append(u'n')
				continue
			if letter == u"n":
				word_in_singlish.append(u'n')
			if letter == u"t":
				word_in_singlish.append(u'th')
				continue
			if letter == u"t":
				word_in_singlish.append(u'th')
			if letter == u"d":
				word_in_singlish.append(u'd')
			if letter == u"d_":
				word_in_singlish.append(u'dh')
			if letter == u"p":
				word_in_singlish.append(u'p')
				continue
			if letter == u"p":
				word_in_singlish.append(u'p')
			if letter == u"b":
				word_in_singlish.append(u'b')
				continue
			if letter == u"b_":
				word_in_singlish.append(u'bh')   # *** mahapprana b -> bh
			if letter == u"m":
				word_in_singlish.append(u'm')
			if letter == u"j":
				word_in_singlish.append(u'y')
			if letter == u"r":
				word_in_singlish.append(u'r')
			if letter == u"l":
				word_in_singlish.append(u'l')
				continue
			if letter == u"w":
				word_in_singlish.append(u'w')
			if letter == u"ʃ":
				word_in_singlish.append(u'sh')
				continue
			if letter == u"ʃ":
				word_in_singlish.append(u'sh')
			if letter == u"s":
				word_in_singlish.append(u's')
			if letter == u"h":
				word_in_singlish.append(u'h')
			if letter == u"l":
				word_in_singlish.append(u'l')
			if letter == u"f":
				word_in_singlish.append(u'f')
			if letter == u"_ ":
				word_in_singlish.append(u'_')

			if letter == u"ou":
				word_in_singlish.append(u'au')
				continue
			if letter == u"ru:":
				word_in_singlish.append(u'ru')

			if letter == u"1":
				word_in_singlish.append(u'1')
			if letter == u"2":
				word_in_singlish.append(u'2')
			if letter == u"3":
				word_in_singlish.append(u'3')
			if letter == u"4":
				word_in_singlish.append(u'4')
			if letter == u"5":
				word_in_singlish.append(u'5')
			if letter == u"6":
				word_in_singlish.append(u'6')
			if letter == u"7":
				word_in_singlish.append(u'7')
			if letter == u"8":
				word_in_singlish.append(u'8')
			if letter == u"9":
				word_in_singlish.append(u'9')
			if letter == u"0":
				word_in_singlish.append(u'0')
			if letter == u".":
				word_in_singlish.append(u'.')
			if letter == u"-":
				word_in_singlish.append(u'-')
			if letter == u"/":
				word_in_singlish.append(u'/')
			if letter == u" ":
				word_in_singlish.append(u' ')
			if letter == u",":
				word_in_singlish.append(u',')
			if letter == u"\n":
				word_in_singlish.append(u'\n')
			if letter == u":":
				word_in_singlish.append(u':')
			if letter == u";":
				word_in_singlish.append(u':')

		# word_in_phoneme = "".join(word_in_phoneme) #converting to string
		return word_in_singlish


root = Tk()
# root.configure(background='gray')
root.title("Welcome to the System")
root.geometry("600x400")
app = SinhalaTransliterator(root)

root.mainloop()
