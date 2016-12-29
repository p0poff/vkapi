import vk
import json

class api:
	def __init__(self):
		self.vk = vk.vk()
		self.v = vk.init.d['v']

	def getResult(self):
		res = json.loads(self.vk.response)
		if self.vk.status==200:
			r = res['response']
		else:
			r = res['error']
		return self.vk.status, r

	def getUserInfo(self, idUser):
		self.vk.checkToken()
		url = 'https://api.vk.com/method/users.get?user_id=%s&v=%s' % (idUser, self.v)
		self.vk.send(url)
		return self.getResult()