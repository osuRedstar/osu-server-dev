import tornado.gen
import tornado.web

from common.log import logUtils as log
from common.web import requestsManager
from helpers.functions import *
from common.sentry import sentry
import re
import urllib.request
import random
from objects import glob

class handler(requestsManager.asyncRequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self, num):
		# create avatars directory if it does not exist
		if not os.path.exists("avatars/avatars"): os.makedirs("avatars/avatars")
		if not os.path.exists("avatars/bancho"): os.makedirs("avatars/bancho")

		if self.request.host.startswith("a."): #avatarserver
			if re.match(r"^/\d+$", self.request.uri):
				avatarid = num if os.path.isfile(f"avatars/avatars/{num}.png") else -1
				IDM(self, f"avatars/avatars/{avatarid}.png", Range=False)
				log.info(f"[avatarserver] | {self.getRequestIP()} - - {self.request.uri}")
			elif re.match(r"^/bancho/id/\d+$", self.request.uri):
				avatarid = int(self.request.uri.replace("/bancho/id/", ""))
				if not os.path.isfile(f"avatars/bancho/{avatarid}.png"): #Check if avatar exists
					urllib.request.urlretrieve(f"https://a.ppy.sh/{avatarid}", f"avatars/bancho/{avatarid}.png")
				IDM(self, f"avatars/bancho/{avatarid}.png", Range=False)
			elif re.match(r"^/bancho/u/[a-zA-Z0-9_]+$", self.request.uri):
				avatarid = self.request.uri.replace("/bancho/u/", "")
				API_key = random.choice(eval(glob.conf.config["bancho"]["apikeys"]))
				avatarid = json.loads(urllib.request.urlopen(f"https://osu.ppy.sh/api/get_user?k={API_key}&u={avatarid}", timeout=3).read().decode())[0]['user_id']
				if not os.path.isfile(f"avatars/bancho/{avatarid}.png"): #Check if avatar exists
					urllib.request.urlretrieve(f"https://a.ppy.sh/{avatarid}", f"avatars/bancho/{avatarid}.png")
				IDM(self, f"avatars/bancho/{avatarid}.png", Range=False)
		else: setStatuscode.tornado404(self)