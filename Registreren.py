from Page import Page
import tkinter as tk
import random
from Telegram import Telegram
from tkinter import messagebox
from DB import DB
from Barcode import Barcode

class Registreren(Page):
    widgets={}
    randomcode = 0
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        widgets = self.widgets
        label = tk.Label(self, text="Registreren", font=('Arial',39),bg="#FFFB00")
        label.pack(side="top", fill="both", expand=True)

        label = tk.Label(self,text='Gebruikersnaam',height=2, font=('Arial',15),bg="#FFFB00")
        label.pack(pady=5,side="top", fill="both")
        self.entrynaam = tk.Entry(self)
        self.entrynaam.pack()

        label = tk.Label(self,text='Volledige Naam',height=2,font=('Arial',15),bg="#FFFB00")
        label.pack(pady=5,side="top", fill="both")
        self.entryvolnaam = tk.Entry(self)
        self.entryvolnaam.pack()

        label = tk.Label(self,text='Wachtwoord', height=2,font=('Arial',15),bg="#FFFB00")
        label.pack(pady=5,side="top", fill="both")
        self.entrywachtwoord = tk.Entry(self,show='*')
        self.entrywachtwoord.pack()

        self.randomcode=random.randrange(1000,9999)
        label = tk.Label(self,text='',height=2,font=('Arial',7),bg="#FFFB00")
        label.pack(pady=2,side="top", fill="both")
        self.qrCode = tk.PhotoImage(file='assets/frame.png')
        self.qrCodeLabel = tk.Label(self, image=self.qrCode, highlightthickness=0, borderwidth =2, relief='flat')
        self.qrCodeLabel.pack()

        self.button = tk.Button(self, text="Ja, ik heb de code verstuurd en wil me registreren", command=self.buttonconfirm)
        self.button.pack(padx=10,pady=10)
        widgets['labelrandomcode'] = tk.Label(self, text='Verstuur naar de \'@NS-Fietsenstalling\' op Telegram deze code: '+str(self.randomcode), font=('Arial',19),bg="#FFFB00")
        widgets['labelrandomcode'].pack(side="top", fill="both", expand=True)
        Page.configure(self,background='#FFFB00')

    def buttonconfirm(self):
        tg= Telegram()
        db = DB()
        box=messagebox.showinfo
        naam = self.entrynaam.get()
        volnaam = self.entryvolnaam.get()
        wachtwoord= self.entrywachtwoord.get()
        telegramId = tg.registerUser(str(self.randomcode))
        self.entrywachtwoord.delete(0, 'end')
        self.entryvolnaam.delete(0, 'end')
        self.entrynaam.delete(0, 'end')
        if volnaam=='':
            messagebox.showinfo('Er is een fout opgetreden!','Geen naam ingevoerd!')
        elif volnaam!='':
            if wachtwoord=='':
                messagebox.showinfo('Er is een fout opgetreden!','Geen wachtwoord ingevoerd!')
            else:
                if naam=='':
                    messagebox.showinfo('Er is een fout opgetreden!','Geen gebruikersnaam ingevoerd')
                elif naam!='':
                    if db.getUserInfo(naam):
                        messagebox.showinfo('Er is een fout opgetreden!','Gebruikersnaam is al in gebruik!')
                    else:
                        if telegramId:
                            code=random.randrange(10000,99999)
                            messagebox.showinfo('Gelukt!','U bent geregistreerd! Uw fietscode is: '+str(code))
                            msg='Uw fietscode is: {}'.format(code)
                            Barcode(code)
                            tg.sendMessage(msg,telegramId)
                            db.newUser(naam,wachtwoord,telegramId, volnaam)
                            db.newFiets(naam,int(code))
                            widgets=self.widgets
                            widgets['labelrandomcode'].destroy()
                            self.randomcode=random.randrange(1000,9999)
                            widgets['labelrandomcode'] = tk.Label(self, text='Verstuur naar de \'@NS-Fietsenstalling\' op Telegram deze code: '+str(self.randomcode), font=('Arial',19),bg="#FFFB00")
                            widgets['labelrandomcode'].pack(side="top", fill="both", expand=True)
                        else:
                            messagebox.showinfo('Er is een fout opgetreden!','Check of u de bovenstaande code goed heeft verstuurd')
