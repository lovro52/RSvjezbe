import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    for record in baza_lozinka:
        if record['korisnicko_ime'] == korisnik and record['lozinka'] == lozinka:
            return f"Korisnik {korisnik}: Autorizacija uspješna."
    return f"Korisnik {korisnik}: Autorizacija neuspješna."

async def autentifikacija(korisnik, lozinka):
    await asyncio.sleep(3)
    for record in baza_korisnika:
        if record['korisnicko_ime'] == korisnik:
            return await autorizacija(korisnik, lozinka)
    return f"Korisnik {korisnik} nije pronađen."

async def main():
    rezultat = await autentifikacija("ana_anic", "super_teska_lozinka")
    print(rezultat)

asyncio.run(main())
