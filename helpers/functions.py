import os
import hashlib
import json
import time
from common.log import logUtils as log
from common.web import requestsManager
import traceback

def exceptionE(msg=""): e = traceback.format_exc(); log.error(f"{msg} \n{e}"); return e

class calculate_md5:
    @classmethod
    def file(cls, fn) -> str:
        md5 = hashlib.md5()
        with open(fn, "rb") as f:
            md5.update(f.read())
        return md5.hexdigest()

    @classmethod
    def text(cls, t) -> str:
        md5 = hashlib.md5()
        md5.update(t.encode("utf-8"))
        return md5.hexdigest()

def resPingMs(self): return (time.time() - self.request._start_time) * 1000

class setStatuscode:
    @classmethod
    def tornado405(cls, self, method=None):
        method = f"<br>Recommend {method} Method" if method else ""
        self.set_status(405)
        self.write(f"<html><title>405: Method Not Allowed</title><body>405: Method Not Allowed{method}</body></html>")

    @classmethod
    def send401(cls, self, errMsg):
        self.set_status(401)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"code": 401, "error": errMsg}, indent=2, ensure_ascii=False))
        self.set_header("Ping", str(resPingMs(self)))

    @classmethod
    def send403(cls, self, rm):
        self.set_status(403)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"code": 403, "error": f"{rm} is Not allowed!!", "message": f"contect --> {ContectEmail}"}, indent=2, ensure_ascii=False))
        self.set_header("Ping", str(resPingMs(self)))

    @classmethod
    def send404(cls, self, inputType, input):
        self.set_status(404)
        self.set_header("return-fileinfo", json.dumps({"filename": "404.html", "path": "templates/404.html", "fileMd5": calculate_md5.file("templates/404.html")}))
        self.render("templates/404.html", inputType=inputType, input=input)
        self.set_header("Ping", str(resPingMs(self)))

    @classmethod
    def send500(cls, self, inputType, input):
        self.set_status(500)
        self.set_header("return-fileinfo", json.dumps({"filename": "500.html", "path": "templates/500.html", "fileMd5": calculate_md5.file("templates/500.html")}))
        self.render("templates/500.html", inputType=inputType, input=input)
        self.set_header("Ping", str(resPingMs(self)))

    @classmethod
    def send503(cls, self, e, inputType, input):
        self.set_status(503)
        #Exception = json.dumps({"type": str(type(e)), "error": str(e)}, ensure_ascii=False)
        self.set_header("Exception", json.dumps({"type": str(type(e)), "error": str(e)}))
        self.set_header("return-fileinfo", json.dumps({"filename": "503.html", "path": "templates/503.html", "fileMd5": calculate_md5.file("templates/503.html")}))
        self.render("templates/503.html", inputType=inputType, input=input, Exception=json.dumps({"type": str(type(e)), "error": str(e)}, ensure_ascii=False))
        self.set_header("Ping", str(resPingMs(self)))

    @classmethod
    def send504(cls, self, inputType, input):
        #cloudflare 504 페이지로 연결됨
        self.set_status(504)
        self.set_header("return-fileinfo", json.dumps({"filename": "504.html", "path": "templates/504.html", "fileMd5": calculate_md5.file("templates/504.html")}))
        self.render("templates/504.html", inputType=inputType, input=input)
        self.set_header("Ping", str(resPingMs(self)))

def IDM(self, path, Range=True):
    if Range:
        idm = True
        log.info("분할 다운로드 활성화!")
        Range = self.request.headers["Range"].replace("bytes=", "").split("-")
        fileSize = os.path.getsize(path)
        start = int(Range[0])
        end = fileSize - 1 if not Range[1] else int(Range[1])
        contentLength = end - start + 1

        self.set_status(206) if start != 0 or (start == 0 and Range[1]) else self.set_status(200)
        self.set_header("Content-Length", contentLength)
        self.set_header("Content-Range", f"bytes={start}-{end}/{fileSize}")
        log.info({"Content-Range": f"bytes={start}-{end}/{fileSize}", "Content-Length": contentLength})

        with open(path, "rb") as f:
            f.seek(start)
            file = f.read(contentLength) if start != 0 or (start == 0 and Range[1]) else f.read()
            self.write(file)
    else:
        idm = False
        with open(path, 'rb') as f: self.write(f.read())

    filename = path.split("/")[-1]
    self.set_header("return-fileinfo", json.dumps({"filename": filename, "path": path, "fileMd5": calculate_md5.file(path)}))
    self.set_header('Content-Type', pathToContentType(path)["Content-Type"])
    self.set_header('Content-Disposition', f'inline; filename="{filename}"')
    self.set_header("Accept-Ranges", "bytes")
    return idm

