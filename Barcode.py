import http.client

class Barcode(object):
	def __init__(self, code):
		self.downloadImage(code, str(code) + ".png")
	def downloadImage(self, code, location):
		conn = http.client.HTTPConnection("www.barcodes4.me")
		conn.request("GET", "/barcode/c128a/frame" + str(code) + ".png")
		r1 = conn.getresponse()
		with open("tmp/" + location, 'bw+') as f:
			f.write(r1.read())
