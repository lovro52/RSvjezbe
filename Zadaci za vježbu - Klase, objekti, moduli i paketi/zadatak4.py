#1
import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, "
              f"Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        print(f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina.")

auto = Automobil("Toyota", "Corolla", 2015, 120000)
auto.ispis()
auto.starost()

#2
import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b if self.b != 0 else "Dijeljenje s nulom nije moguće!"

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return math.sqrt(self.a)

kalkulator = Kalkulator(9, 3)
print(kalkulator.zbroj())
print(kalkulator.oduzimanje())
print(kalkulator.mnozenje())
print(kalkulator.dijeljenje())
print(kalkulator.potenciranje())
print(kalkulator.korijen())

#3
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(**student) for student in studenti]
najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())

print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime} "
      f"s prosjekom {najbolji_student.prosjek()}.")

#4
import math

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r ** 2

krug = Krug(10)
print(f"Opseg kruga: {krug.opseg()}")
print(f"Površina kruga: {krug.povrsina()}")
