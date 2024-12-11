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

from handlers import MainHandler
from handlers import faviconHandler
from handlers import AvatarHandler

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