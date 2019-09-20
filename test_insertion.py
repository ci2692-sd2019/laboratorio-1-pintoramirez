# 
# Fecha: 19-09-2019
# Integrantes: Daniel Pinto
#			   Daniela Ramirez
#
# Algoritmo de testeo: ordenamiento Insertion Sort

# Programa:

import tkinter as tk
from tkinter import messagebox
import insertion

#We define function composition in order to use it as an argument to the map function
def funcComp (f,g):
	return lambda x: f(g(x))

#this will add a breakline to each member of the result array
def addEnter(x):
	return x+"\n"	
#finally, this function will parse to string each of the elements of the init file, and then add a \n to each of them.
def aux (x):
	return funcComp(addEnter,str)(x)

class Window:
	# Creates the windows, text, entry and buttons.
	def __init__(self):
		self.master = tk.Tk()
		self.master.geometry("700x150")
		tk.Label(self.master, text="Given an init file with a number in each line, returns an ordered list of the same elements.").place(x=15,y=15)
		tk.Label(self.master, anchor="e", text="Input the name of the file:").place(x=15,y=50)
		self.e1 = tk.Entry(self.master)
		self.e1.place(x=200,y=50)
		self.accept = tk.Button(self.master, text = "Accept",command = self.acceptClick ).place(x = 500, y = 100)
		self.cancel = tk.Button(self.master, text = "Cancel",command = self.cancelClick).place(x = 600, y = 100)
		self.master.mainloop()
	# Reads init file, gets a list out of it, applies insertion, and then outputs the ordered list in a result.txt file and the console.
	def acceptClick(self):
		fileIn = open(self.e1.get(),"r")
		data = fileIn.readlines()
		fileIn.close()
		result = insertion.InsertionSort(list(map (int, data)))
		fileOut = open("result.txt", "w")
		fileOut.writelines(list(map (aux,result) ))
		fileOut.close()
		messagebox.showinfo("SUCCESS", "the ordered list is written in the result.txt file and will be printed on the console.")
		print(result)  
		self.master.quit()
	# Just closes the application.
	def cancelClick(self):
		messagebox.showinfo("BAI", "sad") 
		self.master.quit()

Window()