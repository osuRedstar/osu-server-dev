import os
import tornado.ioloop
import tornado.web
import json
from common.log import logUtils as log
from common.db import dbConnector
from multiprocessing.pool import ThreadPool
from objects import glob
import redis

from handlers import MainHandler
#from helpers import getmmdb

glob.pool = ThreadPool(4)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler.handler),
    ])

if __name__ == "__main__":
    #getmmdb.dl() #config 설정완료시 활성화 하기

    #glob.db = dbConnector.db(glob.conf.config["db"]["host"], glob.conf.config["db"]["username"], glob.conf.config["db"]["password"], glob.conf.config["db"]["database"], int(glob.conf.config["db"]["workers"]))
    glob.db = dbConnector.db("127.0.0.1", "osu", "821059401241", "redstar", 4)

    #glob.redis = redis.Redis(glob.conf.config["redis"]["host"], glob.conf.config["redis"]["port"], glob.conf.config["redis"]["database"], glob.conf.config["redis"]["password"])
    glob.redis = redis.Redis("127.0.0.1", 6379, 0, 821059401241)
    glob.redis.ping()


    glob.application = make_app()
    port = 10000
    glob.application.listen(port)
    log.info(f"Server Listen on http://localhost:{port} Port | OS = {'Windows' if os.name == 'nt' else 'UNIX'}")
    tornado.ioloop.IOLoop.current().start()