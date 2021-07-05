from tkinter import *
from tkinter import messagebox
import serial
import serial.tools.list_ports as port_list
import time
import psutil

def write_to_file(var):
	with open('input_channel/temp_file.txt', 'a',newline='') as f:
			writer = f.write('i' + var + 'f')
			#writer.writerow(var)	


def user_input():
	global click
	click = 0
	list = []
	def myclick(event = None):
		global click
		global search_channel 
		search_channel = e.get()
		if search_channel.isdigit():
			if int(search_channel) > 0 and int(search_channel) <= 3840:
				if click < 1:
					list.append(search_channel)
					T.insert(END,"Canalul cautat este: " + str(search_channel))
					list.append(search_channel)
					e.delete(0,END)
					click += 1
					#send_data(search_channel)
					print(search_channel)
					write_to_file(search_channel)
				else:
					if list[-1] != search_channel:
						T.delete('1.0', END)
						T.insert(END,"Canalul cautat este: " + str(search_channel))
						list.append(search_channel)
						e.delete(0,END)
						#send_data(search_channel)
						print(search_channel)
						write_to_file(search_channel)
					else:
						e.delete(0,END)
			else:
				messagebox.showinfo("ERROR", "Te rog introdu un numar pozitiv si mai mic decat 3841")
				e.delete(0,END)
		else:
			messagebox.showinfo("ERROR", "Te rog introdu un numar pozitiv si mai mic decat 3841")
			e.delete(0,END)	
	global root
	root = Tk()
	root.title("Channel Search")
	root.bind("<Return>",myclick)

	T = Text(root, height = 5, width = 42)
	# Create label
	l = Label(root, text = "Introdu canalul pe care il cauti")
	l.config(font =("Courier", 14))

	#Fact = "Canalul cautat este: "

	l.grid(row = 0,column = 0)
	T.grid(row = 5, column = 0)

	e = Entry(root, width = 50,borderwidth = 5)
	e.grid(row = 1,column = 0,padx = 10,pady = 10)
	#e.insert(0, "Enter your name")
	
	myButton = Button(root, text = "Save Channel",command = myclick)
	myButton.grid(row = 3, column = 0)

	#T.insert(END, search_channel)

	root.mainloop()


user_input()