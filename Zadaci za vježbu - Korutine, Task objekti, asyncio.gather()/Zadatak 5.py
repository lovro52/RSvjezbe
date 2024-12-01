import asyncio
import hashlib

async def secure_data(data):
    await asyncio.sleep(3)
    return {
        'prezime': data['prezime'],
        'broj_kartice': hashlib.sha256(data['broj_kartice'].encode()).hexdigest(),
        'CVV': hashlib.sha256(data['CVV'].encode()).hexdigest()
    }

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Ivić', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Kovačić', 'broj_kartice': '8765432187654321', 'CVV': '456'},
        {'prezime': 'Marić', 'broj_kartice': '1122334455667788', 'CVV': '789'}
    ]
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    print(rezultati)

asyncio.run(main())
