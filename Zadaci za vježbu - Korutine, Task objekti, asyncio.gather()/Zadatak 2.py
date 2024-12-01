import asyncio

async def fetch_users():
    print("Dohvaćam korisnike...")
    await asyncio.sleep(3)
    return [{"id": 1, "ime": "Ana"}, {"id": 2, "ime": "Ivan"}]

async def fetch_products():
    print("Dohvaćam proizvode...")
    await asyncio.sleep(5)
    return [{"id": 101, "naziv": "Laptop"}, {"id": 102, "naziv": "Telefon"}]

async def main():
    users, products = await asyncio.gather(fetch_users(), fetch_products())
    print(f"Korisnici: {users}")
    print(f"Proizvodi: {products}")

asyncio.run(main())
