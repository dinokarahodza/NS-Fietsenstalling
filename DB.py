import sqlite3
import hashlib
import datetime

class DB():
	def __init__(self):
		self.conn = sqlite3.connect('db/NSFietsenstalling.db')
		self.c = self.conn.cursor()

	def newUser(self, username, password, telegram_id, full_name):
		if not self.getUserInfo(username):
			self.c.execute("INSERT INTO gebruiker VALUES(?,?,?,?)", [username, hashlib.sha256(str.encode(password)).hexdigest(), telegram_id, full_name]) #voegt de gebruiker toe aan de tabel gebruiker
			self.conn.commit()
			return True
		return False

	def newFiets(self, username, fietscode):
		if not self.checkFietsExists(fietscode):
			self.c.execute("INSERT INTO fiets VALUES(?,?,?)", [int(fietscode), 0, username])
			self.conn.commit()
			return True
		return False

	def ophaalFiets(self, fietscode, username):
		self.c.execute("SELECT in_stalling FROM fiets WHERE fietscode = ? AND in_stalling = 1 AND gebruikersnaam = ?",[fietscode, username])
		data = self.c.fetchone()
		if data:
			self.c.execute("UPDATE fiets SET in_stalling = 0 WHERE fietscode = ?",[fietscode])
			self.c.execute("INSERT INTO stalling_log (fietscode, timestamp, inorout) VALUES(?,?,?)",[fietscode, str(datetime.datetime.now()).split('.')[0],"out"])
			self.conn.commit()
			return True
		return False

	def stalFiets(self, fietscode, username):
		self.c.execute("SELECT in_stalling FROM fiets WHERE fietscode = ? AND in_stalling = 0 AND gebruikersnaam = ?",[fietscode, username])
		data = self.c.fetchone()
		if data:
			self.c.execute("UPDATE fiets SET in_stalling = 1 WHERE fietscode = ?",[fietscode])
			self.c.execute("INSERT INTO stalling_log (fietscode, timestamp, inorout) VALUES(?,?,?)",[fietscode, str(datetime.datetime.now()).split('.')[0],"in"])
			self.conn.commit()
			return True
		return False

	def verifyUser(self, username, password):
		self.c.execute("SELECT * FROM gebruiker WHERE gebruikersnaam = ? LIMIT 1", [username])
		data = self.c.fetchone()
		if data and data[1] == hashlib.sha256(str.encode(password)).hexdigest():
			return True
		return False

	def getUserInfo(self, username):
		self.c.execute("SELECT * FROM gebruiker WHERE gebruikersnaam = ?", [username])
		data = self.c.fetchone()
		if data == None:
			return False
		return data

	def execute(self, query, params):
		self.c.execute(query, params)
		return self.c.fetchall()

	def checkFietsExists(self, fietscode):
		self.c.execute("SELECT fietscode FROM fiets WHERE fietscode = ?", [fietscode])
		if self.c.fetchall():
			return True
		return False

	def getUserFietsen(self, username):
		self.c.execute("SELECT fietscode, in_stalling FROM fiets WHERE gebruikersnaam = ?", [username])
		return self.c.fetchall()