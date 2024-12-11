import os
import configparser
from common.log import logUtils as log

class config:
	"""
	config.ini object

	config -- list with ini data
	default -- if true, we have generated a default config.ini
	"""

	config = configparser.ConfigParser()
	extra = {}
	fileName = ""		# config filename
	default = True

	# Check if config.ini exists and load/generate it
	def __init__(self, __file):
		"""
		Initialize a config object

		__file -- filename
		"""

		self.fileName = __file
		if os.path.isfile(self.fileName):
			# config.ini found, load it
			self.config.read(self.fileName)
			self.default = False
		else:
			# config.ini not found, generate a default one
			self.generateDefaultConfig()
			self.default = True

	# Check if config.ini has all needed the keys
	def checkConfig(self):
		"""
		Check if this config has the required keys

		return -- True if valid, False if not
		"""

		noneCheck = []

		try:
			# Try to get all the required keys
			noneCheck.append(self.config.get("server", "host"))
			noneCheck.append(self.config.get("server", "port"))
			noneCheck.append(self.config.get("server", "osuserverdomain"))
			noneCheck.append(self.config.get("server", "ContectEmail"))
			noneCheck.append(self.config.get("server", "debug"))
			noneCheck.append(self.config.get("server", "beatmapcacheexpire"))
			noneCheck.append(self.config.get("server", "letsapiurl"))
			noneCheck.append(self.config.get("server", "banchourl"))
			noneCheck.append(self.config.get("server", "replayspath"))
			noneCheck.append(self.config.get("server", "beatmapspath"))
			noneCheck.append(self.config.get("server", "screenshotspath"))
			noneCheck.append(self.config.get("server", "threads"))
			noneCheck.append(self.config.get("server", "gzip"))
			noneCheck.append(self.config.get("server", "gziplevel"))
			noneCheck.append(self.config.get("server", "cikey"))
			noneCheck.append(self.config.get("server", "deltaurl"))
			noneCheck.append(self.config.get("server", "publicdelta"))

			noneCheck.append(self.config.get("bancho", "apiurl"))
			noneCheck.append(self.config.get("bancho", "Apikeys"))
			noneCheck.append(self.config.get("bancho", "username"))
			noneCheck.append(self.config.get("bancho", "password"))

			noneCheck.append(self.config.get("db", "host"))
			noneCheck.append(self.config.get("db", "port"))
			noneCheck.append(self.config.get("db", "username"))
			noneCheck.append(self.config.get("db", "password"))
			noneCheck.append(self.config.get("db", "database"))
			noneCheck.append(self.config.get("db", "workers"))

			noneCheck.append(self.config.get("redis", "host"))
			noneCheck.append(self.config.get("redis", "port"))
			noneCheck.append(self.config.get("redis", "database"))
			noneCheck.append(self.config.get("redis", "password"))

			noneCheck.append(self.config.get("cheesegull", "apiurl"))
			noneCheck.append(self.config.get("cheesegull", "apikey"))

			noneCheck.append(self.config.get("sentry", "enable"))
			noneCheck.append(self.config.get("sentry", "banchodsn"))
			noneCheck.append(self.config.get("sentry", "ircdsn"))

			noneCheck.append(self.config.get("datadog", "enable"))
			noneCheck.append(self.config.get("datadog", "apikey"))
			noneCheck.append(self.config.get("datadog", "appkey"))

			noneCheck.append(self.config.get("discord", "enable"))
			noneCheck.append(self.config.get("discord", "anticheat"))
			noneCheck.append(self.config.get("discord", "ranked-std"))
			noneCheck.append(self.config.get("discord", "ranked-taiko"))
			noneCheck.append(self.config.get("discord", "ranked-ctb"))
			noneCheck.append(self.config.get("discord", "ranked-mania"))
			noneCheck.append(self.config.get("discord", "announcement"))
			noneCheck.append(self.config.get("discord", "ahook"))
			noneCheck.append(self.config.get("discord", "score"))

			noneCheck.append(self.config.get("irc", "enable"))
			noneCheck.append(self.config.get("irc", "port"))
			noneCheck.append(self.config.get("irc", "hostname"))

			noneCheck.append(self.config.get("localize", "enable"))
			noneCheck.append(self.config.get("localize", "ipapiurl"))

			noneCheck.append(self.config.get("mmdb", "id"))
			noneCheck.append(self.config.get("mmdb", "key"))

			noneCheck.append(self.config.get("cono", "enable"))

			noneCheck.append(self.config.get("custom", "config"))
			return True
		except: return False
		finally:
			if None in noneCheck or "" in noneCheck: return None
				


	# Generate a default config.ini
	def generateDefaultConfig(self):
		"""Open and set default keys for that config file"""

		# Open config.ini in write mode
		f = open(self.fileName, "w")

		# Set keys to config object
		self.config.add_section("server")
		self.config.set("server", "host", "0.0.0.0")
		self.config.set("server", "port", "6200")
		self.config.set("server", "osuserverdomain", "redstar.moe")
		self.config.set("server", "ContectEmail", "support@redstar.moe")
		self.config.set("server", "debug", "0")
		self.config.set("server", "beatmapcacheexpire", "86400")
		self.config.set("server", "letsapiurl", "http://127.0.0.1:5002/letsapi")
		self.config.set("server", "banchourl", "http://127.0.0.1:5001")
		self.config.set("server", "replayspath", "data/replays")
		self.config.set("server", "beatmapspath", "data/beatmaps")
		self.config.set("server", "screenshotspath", "data/screenshots")
		self.config.set("server", "threads", "16")
		self.config.set("server", "gzip", "1")
		self.config.set("server", "gziplevel", "6")
		self.config.set("server", "cikey", "changeme")
		self.config.set("server", "deltaurl", "delta.ppy.sh")
		self.config.set("server", "publicdelta", "0")

		self.config.add_section("bancho")
		self.config.set("bancho", "apiurl", "https://osu.ppy.sh")
		self.config.set("bancho", "Apikeys", "['Your_Bancho_APIKKEY_1', 'Your_Bancho_APIKKEY_2']")
		self.config.set("bancho", "username", "")
		self.config.set("bancho", "password", "")

		self.config.add_section("db")
		self.config.set("db", "host", "localhost")
		self.config.set("db", "port", "3306")
		self.config.set("db", "username", "root")
		self.config.set("db", "password", "")
		self.config.set("db", "database", "redstar")
		self.config.set("db", "workers", "16")

		self.config.add_section("redis")
		self.config.set("redis", "host", "localhost")
		self.config.set("redis", "port", "6379")
		self.config.set("redis", "database", "0")
		self.config.set("redis", "password", "")

		self.config.add_section("cheesegull")
		self.config.set("cheesegull", "apiurl", "http://localhost:6201/api")
		self.config.set("cheesegull", "apikey", "")

		self.config.add_section("sentry")
		self.config.set("sentry", "enable", "0")
		self.config.set("sentry", "banchodsn", "")
		self.config.set("sentry", "ircdsn", "")

		self.config.add_section("datadog")
		self.config.set("datadog", "enable", "0")
		self.config.set("datadog", "apikey", "")
		self.config.set("datadog", "appkey", "")

		self.config.add_section("discord")
		self.config.set("discord", "enable", "0")
		self.config.set("discord", "anticheat", "")
		self.config.set("discord", "ranked-std", "")
		self.config.set("discord", "ranked-taiko", "")
		self.config.set("discord", "ranked-ctb", "")
		self.config.set("discord", "ranked-mania", "")
		self.config.set("discord", "announcement", "")
		self.config.set("discord", "ahook", "")
		self.config.set("discord", "score", "")

		self.config.add_section("irc")
		self.config.set("irc", "enable", "1")
		self.config.set("irc", "port", "6667")
		self.config.set("irc", "hostname", "redstar")

		self.config.add_section("localize")
		self.config.set("localize", "enable", "1")
		self.config.set("localize", "ipapiurl", "https://ip.zxq.co")

		self.config.add_section("mmdb")
		self.config.set("mmdb", "id", "")
		self.config.set("mmdb", "key", "")

		self.config.add_section("cono")
		self.config.set("cono", "enable", "0")

		self.config.add_section("custom")
		self.config.set("custom", "config", "common/config.json")

		# Write ini to file and close
		self.config.write(f)
		f.close()

conf = config("config.ini")

if conf.default:
	# We have generated a default config.ini, quit server
	log.warning("[!] config.ini not found. A default one has been generated.")
	log.warning("[!] Please edit your config.ini and run the server again.")
	exit()

# If we haven't generated a default config.ini, check if it's valid
if False and conf.checkConfig() is None: #비활성화
	log.warning("[!] There are omissions in some setting values.")
	log.warning("[!] Please edit your config.ini and run the server again.")
	exit()
elif conf.checkConfig() is False:
	log.error("[!] Invalid config.ini. Please configure it properly")
	log.error("[!] Delete your config.ini to generate a default one")
	exit()