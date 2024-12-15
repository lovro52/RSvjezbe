from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod(request):
    proizvod_id = int(request.match_info.get('id', 0))
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)
    if proizvod:
        return web.json_response(proizvod)
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod)

web.run_app(app, port=8081)
