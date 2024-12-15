from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Miš", "cijena": 100, "kolicina": 50},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 30}
]

async def post_proizvodi(request):
    data = await request.json()
    proizvodi.append(data)
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_post('/proizvodi', post_proizvodi)

web.run_app(app, port=8081)
