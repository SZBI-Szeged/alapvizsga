from os import system
from masodikFeladat import legmagasabbPont
system("cls")

class FileBeolvas:
    def __init__(self, fileNev):
        self.FileNev = fileNev
        
    def feldolgoz(self):
        f = open(self.FileNev, "r", encoding="utf-8")
        self.ElsoSor = f.readline()
        self.Adatok = []
        for elem in f:
            adat = elem.split(';')
            self.Adatok.append(adat)
            
    def legmagasabbPontMeghatarozasa(self):
        self.Emelkedes = []
        self.Sullyedes = []
        
        for elem in self.Adatok:
            self.Emelkedes.append(int(elem[3]))
            self.Sullyedes.append(int(elem[4]))
        
        self.Magas = legmagasabbPont(self.Emelkedes, self.Sullyedes, int(self.ElsoSor))
        
    def pecseteloHelyekSzama(self):
        self.PecsetSzam = 0
        for elem in self.Adatok:
            if elem[5].strip() == "i":
                self.PecsetSzam += 1 

fb = FileBeolvas("kektura.csv")
fb.feldolgoz()

lista = fb.Adatok
allomasokSzama = lista
elsoKiir = f"A Kék Túra állomásainak száma: {len(allomasokSzama)}"
print(elsoKiir)

osszHossz = 0

for elem in lista:
    osszHossz += float(elem[2])

masodikKiir = f"A túra összes hossza: {osszHossz:.2f} km"
print(masodikKiir)

fb.legmagasabbPontMeghatarozasa()
legmagasabbPontErteke = fb.Magas

harmadikKiir = f"A legmagasabb pont értéke: {legmagasabbPontErteke} m"
print(harmadikKiir)

fb.pecseteloHelyekSzama()
pecsetSzam = fb.PecsetSzam
negyedikKiir = f"Pecsételő helyek száma: {pecsetSzam}"
print(negyedikKiir)