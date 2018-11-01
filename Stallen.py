from Page import Page
import tkinter as tk
from DB import DB
from Telegram import Telegram
from tkinter import messagebox

class Stallen(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)

		label = tk.Label(self, text="Stallen", font=('Arial',39),bg="#FFFB00")
		label.pack(side="top", fill="both", expand=True)

		label = tk.Label(self,text='Fietsnummer',height=3, font=('Arial',15),bg="#FFFB00")
		label.pack(pady=8,side="top", fill="both")
		self.entrycode = tk.Entry(self)
		self.entrycode.pack()

		label = tk.Label(self,text='Gebruikersnaam',height=3,font=('Arial',15),bg="#FFFB00")
		label.pack(pady=8,side="top", fill="both")
		self.entrynaam = tk.Entry(self)
		self.entrynaam.pack()

		label = tk.Label(self,text='Wachtwoord', height=3,font=('Arial',15),bg="#FFFB00")
		label.pack(pady=8,side="top", fill="both")
		self.entrywachtwoord = tk.Entry(self,show='*')
		self.entrywachtwoord.pack()

		self.button = tk.Button(self, text="Confirm", command=self.buttonconfirm, font=('Arial',15))
		self.button.pack(padx=10,pady=10)
		Page.configure(self,background='#FFFB00')

	def buttonconfirm(self):
		naam = self.entrynaam.get()
		code = self.entrycode.get()
		wachtwoord = self.entrywachtwoord.get()
		db = DB()
		user = db.getUserInfo(naam)
		tg = Telegram()
		self.entrywachtwoord.delete(0, 'end')
		self.entrycode.delete(0, 'end')
		self.entrynaam.delete(0, 'end')

		if db.verifyUser(naam,wachtwoord):
			if user:
				if db.stalFiets(code,naam):
					messagebox.showinfo("Gelukt!", "De fiets is gestald")
					tg.sendMessage("Uw fiets is gestald!",user[2])
				else:
					messagebox.showinfo('Er is een fout opgetreden!','De fiets is niet bekend bij deze gebruiker,de fiets is niet bekend of de fiets staat al gestald!')
			else:
				messagebox.showinfo('Onbekende gebruiker!','Uw Gebruikersnaam is niet bij ons bekend, als u nieuw bent, kunt u zich registreren op de pagina \'Registreren\'')
		else:
			messagebox.showinfo('Er is een fout opgetreden','Uw Gebruikersnaam/Wachtwoord combinatie klopt niet!')
