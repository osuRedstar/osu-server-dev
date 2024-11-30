from common.web import requestsManager
from helpers.functions import IDM

class handler(requestsManager.asyncRequestHandler):
	def asyncGet(self): IDM(self, "favicon.ico", Range=False)