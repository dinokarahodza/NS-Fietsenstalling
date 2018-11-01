from Page import Page
import tkinter as tk

class Home(Page):
	def __init__(self, *args):
		Page.__init__(self, *args)
		tekst = tk.Label(self, text="Welkom bij de\nNS Fietsenstalling", bg="#FFFB08", font=("Arial", 39))
		tekst.pack(side="top", fill="both", expand=True)
		Page.configure(self,background='#FFFB08')
