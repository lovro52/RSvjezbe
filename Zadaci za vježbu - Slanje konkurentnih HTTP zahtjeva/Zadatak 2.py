import aiohttp
import asyncio

async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        fact = await response.json()
        return fact['fact']

async def filter_cat_facts(cat_facts):
    return [fact for fact in cat_facts if "cat" in fact.lower() or "cats" in fact.lower()]

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for _ in range(20)]
        cat_facts = await asyncio.gather(*tasks)

    filtered_facts = await filter_cat_facts(cat_facts)

    print("Filtrirane činjenice o mačkama:")
    for fact in filtered_facts:
        print(f"- {fact}")

asyncio.run(main())
