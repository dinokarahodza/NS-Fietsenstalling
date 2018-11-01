from Page import Page
import tkinter as tk
from Telegram import Telegram
import random
from DB import DB
from tkinter import messagebox

class Ophalen(Page):
	widgets = {}
	fietsnummer = 0
	gebruikersnaam = 0
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		widgets = self.widgets
		widgets['1'] = tk.Label(self, text="Ophalen", font=('Arial',39),bg="#FFFB00")
		widgets['1'].pack(side="top", fill="both",expand=True)

		self.widgets['fietsNummer'] = tk.Entry(self)
		widgets['2'] = tk.Label(self,text='Fietsnummer',height=2, bg='#FFFB00', font=('Arial',15))
		widgets['2'].pack(pady=10)
		self.widgets['fietsNummer'].pack(padx=10, pady=10)

		self.widgets['gebruikersnaam'] = tk.Entry(self)
		widgets['3'] = tk.Label(self,text='Gebruikersnaam',height=2, bg='#FFFB00', font=('Arial',15))
		widgets['3'].pack(pady=10)
		self.widgets['gebruikersnaam'].pack(padx=10, pady=10)

		self.widgets['wachtwoord'] = tk.Entry(self, show='*')
		widgets['4'] = tk.Label(self,text='Wachtwoord',height=2, bg='#FFFB00', font=('Arial',15))
		widgets['4'].pack(pady=10)
		self.widgets['wachtwoord'].pack(padx=10, pady=10)

		self.widgets['button'] = tk.Button(self, text='Druk hier', command=self.clicked, font=('Arial',15))
		self.widgets['button'].pack(pady=10)
		Page.configure(self,background='#FFFB00')


	def clicked(self):
		fietsNummer = self.widgets['fietsNummer'].get()
		self.fietsNummer = fietsNummer
		gebruikersnaam = self.widgets['gebruikersnaam'].get()
		self.gebruikersnaam = gebruikersnaam
		wachtwoord = self.widgets['wachtwoord'].get()
		self.widgets['wachtwoord'].delete(0, 'end')
		self.widgets['gebruikersnaam'].delete(0, 'end')
		self.widgets['fietsNummer'].delete(0, 'end')
		db = DB()

		if db.verifyUser(gebruikersnaam, wachtwoord):
			if  True: # FIXED by Chris, sorry

				widgets = self.widgets
				tg = Telegram()
				self.widgets['msg1'] = random.randrange(1000, 9999)
				username1 = db.getUserInfo(gebruikersnaam)
				tg.sendMessage(widgets['msg1'], username1[2])
				widgets['1'].destroy()
				widgets['2'].destroy()
				widgets['3'].destroy()
				widgets['4'].destroy()
				widgets['fietsNummer'].destroy()
				widgets['gebruikersnaam'].destroy()
				widgets['wachtwoord'].destroy()
				widgets['button'].destroy()
				widgets = self.widgets
				widgets['5'] = tk.Label(self, text="Voer uw telegram verificatie code in", font=('Arial',28),bg="#FCC917")
				widgets['5'].pack(side="top", fill="both",expand=True)
				self.widgets['telegramCode'] = tk.Entry(self)
				self.widgets['telegramCode'].pack(padx=10, pady=10)
				self.widgets['button2'] = tk.Button(self, text='Druk hier', command=self.clicked2)
				self.widgets['button2'].pack(pady=10)
			else:
				messagebox.showinfo('Fout', 'Verkeerde invoergegevens')
		else:
			messagebox.showinfo('Fout', 'Verkeerde invoergegevens')

	def clicked2(self):
		tg=Telegram()
		telegramCode = self.widgets['telegramCode'].get()
		if str(self.widgets['msg1']) == str(telegramCode):
			db = DB()
			widgets = self.widgets
			widgets['5'].destroy()
			widgets['telegramCode'].destroy()
			widgets['button2'].destroy()
			if db.ophaalFiets(self.fietsNummer, self.gebruikersnaam):
				messagebox.showinfo('Succes', 'U kunt uw fiets ophalen.')
				username2 = db.getUserInfo(self.gebruikersnaam)
				tg.sendMessage('Uw fiets is opgehaald!', username2[2])
			else:
				messagebox.showinfo('Helaas', 'Deze fiets staat niet in de stalling.')
			widgets = self.widgets
			widgets['1'] = tk.Label(self, text="Ophalen", font=('Arial',42),bg="#FCC917")
			widgets['1'].pack(side="top", fill="both",expand=True)

			self.widgets['fietsNummer'] = tk.Entry(self)
			widgets['2'] = tk.Label(self,text='Fietsnummer',height=2, bg='#FCC917', font=('Arial',15))
			widgets['2'].pack(pady=10)
			self.widgets['fietsNummer'].pack(padx=10, pady=10)

			self.widgets['gebruikersnaam'] = tk.Entry(self)
			widgets['3'] = tk.Label(self,text='Gebruikersnaam',height=2, bg='#FCC917', font=('Arial',15))
			widgets['3'].pack(pady=10)
			self.widgets['gebruikersnaam'].pack(padx=10, pady=10)

			self.widgets['wachtwoord'] = tk.Entry(self, show='*')
			widgets['4'] = tk.Label(self,text='Wachtwoord',height=2, bg='#FCC917', font=('Arial',15))
			widgets['4'].pack(pady=10)
			self.widgets['wachtwoord'].pack(padx=10, pady=10)

			self.widgets['button'] = tk.Button(self, text='Druk hier', command=self.clicked, font=('Arial',15))
			self.widgets['button'].pack(pady=10)
			Page.configure(self,background='#FCC917')
		else:
			messagebox.showinfo('Error','U heeft een verkeerde code ingevoerd, probeer het opnieuw.')
