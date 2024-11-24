# shop/narudzbe.py

class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_opis = ", ".join([f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_opis}, Ukupna cijena: {self.ukupna_cijena} EUR")

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list) or not lista_proizvoda:
        raise ValueError("Argument mora biti ne-prazna lista.")
    
    for p in lista_proizvoda:
        if not isinstance(p, dict) or not {"naziv", "cijena", "kolicina"}.issubset(p):
            raise ValueError("Svaki element liste mora biti rječnik s ključevima 'naziv', 'cijena' i 'kolicina'.")
        if p["kolicina"] <= 0:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    ukupna_cijena = sum(p["cijena"] * p["kolicina"] for p in lista_proizvoda)
    return Narudzba(lista_proizvoda, ukupna_cijena)
