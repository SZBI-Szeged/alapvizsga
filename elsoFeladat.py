from os import system
system("cls")

elsoMagassag = 0
masodikMagassag = 0

try:
    elsoMagassag = int(input("Kérek egy magasságot méterben: "))
    masodikMagassag = int(input("Kérek egy másik magasságot méterben: "))
except ValueError:
    print("Nem megfelelő bemeneti formátum!")

if masodikMagassag < elsoMagassag:
    x = elsoMagassag
    elsoMagassag = masodikMagassag
    masodikMagassag = x

van = True

for i in range(elsoMagassag, masodikMagassag + 1):
    if i % 2 == 0 and i % 7 == 0:
        print(i)
        van = False

if van:
    print("Nincs 2-vel és 7-tel is osztható szám a két bekért magasság között.")