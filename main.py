import os
import tornado.ioloop
import tornado.web
import json
from objects import glob
from helpers import configHelper
from common.log import logUtils as log
from common.db import dbConnector
from multiprocessing.pool import ThreadPool
import redis
from helpers.functions import IDM
from helpers import getmmdb

from handlers import MainHandler, faviconHandler, AvatarHandler
from handlers import apiFokabotMessageHandler
from handlers import apiDeltaClients
from handlers import apiIsOnlineHandler
from handlers import apiOnlineUsersHandler
from handlers import apiServerStatusHandler
from handlers import apiVerifiedStatusHandler
from handlers import ciTriggerHandler
from handlers import menuIconHandler
from handlers import apiCacheBeatmapHandler, rateHandler, changelogHandler
from handlers import apiPPHandler
from handlers import apiStatusHandler
from handlers import banchoConnectHandler
from handlers import checkUpdatesHandler
from handlers import downloadMapHandler
from handlers import emptyHandler
from handlers import getBeatmapinfoHandler
from handlers import getFullReplayHandler
from handlers import getFullReplayHandlerRelax
from handlers import getFullReplayHandlerAutopilot
from handlers import getReplayHandler
from handlers import getScoresHandler
from handlers import getScreenshotHandler
from handlers import getSeasonalHandler
from handlers import loadTestHandler
from handlers import mapsHandler
from handlers import inGameRegistrationHandler
from handlers import getFullErrorHandler
from handlers import osuErrorHandler
from handlers import osuSearchHandler
from handlers import osuSearchSetHandler
from handlers import osuSessionHandler
from handlers import redirectHandler
from handlers import submitModularHandler
from handlers import uploadScreenshotHandler
from handlers import commentHandler
from handlers import lastFMHandler
from handlers import findBeatmapMd5Handler
from handlers import getfriends
from handlers import replayParserHandler
from handlers import give_betatagHandler
from handlers import bmsubmitGetid
from handlers import getBeatmapTopic
from handlers import bmsubmitUpload
from handlers import bmsubmitPost

