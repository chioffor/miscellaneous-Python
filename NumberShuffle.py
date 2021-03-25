"""
Chika Offor
Cwiczenie 59_2.
Program losuje liczby od 1-10 i pyta uzytkownik jaki jest wynik mnozenia
"""

import random

poprawne_odpowiedzi = []
while True:
    los1 = random.randint(1, 10)
    los2 = random.randint(1, 10)
    poprawna = los1 * los2
    odpowiedz_uzytkownika = int(input(f"Ile to jest: {los1} * {los2}? -> "))
    if odpowiedz_uzytkownika == poprawna:
        print("Poprawna")
        poprawne_odpowiedzi.append(odpowiedz_uzytkownika)
    while odpowiedz_uzytkownika != poprawna:
        print("Nie poprawna")
        odpowiedz_uzytkownika = int(input(f"Ile to jest: {los1} * {los2}? -> "))
        if odpowiedz_uzytkownika == poprawna:
            print("Poprawna")
            poprawne_odpowiedzi.append(odpowiedz_uzytkownika)
    if len(poprawne_odpowiedzi) == 5:
        break















