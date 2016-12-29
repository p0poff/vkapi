import time

class vktime:
	def __init__(self):
		self.savedTime = self.getCurTime()

	def getCurTime(self):
		return int(time.time())

	def setSavedTime(self, t):
		self.savedTime = t

	def timeIsEmpty(self, expires):
		curTime = self.getCurTime()
		delta = curTime - self.savedTime
		if delta >= expires:
			res = True
		else:
			res = False

		return res, curTime