def pathToContentType(path, isInclude=False):
    if path == 0: return None
    fn, fe = os.path.splitext(os.path.basename(path));
    ffln = path.replace(f"/{path.split('/')[-1]}", "")
    fln = os.path.splitext(os.path.basename(ffln.split('/')[-1]))[0]
    if os.name == "nt":
        while fln.endswith("."): fln = fln[:-1]

    if isInclude and ".aac" in path or not isInclude and path.endswith(".aac"): ct, tp = ("audio/aac", "audio")
    elif isInclude and ".apng" in path or not isInclude and path.endswith(".apng"): ct, tp = ("image/apng", "image")
    elif isInclude and ".avif" in path or not isInclude and path.endswith(".avif"): ct, tp = ("image/avif", "image")
    elif isInclude and ".avi" in path or not isInclude and path.endswith(".avi"): ct, tp = ("video/x-msvideo", "video")
    elif isInclude and ".bin" in path or not isInclude and path.endswith(".bin"): ct, tp = ("application/octet-stream", "file")
    elif isInclude and ".css" in path or not isInclude and path.endswith(".css"): ct, tp = ("text/css", "file")
    elif isInclude and ".gif" in path or not isInclude and path.endswith(".gif"): ct, tp = ("image/gif", "image")
    elif isInclude and ".html" in path or not isInclude and path.endswith(".html"): ct, tp = ("text/html", "file")
    elif isInclude and ".ico" in path or not isInclude and path.endswith(".ico"): ct, tp = ("image/x-icon", "image")
    elif isInclude and ".jfif" in path or not isInclude and path.endswith(".jfif"): ct, tp = ("image/jpeg", "image")
    elif isInclude and ".jpeg" in path or not isInclude and path.endswith(".jpeg"): ct, tp = ("image/jpeg", "image")
    elif isInclude and ".jpg" in path or not isInclude and path.endswith(".jpg"): ct, tp = ("image/jpeg", "image")
    elif isInclude and ".js" in path or not isInclude and path.endswith(".js"): ct, tp = ("text/javascript", "file")
    elif isInclude and ".json" in path or not isInclude and path.endswith(".json"): ct, tp = ("application/json", "file")
    elif isInclude and ".mp3" in path or not isInclude and path.endswith(".mp3"): ct, tp = ("audio/mpeg", "audio")
    elif isInclude and ".mp4" in path or not isInclude and path.endswith(".mp4"): ct, tp = ("video/mp4", "video")
    elif isInclude and ".mpeg" in path or not isInclude and path.endswith(".mpeg"): ct, tp = ("audio/mpeg", "audio")
    elif isInclude and ".oga" in path or not isInclude and path.endswith(".oga"): ct, tp = ("audio/ogg", "audio")
    elif isInclude and ".ogg" in path or not isInclude and path.endswith(".ogg"): ct, tp = ("application/ogg", "audio")
    elif isInclude and ".ogv" in path or not isInclude and path.endswith(".ogv"): ct, tp = ("video/ogg", "video")
    elif isInclude and ".ogx" in path or not isInclude and path.endswith(".ogx"): ct, tp = ("application/ogg", "audio")
    elif isInclude and ".opus" in path or not isInclude and path.endswith(".opus"): ct, tp = ("audio/opus", "audio")
    elif isInclude and ".png" in path or not isInclude and path.endswith(".png"): ct, tp = ("image/png", "image")
    elif isInclude and ".svg" in path or not isInclude and path.endswith(".svg"): ct, tp = ("image/svg+xml", "image")
    elif isInclude and ".tif" in path or not isInclude and path.endswith(".tif"): ct, tp = ("image/tiff", "image")
    elif isInclude and ".tiff" in path or not isInclude and path.endswith(".tiff"): ct, tp = ("image/tiff", "image")
    elif isInclude and ".ts" in path or not isInclude and path.endswith(".ts"): ct, tp = ("video/mp2t", "video")
    elif isInclude and ".txt" in path or not isInclude and path.endswith(".txt"): ct, tp = ("text/plain", "file")
    elif isInclude and ".wav" in path or not isInclude and path.endswith(".wav"): ct, tp = ("audio/wav", "audio")
    elif isInclude and ".weba" in path or not isInclude and path.endswith(".weba"): ct, tp = ("audio/webm", "audio")
    elif isInclude and ".webm" in path or not isInclude and path.endswith(".webm"): ct, tp = ("video/webm", "video")
    elif isInclude and ".webp" in path or not isInclude and path.endswith(".webp"): ct, tp = ("image/webp", "image")
    elif isInclude and ".zip" in path or not isInclude and path.endswith(".zip"): ct, tp = ("application/zip", "file")
    elif isInclude and ".flv" in path or not isInclude and path.endswith(".flv"): ct, tp = ("video/x-flv", "video")
    elif isInclude and ".wmv" in path or not isInclude and path.endswith(".wmv"): ct, tp = ("video/x-ms-wmv", "video")
    elif isInclude and ".mkv" in path or not isInclude and path.endswith(".mkv"): ct, tp = ("video/x-matroska", "video")

    elif isInclude and ".osz" in path or not isInclude and path.endswith(".osz"): ct, tp = ("application/x-osu-beatmap-archive", "file")
    elif isInclude and ".osr" in path or not isInclude and path.endswith(".osr"): ct, tp = ("application/x-osu-replay", "file")
    elif isInclude and ".osu" in path or not isInclude and path.endswith(".osu"): ct, tp = ("application/x-osu-beatmap", "file")
    elif isInclude and ".osb" in path or not isInclude and path.endswith(".osb"): ct, tp = ("application/x-osu-storyboard", "file")
    elif isInclude and ".osk" in path or not isInclude and path.endswith(".osk"): ct, tp = ("application/x-osu-skin", "file")

    else: ct, tp = ("application/octet-stream", "?")
    return {"Content-Type": ct, "foldername": fln, "fullFoldername": ffln, "filename": fn, "extension": fe, "fullFilename": fn + fe, "type": tp, "path": path}