from os import system
system("cls")

elsoMagassag = int(input("Kérek egy magasságot méterben: "))
masodikMagassag = int(input("Kérek egy másik magasságot méterben: "))

if masodikMagassag < elsoMagassag:
    x = elsoMagassag
    elsoMagassag = masodikMagassag
    masodikMagassag = x

van = True

for i in range(elsoMagassag, masodikMagassag + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
        van = False

if van:
    print("Nincs 2-vel és 3-mal is osztható szám a két bekért magasság között.")