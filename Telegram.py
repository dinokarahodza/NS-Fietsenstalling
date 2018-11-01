import http.client, urllib.parse
from time import time
import json

class Telegram():

	apiKey = "782863527:AAHegFz4QG7lwhgCHRUoe3xW5LHxdoD21x4"
	api = "api.telegram.org"

	def doRequest(self, apiMethod, data):
		params = urllib.parse.urlencode(data)
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn = http.client.HTTPSConnection(self.api)
		conn.request("POST", "/" + self.apiKey + "/" + apiMethod, params, headers)
		response = conn.getresponse()
		return [response.status, response.reason, response.read().decode('utf-8')]

	def sendMessage(self, msg, username):
		self.doRequest("sendMessage", {'chat_id': username, 'text': msg})

	def registerUser(self, code):
		result = json.loads(self.doRequest("getUpdates", {'update_id': int(time()) })[2])
		for x in result['result']:
			if code == x['message']['text']:
				return x['message']['chat']['id']
		return False