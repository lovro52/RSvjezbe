# main.py

from shop.proizvodi import dodaj_proizvod, proizvodi
from shop.narudzbe import napravi_narudzbu

# Dodavanje proizvoda
dodaj_proizvod("Laptop", 5000, 10)
dodaj_proizvod("Monitor", 1000, 20)

# Ispis svih proizvoda
print("Popis proizvoda:")
for proizvod in proizvodi:
    proizvod.ispis()

# Kreiranje narudžbe
proizvodi_za_narudzbu = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1},
]

narudzba = napravi_narudzbu(proizvodi_za_narudzbu)
if narudzba:
    narudzba.ispis_narudzbe()
