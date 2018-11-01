from Page import Page
import tkinter as tk
from DB import DB
from Telegram import Telegram
from Barcode import Barcode
import random
from tkinter import messagebox, END

class informatie(Page):
	db = DB()
	tg = Telegram()
	w = {}
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		Page.configure(self,background='#FFFB00')
		self.infoStart()

	def infoStart(self):
		for i in self.w:
			self.w[i].pack_forget()

		self.w['title'] = tk.Label(self, text="Meer informatie", font=('Arial',39),bg="#FFFB00")
		self.w['title'].pack()

		self.w['description'] = tk.Label(self, bg="#FFFB00", text="Maar hieronder de keuze of u algemene informatie \nover het stallen van uw fiets wilt zien of uw persoonlijke informatie wil bekijken en/of bijwerken.")
		self.w['description'].pack(side="top", fill="both", expand=True)

		self.w['generalInfoButton'] = tk.Button(self, text="Algemene Informatie", command=self.generalInfo,bg="#FFFB00")
		self.w['generalInfoButton'].pack()

		self.w['userInfoButton'] = tk.Button(self, text="Gebruikersinformatie", command=self.userInfo,bg="#FFFB00")
		self.w['userInfoButton'].pack()

	def userInfo(self):

		for i in self.w:
			self.w[i].pack_forget()

		self.w['title']["text"] = "Inloggen"
		self.w['title'].pack()

		self.w['labelUsername'] = tk.Label(self, bg="#FCC917", text="Gebruikersnaam")
		self.w['labelUsername'].pack()

		self.w['username'] = tk.Entry(self)
		self.w['username'].pack()

		self.w['labelPassword'] = tk.Label(self, bg="#FCC917", text="Password")
		self.w['labelPassword'].pack()

		self.w['password'] = tk.Entry(self,show='*')
		self.w['password'].pack()

		self.w['loginButton'] = tk.Button(self, text="Login", command=self.login,bg="#FFFB00")
		self.w['loginButton'].pack()


	def login(self):
		username = self.w['username'].get()
		password = self.w['password'].get()
		if self.db.verifyUser(username, password):
			self.askTelegramCode(username)
		else:
			messagebox.showinfo("Helaas", "Uw deze combinatie van gebruikersnaam en wachtwoord komt niet voor in ons systeem.")

	def askTelegramCode(self, username):
		for i in self.w:
			self.w[i].pack_forget()

		self.userdata = self.db.getUserInfo(username)
		self.sendTgCode = random.randrange(1000, 9999)
		self.tg.sendMessage(self.sendTgCode, self.userdata[2])

		self.w['title']["text"] = "Voer uw Telegram code in"
		self.w['title'].pack()

		self.w['description']["text"] = "Er is een code naar uw Telegram account verzonden, voer deze hieronder in om in te loggen."
		self.w['description'].pack()

		self.w['tgCode'] = tk.Entry(self)
		self.w['tgCode'].pack()

		self.w['login'] = tk.Button(self, text="Login", command=self.checkTgCode, bg="#FCC917")
		self.w['login'].pack()

		self.w['back'] = tk.Button(self, text="Terug", command=self.infoStart, bg="#FCC917")
		self.w['back'].pack()


	def checkTgCode(self):
		if str(self.w['tgCode'].get()) == str(self.sendTgCode):
			self.showUserInfo(self.userdata)
		else:
			messagebox.showinfo("Helaas", "De ingevoerde code komt niet overeen met de toegestuude code, vul de toegestuude code correct in.")

	def showUserInfo(self, userdata): # Na login laat deze functie alle gebruikersinfo zien
		for i in self.w:
			self.w[i].pack_forget()

		self.w['title']["text"] = "Persoonlijke gegevens"
		self.w['title'].pack()

		self.w['showFullname'] = tk.Label(self, bg="#FCC917", text="Volledige naam \t" + userdata[3])
		self.w['showFullname'].pack()

		self.w['showUsername'] = tk.Label(self, bg="#FCC917", text="Gebruikersnaam \t" + userdata[0])
		self.w['showUsername'].pack()

		self.w['showTelegramId'] = tk.Label(self, bg="#FCC917", text="Telegram id \t" + userdata[2])
		self.w['showTelegramId'].pack()

		self.w['showRegisteredBikes'] = tk.Label(self, bg="#FCC917", text="Uw geregistreerde fietsen:")
		self.w['showRegisteredBikes'].pack()

		self.w['showBicycles'] = tk.Listbox(self, font=("Courier", "16"))
		self.w['showBicycles'].pack()

		bicycles = self.db.getUserFietsen(userdata[0])
		self.w['showBicycles'].insert(END, "#\t\tin stalling?")
		for bicycle in bicycles:
			status = "Ja"
			if bicycle[1] == 0:
				status = "Nee"
			self.w['showBicycles'].insert(END, str(bicycle[0]) + "\t\t\t\t\t" + status)


		self.w['addBicycle'] = tk.Button(self, text="Nog een Fiets Registeren", command=self.registerBike, bg="#FCC917")
		self.w['addBicycle'].pack()

		self.w['back'] = tk.Button(self, text="Terug", command=self.infoStart, bg="#FCC917")
		self.w['back'].pack()

	def registerBike(self):
		code = code=random.randrange(10000, 99999)
		while self.db.checkFietsExists(code):
			code = code=random.randrange(10000, 99999)
		self.db.newFiets(self.userdata[0], code)
		messagebox.showinfo("Succes!", "Uw nieuwe fiets is geregistreerd met de code " + str(code))
		self.tg.sendMessage("U heeft uw nieuwe fiets succesvol geregistreerd! De bijbehorende fietscode is: " + str(code), self.userdata[2])
		Barcode(code)



	def generalInfo(self):
		for i in self.w:
			self.w[i].pack_forget()

		self.w['title']["text"] = "Algemene informatie"
		self.w['title'].pack()

		self.w['description']["text"] = "Deze applicatie is geschreven door Dino & Naishel"
		self.w['description'].pack()

		self.w['back'] = tk.Button(self, text="Terug", command=self.infoStart, bg="#FCC917")
		self.w['back'].pack()
