import aiohttp
import asyncio
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        responses = await asyncio.gather(*tasks)

    
    names = [user['name'] for user in responses[0]]
    emails = [user['email'] for user in responses[0]]
    usernames = [user['username'] for user in responses[0]]

    
    print("Imena korisnika:", names)
    print("Email adrese korisnika:", emails)
    print("Korisnička imena:", usernames)

    end = time.time()
    print(f"Vrijeme izvođenja: {end - start:.2f} sekundi.")

asyncio.run(main())
