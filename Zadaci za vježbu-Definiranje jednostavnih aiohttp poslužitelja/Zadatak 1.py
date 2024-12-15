from aiohttp import web

async def get_proizvodi(request):
    proizvodi = [
        {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
        {"naziv": "Miš", "cijena": 100, "kolicina": 50},
        {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 30}
    ]
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)

web.run_app(app, port=8081)