def make_app():
    return tornado.web.Application([
        #(r"/favicon.ico", tornado.web.StaticFileHandler, {"path": "/"}),
        (r"/favicon.ico", faviconHandler.handler),
        (r"/", MainHandler.handler),
        (r"/(\d+)", AvatarHandler.handler), #(r"/([^/]+)", AvatarHandler.handler),
        (r"/bancho/id/(\d+)", AvatarHandler.handler),
        (r"/bancho/u/([^/]+)", AvatarHandler.handler),

        #pep
        (r"/api/v1/isOnline", apiIsOnlineHandler.handler),
		(r"/api/v1/onlineUsers", apiOnlineUsersHandler.handler),
		(r"/api/v1/serverStatus", apiServerStatusHandler.handler),
		(r"/api/v1/ciTrigger", ciTriggerHandler.handler),
		(r"/api/v1/verifiedStatus", apiVerifiedStatusHandler.handler),
		(r"/api/v1/fokabotMessage", apiFokabotMessageHandler.handler),
		(r"/api/v2/clients/.*", apiDeltaClients.handler),
		(r"/menu-content.json", menuIconHandler.handler),



        #lets
        (r"/letsapi/v1/find-beatmap-md5", findBeatmapMd5Handler.handler),
		(r"/web/osu-getfriends.php", getfriends.handler),
		(r"/web/replayparser", replayParserHandler.handler),
		(r"/web/frontend/give-betatag/(.*)", give_betatagHandler.handler),
		#Beatmap Submit System
		(r"/web/osu-osz2-bmsubmit-getid.php", bmsubmitGetid.handler),
		(r"/web/osu-get-beatmap-topic.php", getBeatmapTopic.handler),
		(r"/web/osu-osz2-bmsubmit-upload.php", bmsubmitUpload.handler),
		(r"/web/osu-osz2-bmsubmit-post.php", bmsubmitPost.handler),
		(r"/users", inGameRegistrationHandler.handler),
		(r"/web/bancho_connect.php", banchoConnectHandler.handler),
		(r"/web/osu-osz2-getscores.php", getScoresHandler.handler),
		(r"/web/osu-submit-modular.php", submitModularHandler.handler),
		(r"/web/osu-submit-modular-selector.php", submitModularHandler.handler),
		(r"/web/osu-getbeatmapinfo.php", getBeatmapinfoHandler.handler),
		(r"/web/osu-getreplay.php", getReplayHandler.handler),
		(r"/web/osu-getseasonal.php", getSeasonalHandler.handler),
		(r"/web/osu-screenshot.php", uploadScreenshotHandler.handler),
		(r"/web/osu-search.php", osuSearchHandler.handler),
		(r"/web/osu-search-set.php", osuSearchSetHandler.handler),
		(r"/web/osu-session.php", osuSessionHandler.handler),
		(r"/web/check-updates.php", checkUpdatesHandler.handler),
		(r"/web/osu-error.php", osuErrorHandler.handler),
		(r"/web/osu-comment.php", commentHandler.handler),
		(r"/p/changelog", changelogHandler.handler),
		(r"/web/changelog.php", changelogHandler.handler),
		(r"/home/changelog", changelogHandler.handler),
		(r"/web/osu-rate.php", rateHandler.handler),
		(r"/ss/(.*)", getScreenshotHandler.handler),
		(r"/web/maps/(.*)", mapsHandler.handler),
		(r"/d/(.*)", downloadMapHandler.handler),
		(r"/s/(.*)", downloadMapHandler.handler),
		(r"/web/replays/(.*)", getFullReplayHandler.handler),
		(r"/web/replays_relax/(.*)", getFullReplayHandlerRelax.handler),
		(r"/web/replays_ap/(.*)", getFullReplayHandlerAutopilot.handler),
		(r"/web/errorlogs/(.*)", getFullErrorHandler.handler),
		(r"/p/verify", redirectHandler.handler, dict(destination=f"https://{server_domain}/")),
		(r"/u/(.*)", redirectHandler.handler, dict(destination=f"https://{server_domain}" + "/u/{}")),
		(r"/api/v1/status", apiStatusHandler.handler),
		(r"/api/v1/pp", apiPPHandler.handler),
		(r"/api/v1/cacheBeatmap", apiCacheBeatmapHandler.handler),
		(r"/letsapi/v1/status", apiStatusHandler.handler),
		(r"/letsapi/v1/pp", apiPPHandler.handler),
		(r"/letsapi/v1/cacheBeatmap", apiCacheBeatmapHandler.handler),
		(r"/web/lastfm.php", lastFMHandler.handler),
		# Not done yet
		(r"/web/osu-get-beatmap-topic.php", emptyHandler.handler), # Beatmap Topic
		(r"/web/osu-markasread.php", emptyHandler.handler), # Mark As Read
		(r"/web/osu-addfavourite.php", emptyHandler.handler), # Add Favorite
		(r"/web/osu-checktweets.php", emptyHandler.handler), # Do we need this?
		(r"/loadTest", loadTestHandler.handler),
    ])

if __name__ == "__main__":
    glob.conf = configHelper.config("config.ini")
    getmmdb.dl() #config 설정완료시 활성화 하기

    glob.pool = ThreadPool(4) #config.ini에 해당 값 있음

    #glob.db = dbConnector.db(glob.conf.config["db"]["host"], glob.conf.config["db"]["username"], glob.conf.config["db"]["password"], glob.conf.config["db"]["database"], int(glob.conf.config["db"]["workers"]))
    glob.db = dbConnector.db("127.0.0.1", "osu", "821059401241", "redstar", 4)

    #glob.redis = redis.Redis(glob.conf.config["redis"]["host"], glob.conf.config["redis"]["port"], glob.conf.config["redis"]["database"], glob.conf.config["redis"]["password"])
    glob.redis = redis.Redis("127.0.0.1", 6379, 0, "821059401241")
    glob.redis.ping()

    glob.application = make_app()
    port = 10000
    glob.application.listen(port)
    log.info(f"Server Listen on http://localhost:{port} Port | OS = {'Windows' if os.name == 'nt' else 'UNIX'}")
    tornado.ioloop.IOLoop.current().start()