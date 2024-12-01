import asyncio

async def fetch_data():
    print("Dohvaćam podatke...")
    await asyncio.sleep(3)
    data = [x for x in range(1, 11)]  
    print("Podaci dohvaćeni.")
    return data

async def main():
    result = await fetch_data()
    print(f"Dohvaćeni podaci: {result}")

asyncio.run(main())
