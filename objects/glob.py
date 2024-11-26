"""Global objects and variables"""

import time
from common.ddog import datadogClient
from common.files import fileBuffer, fileLocks
from objects import channelList
from objects import matchList
from objects import streamList
from objects import tokenList
from common.web import schiavo

try:
	with open("version") as f: VERSION = f.read().strip()
	if VERSION == "": raise Exception
except: VERSION = "Unknown"
ACHIEVEMENTS_VERSION = 1

DATADOG_PREFIX = "ripple"
db = None
redis = None
conf = None
application = None
pool = None
pascoa = {}

BOT_NAME = "Devlant" # YOU CAN CHANGE TO YOUR BOT NAME! #
self = None
banchoConf = None
tokens = tokenList.tokenList()
channels = channelList.channelList()
matches = matchList.matchList()
verifiedCache = {}
chatFilters = None
ircServer = None
busyThreads = 0
outputRequestTime = False
outputPackets = False
gzip = False
localize = False
irc = False
restarting = False
startTime = int(time.time())
streams = streamList.streamList()

debug = False
sentry = False

# Cache and objects
fLocks = fileLocks.fileLocks()
fileBuffers = fileBuffer.buffersList()
dog = datadogClient.datadogClient()
schiavo = schiavo.schiavo()
achievementClasses = {}

# Additional modifications
COMMON_VERSION_REQ = "1.2.1"
try:
	with open("common/version") as f: COMMON_VERSION = f.read().strip()
	if COMMON_VERSION == "": raise Exception
except: COMMON_VERSION = "Unknown"