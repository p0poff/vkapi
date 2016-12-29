import requests
import vktime
import init
import json

class vk:
	def __init__(self):
		self.time = vktime.vktime()

		self.access_token = ''
		self.expires = 0

		self.response = {}
		self.status = 0

	def checkToken(self):
		timeEmpty, curTime = self.time.timeIsEmpty(self.expires)
		if timeEmpty == True:
			while True:
				error, req = self.getAccessToken()
				if error == False:
					break
			self.access_token = req.get('access_token', '')
			self.expires = req.get('expires_in', 0)
			self.time.setSavedTime(curTime)

	def send(self, url):
		r = requests.get(url=url)
		self.status = r.status_code
		try:
			self.response = r.text
		except:
			print('send %s wrong')
			self.response = {}

	def getResponse(self):
		return self.response

	def getStatus(self):
		return self.status

	def getAccessToken(self):
		authUrl = 'https://oauth.vk.com/authorize?client_id=%s&display=page&redirect_uri=%s&scope=friends&response_type=code&v=%s' % (init.d['client_id'], init.d['redirect_uri'], init.d['v'])
		print('*********************************')
		print(authUrl)
		print('write CODE')
		code = input()
		tokenUrl = 'https://oauth.vk.com/access_token?client_id=%s&client_secret=%s&redirect_uri=%s&code=%s' % (init.d['client_id'], init.d['client_secret'], init.d['redirect_uri'], code)
		r = requests.get(url=tokenUrl)
		try:
			res = json.loads(r.text)
		except:
			print('ERROR request get token...')
			return True, {}

		if 'error' in res:
			print('ERROR... - %s, %s' % (res['error'], res['error_description']))
			return True, {}

		return False, res