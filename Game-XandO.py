"""
Chika Offor
Cwiczenia 46_3.
Gra w kolko i krzyzyk
"""
def display(gra):
    """
    Game board display
    """
    for i in gra:
        for j in i:
            print(j, end=' ')
        print()

gra = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
zajeta_pola = []

def win():
    """
    Sprawdza czy sa wygrane pole
    """
    if gra[0][0] == gra[1][0] == gra[2][0] != '*':
        return True
    elif gra[0][0] == gra[0][1] == gra[0][2] != '*':
        return True
    elif gra[0][1] == gra[1][1] == gra[2][1] != '*':
        return True
    elif gra[0][2] == gra[1][2] == gra[2][2] != '*':
        return True
    elif gra[1][0] == gra[1][1] == gra[1][2] != '*':
        return True
    elif gra[2][0] == gra[2][1] == gra[2][2] != '*':
        return True
    elif gra[0][2] == gra[1][1] == gra[2][0] != '*':
        return True
    elif gra[0][0] == gra[1][1] == gra[2][2] != '*':
        return True

gracz = 'O'
while True:
    display(gra)
    wsp = input(f"Gracz '{gracz}' Podaj wspolrzednk: ") #input od uzytkownika sa wspolrzedne gry (rows and columns) np, 01, 22 ...
    x = int(wsp[0])
    y = int(wsp[1])
    gra[x][y] = gracz                                   #x jest numer row i y jest numer column

    if gracz == 'O':
        gracz = 'X'
    else:
        gracz = 'O'

    if wsp in zajeta_pola:
        print(" Pola zajeta")
        gra[x][y] = gracz
        #continue
    else:
        zajeta_pola.append(wsp)

    if win():
        print("Wygrales!!!")
        break

    if len(zajeta_pola) == 9:                          #jesli nie ma wygranych
         print("Nie ma wygranych!\nGame over!!!")
         break





















