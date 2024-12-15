from aiohttp import web
proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]
narudzbe = []
async def post_narudzbe(request):
    data = await request.json()
    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")
    
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)
    if not proizvod:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    narudzba = {"proizvod_id": proizvod_id, "kolicina": kolicina}
    narudzbe.append(narudzba)
    return web.json_response(narudzbe, status=201)

app = web.Application()
app.router.add_post('/narudzbe', post_narudzbe)

web.run_app(app, port=8081)
