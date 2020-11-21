from aiohttp import web
from aiohttp import ClientSession
from functools import lru_cache
from io import BytesIO
from collections import Counter
from datetime import datetime, timezone, timedelta
import textwrap
from uuid import uuid4
from time import time
import asyncio
import traceback
from tabulate import tabulate
import sys
import pprint
from ua_parser import user_agent_parser
import json
import random
from pathlib import Path


DEV = '-dev' in sys.argv
RATER_COOKIE = "nikoRateLimiterID"
TELEGRAM_TOKEN = "1095344417:AAEc0suB1LIY4nhMTeR_EGXnaArDlX693tE"
TELEGRAM_BOT_SEND_MESS_URL = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage'
TELEGRAM_BOT_SEND_FILE_URL = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendDocument'


async def telegram_send(bot_message):
    if DEV:
        print(bot_message)
        return
    _p = dict(chat_id=354451358, text=bot_message)
    async with ClientSession() as session:
        async with session.get(TELEGRAM_BOT_SEND_MESS_URL, params=_p):
            return


async def telegram_send_as_file(bio):
    if DEV:
        with open("biosave_" + bio.name, "wb") as f:
            f.write(bio.read())
        print(bio.name, "saved.")
        return
    _p = dict(chat_id="354451358")
    async with ClientSession() as session:
        async with session.get(TELEGRAM_BOT_SEND_FILE_URL, data={'document': bio, **_p}) as p:
            return


STATISTICS = {}
SAVE_FILE_ANALYTICS_PATH = Path("./analy.ze")
if not DEV and SAVE_FILE_ANALYTICS_PATH.exists():
    with open(SAVE_FILE_ANALYTICS_PATH) as f_:
        backup = json.load(f_)
    STATISTICS_EVENTS = backup
else:
    STATISTICS_EVENTS = {'uuid': [], 'time': [], 'lang': [], 'ipad': [], 'cont': [], 'city': [], 'item': [], 'os': [],
                         'ua': []}


async def shed(_):
    STATISTICS["time_start"] = time()
    asyncio.create_task(notify())


async def notify():
    while True:
        for i in range(4):
            users_unique = len(Counter(STATISTICS_EVENTS['uuid']).keys())
            users_total = len(STATISTICS_EVENTS['uuid'])
            up_time = int(time() - STATISTICS["time_start"])
            cities = Counter(STATISTICS_EVENTS['city'])
            try:
                cities.pop("")
            except Exception:
                pass
            STATISTICS["time_up"] = str.join(
                ":",
                [str(i).zfill(2) for i in [up_time // (60 * 60), (up_time // 60) % 60, up_time % 60]]
            )
            print(f'**Uptime**: {STATISTICS["time_up"]}\n'
                  f'**Users**: {users_unique}/{users_total}\n'
                  f'''{pprint.pformat(dict(cities)).replace("'", "")}''')
            await asyncio.sleep(15 * (60 + i))


@lru_cache(1)
def get_index_html(_):
    with open("web/index.html", "rb") as f:
        return f.read()


@lru_cache(1)
def get_preview_html(_):
    with open("web/preview.html", "rb") as f:
        return f.read()


async def register_connection(uuid, request: web.Request, item="index"):
    STATISTICS_EVENTS['uuid'].append(uuid)
    STATISTICS_EVENTS['time'].append(datetime.now(tz=timezone(timedelta(hours=+3))).isoformat(' ').split('.')[0])
    STATISTICS_EVENTS['item'].append(item)
    lang = request.headers.get("Accept-Language", "any").lower()
    STATISTICS_EVENTS['lang'].append(lang)
    try:
        ua = user_agent_parser.Parse(request.headers.get("User-Agent"))
        dev = ' '.join(ua['device'].values())
        if 'patch_minor' in ua['os'].keys():
            del ua['os']['patch_minor']
        os = ua['os']['family']
        full_os = ('.'.join(ua['os'].values()))
        dev = ua['user_agent']['family'] + ' ' + dev + ' ' + full_os
        STATISTICS_EVENTS['ua'].append(dev)
        STATISTICS_EVENTS['os'].append(os)
    except Exception:
        STATISTICS_EVENTS['ua'].append("")
        STATISTICS_EVENTS['os'].append("")
    ip = request.remote if not DEV else f"{random.randrange(255)}.13.130.40"
    STATISTICS_EVENTS['ipad'].append(ip)
    try:
        geo_info = 'Fakeland'
        STATISTICS_EVENTS['city'].append(geo_info.city.names['ru'])
        STATISTICS_EVENTS['cont'].append(geo_info.country.iso_code)
    except Exception:
        STATISTICS_EVENTS['city'].append('')
        STATISTICS_EVENTS['cont'].append('')
    with open(SAVE_FILE_ANALYTICS_PATH, "w") as f:
        json.dump(STATISTICS_EVENTS, f)


def get_rowed_stats():
    rowed = [i for i in zip(*STATISTICS_EVENTS.values())]
    t = tabulate(rowed, STATISTICS_EVENTS.keys(), tablefmt="html")
    t = ('<meta charset="utf-8">'
         '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">'
         + t.replace('<table>', '<table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">'))
    return t


async def index(request: web.Request):
    await request.release()
    who = request.cookies.get(RATER_COOKIE)
    if who is None:
        who = str(uuid4())
    asyncio.create_task(register_connection(who, request))
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


async def checkout(request: web.Request):
    who = request.cookies.get(RATER_COOKIE)
    if who is None:
        who = str(uuid4())
    body = await request.json()
    print(body)
    # await telegram_send(str(body))
    asyncio.create_task(register_connection(who, request, "checkout"))
    response = web.Response(body="ok", status=200)
    response.cookies[RATER_COOKIE] = who
    return response


async def error_middleware(_, handler):
    async def middleware_handler(request):
        try:
            response = await handler(request)
            return response
        except web.HTTPException as ex:
            raise ex
        except Exception:
            trb = str.join("", traceback.format_exception(*sys.exc_info()))
            asyncio.create_task(telegram_send("**ERROR:** \n```\n" + trb + "\n```"))
            return web.Response(text="Incident will be reported. Your data saved.")
    return middleware_handler


app = web.Application()
app.add_routes([
    web.static('/such_static/', "./web/"),
    web.get('/', index),
    web.post('/checkout', checkout),
    web.get('/preview/{path:.*}', preview),
    web.get('/shirt/{path:.*}', shirt),
])
app.on_startup.append(shed)
app.middlewares.append(error_middleware)
if DEV:
    web.run_app(app, host="0.0.0.0", port=8080)
else:
    web.run_app(app, host="0.0.0.0", port=80)
