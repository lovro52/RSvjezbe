import aiohttp
import asyncio

async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()
        return data['data'][0]['attributes']['body']

async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        fact = await response.json()
        return fact['fact']

async def mix_facts(dog_facts, cat_facts):
    return [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]

async def main():
    async with aiohttp.ClientSession() as session:
        dog_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_tasks = [get_cat_fact(session) for _ in range(5)]
        dog_cat_facts = await asyncio.gather(*dog_tasks, *cat_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]
    mixed_facts = await mix_facts(dog_facts, cat_facts)

    print("Mixane činjenice o psima i mačkama:")
    for fact in mixed_facts:
        print(f"- {fact}")

asyncio.run(main())
