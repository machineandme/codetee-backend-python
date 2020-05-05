from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.static('/', "./web/")])
web.run_app(app, host="127.0.0.1")