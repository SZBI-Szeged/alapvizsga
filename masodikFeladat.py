from os import system
from random import randrange
system("cls")

def feltolt():
	lista = []
	for i in range(20):
		veletlen = randrange(0, 201)
		lista.append(veletlen)
	return lista

emelkedesek = feltolt()
sullyedesek = feltolt()

print(emelkedesek)
print(sullyedesek)

def legmagasabbPont(elsoLista, masodikLista, kezdoMagassag):
	global index
	magassag = kezdoMagassag
	index = -1

	for i in range(len(elsoLista)):
		kulonbseg = elsoLista[i] - masodikLista[i]
		kezdoMagassag += kulonbseg
		if magassag <= kezdoMagassag:
			magassag = kezdoMagassag
			index = i

	return magassag

legmagasabbPontErteke = legmagasabbPont(emelkedesek, sullyedesek, 100)

kiir = f"A legmagasabb ponthoz tartozó szakasz sorszáma: {index + 1}, és értéke: {legmagasabbPontErteke} méter."
print(kiir)