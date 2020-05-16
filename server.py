from aiohttp import web
from aiohttp import ClientSession
from functools import lru_cache
from io import BytesIO
from collections import Counter
import json
from uuid import uuid4
from time import time
import asyncio

import pprint
import geoip2.database

GEO_IP = geoip2.database.Reader('./GeoLite2-City.mmdb')
RATER_COOKIE = "nikoRateLimiterID"
TELEGRAM_TOKEN = "1095344417:AAEc0suB1LIY4nhMTeR_EGXnaArDlX693tE"
TELEGRAM_BOT_SEND_MESS_URL = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage'
TELEGRAM_BOT_SEND_FILE_URL = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendDocument'


async def telegram_send(bot_message):
    _p = dict(chat_id=354451358, parse_mode='Markdown', text=bot_message)
    async with ClientSession() as session:
        async with session.get(TELEGRAM_BOT_SEND_MESS_URL, params=_p):
            return


async def telegram_send_as_file(bio):
    _p = dict(chat_id="354451358")
    async with ClientSession() as session:
        async with session.get(TELEGRAM_BOT_SEND_FILE_URL, data={'document': bio, **_p}) as p:
            return


STATISTICS = {}
STATISTICS_EVENTS = {'uuid': [], 'time': [], 'ipad': [], 'cont': [], 'city': [], 'item': []}


async def shed(_):
    STATISTICS["time_start"] = time()
    asyncio.create_task(notify())


async def notify():
    while True:
        for _ in range(6):
            await asyncio.sleep(60 * 60)
            uuids = Counter(STATISTICS_EVENTS['uuid'])
            uniq = len(uuids.keys())
            total = len(STATISTICS_EVENTS['uuid'])
            uptime = int(time() - STATISTICS["time_start"])
            citys = Counter(STATISTICS_EVENTS['city'])
            STATISTICS["time_up"] = str.join(":",
                [str(i).zfill(2) for i in [uptime // (60 * 60), (uptime // 60) % 60, uptime % 60]]
            )
            await telegram_send(f"""
__Uptime__: {STATISTICS["time_up"]}
__Users__: {uniq}/{total}
{pprint.pformat(citys.__dict__)}
""")
        bio = BytesIO(json.dumps(STATISTICS_EVENTS).encode())
        bio.name = "stat.json"
        await telegram_send_as_file(bio)


@lru_cache(1)
def get_index_html(_):
    with open("web/index.html", "rb") as file:
        return file.read()


@lru_cache(1)
def get_preview_html(_):
    with open("web/preview.html", "rb") as file:
        return file.read()


async def register_connection(uuid, request: web.Request, item="index"):
    STATISTICS_EVENTS['uuid'].append(uuid)
    STATISTICS_EVENTS['time'].append(int(time()))
    STATISTICS_EVENTS['ipad'].append(request.remote)
    STATISTICS_EVENTS['item'].append(item)
    try:
        geo_info = GEO_IP.city(request.remote)
        STATISTICS_EVENTS['city'].append(geo_info.city.names['ru'])
        STATISTICS_EVENTS['cont'].append(geo_info.country.iso_code)
    except Exception:
        STATISTICS_EVENTS['city'].append('')
        STATISTICS_EVENTS['cont'].append('')


async def index(request: web.Request):
    await request.release()
    who = request.cookies.get(RATER_COOKIE)
    if who is None:
        who = str(uuid4())
    await register_connection(who, request)
    response = web.Response(body=get_index_html(time()), content_type="text/html", charset="utf-8")  # TODO time remove
    response.cookies[RATER_COOKIE] = who
    return response


async def preview(request: web.Request):
    await request.release()
    item = request.match_info['path'].strip("/")
    who = request.cookies.get(RATER_COOKIE)
    if who is None:
        who = str(uuid4())
    await register_connection(who, request, item)
    response = web.Response(body=get_preview_html(time()), content_type="text/html", charset="utf-8")  # TODO time remove
    response.cookies[RATER_COOKIE] = who
    return response


async def shirt(request: web.Request):
    item = request.match_info['path'].strip("/")
    lib, file_name = item.split("/")
    if file_name == "tee.jpg":
        file_name = lib + "/" + file_name
    with open("web/shirt/" + file_name, 'rb') as file:
        data = file.read()
        response = web.Response(body=data)
    return response


async def error_middleware(_, handler):
    async def middleware_handler(request):
        try:
            response = await handler(request)
            return response
        except Exception as ex:
            await telegram_send("__ERROR:__ " + repr(ex))
            return web.Response(text="Incident will be reported. Your data saved.")
    return middleware_handler


app = web.Application()
app.add_routes([
    web.static('/such_static/', "./web/"),
    web.get('/', index),
    web.get('/preview/{path:.*}', preview),
    web.get('/shirt/{path:.*}', shirt),
])
app.on_startup.append(shed)
app.middlewares.append(error_middleware)
web.run_app(app, host="127.0.0.1")
