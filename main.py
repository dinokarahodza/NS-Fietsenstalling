import tkinter as tk
from Registreren import Registreren
from Stallen import Stallen
from Ophalen import Ophalen
from Home import Home
from informatie import informatie

class MainView(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		home = Home(self)
		functie1 = Registreren(self)
		functie2 = Stallen(self)
		functie3 = Ophalen(self)
		functie4 = informatie(self)

		buttonframe = tk.Frame(self, background="#FFFB00")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		buttonframe.pack(side="top", fill="x", expand=False)

		home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		functie1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		functie2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		functie3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		functie4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


		button1 = tk.Button(buttonframe, text="Registreren", command=functie1.lift, bg="#47A8E5", height=2, width=45, font=("Arial", 22), highlightcolor="white")
		button2 = tk.Button(buttonframe, text="Stallen", command=functie2.lift,bg="#47A8E5", height=2, width=45, font=("Arial", 22), highlightcolor="white")
		button3 = tk.Button(buttonframe, text="Ophalen", command=functie3.lift,bg="#47A8E5", height=2, width=45, font=("Arial", 22), highlightcolor="white")
		button4 = tk.Button(buttonframe, text="Meer informatie", command=functie4.lift,bg="#47A8E5", height=2, width=45, font=("Arial", 22), highlightcolor="white")

		button1.grid(row= 1, column=1)
		button2.grid(row= 1, column=2)
		button3.grid(row= 2, column=1)
		button4.grid(row= 2, column=2)


		home.show()

if __name__ == "__main__":
	root = tk.Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_title("NS-Fietsenstalling - Gemaakt door Dino & Naishel")
	root.overrideredirect(True)
	root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
	while True:
		root.update_idletasks()
		root.update()