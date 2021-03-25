"""
Chika Offor
Cwiczenia 59_1
Program losuje liczby od 1-10 wraz z dzialaniem (dodawanie, odejmowanie i mnozenie)
i pyta uzytkownik jaki jest wynik
"""

import random

poprawne_odpowiedzi = []
zle_odpowiedzi = []

x = 1
while x < 11:
    los1 = random.randint(1, 10)
    los2 = random.randint(1, 10)
    znaki = ["+", "-", "*"]
    los_znaki = random.randint(0, 2)
    poprawna1 = los1 + los2
    poprawna2 = los1 - los2
    poprawna3 = los1 * los2
    odpowiedzi_uzytkownika = int(input(f"Ile to jest : {los1} {znaki[los_znaki]} {los2}? -> "))
    x +=1
    if poprawna1 == odpowiedzi_uzytkownika or poprawna2 == odpowiedzi_uzytkownika or poprawna3 == odpowiedzi_uzytkownika:
        poprawne_odpowiedzi.append(odpowiedzi_uzytkownika)
    else:
        zle_odpowiedzi.append(odpowiedzi_uzytkownika)

print(f"Miale(a)s {len(poprawne_odpowiedzi)} poprawne odpowiedzi i {len(zle_odpowiedzi)} zle odpowiedzi")




