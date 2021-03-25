"""
Chika Offor
Cwiczenia 59.
Gra w "za duzo, za malo"
"""
import random

los = random.randint(1, 100)

print("Zgadnij numer calkowitych od 1-100")
while True:                                            #Komputer losuje liczba w przedzialu 1-100
    for i in range(5):
        zgadnij = int(input(f"Zgadnij jaki numer to jest: "))   #gracz na zgadnac jaki to liczba
        if zgadnij < los:
            print("Podales za mala liczbe")
        if zgadnij > los:
            print("Podales za duza liczbe")
        if zgadnij == los:
            print("Gratulacje!!")
            break
        if i == 4:
            print("Przegrales")


    print("Czy chcesz grac jeszcze raz?")
    odpowiedz = input("Wpisz 'N' jesli nie a 'T' jesli tak: ").upper()

    if odpowiedz == "T":
        continue
    elif odpowiedz == "N":
        break














