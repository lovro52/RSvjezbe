# shop/proizvodi.py

class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} EUR, Količina: {self.kolicina}")

proizvodi = []

def dodaj_proizvod(naziv, cijena, kolicina):
    proizvodi.append(Proizvod(naziv, cijena, kolicina))
