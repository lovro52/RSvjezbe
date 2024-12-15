import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8081/proizvodi')
        print(await response.json())
        
        response = await session.get('http://localhost:8081/proizvodi/2')
        print(await response.json())

        narudzba = {"proizvod_id": 2, "kolicina": 3}
        response = await session.post('http://localhost:8081/narudzbe', json=narudzba)
        print(await response.json())

asyncio.run(main())
