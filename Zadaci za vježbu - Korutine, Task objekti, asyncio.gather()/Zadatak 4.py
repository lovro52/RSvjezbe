import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    return f"Broj {broj} je {'paran' if broj % 2 == 0 else 'neparan'}."

async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]
    print(f"Nasumični brojevi: {brojevi}")
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]
    rezultati = await asyncio.gather(*zadaci)
    print("\n".join(rezultati))

asyncio.run(main())
