class Trenerow:

    def __init__(self, imie, nazwisko, specjalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.specjalizacja = specjalizacja


    def __str__(self):
        return f"Imie: {self.imie.capitalize()} | Nazwisko: {self.nazwisko.capitalize()} | Specjalizacja: {self.specjalizacja.capitalize()}"

class Uczestnicy:

    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Imie: {self.imie.capitalize()} | Nazwisko: {self.nazwisko.capitalize()} | Telefon: {self.telefon} | Email: {self.email}"

class Kurs:

    def __init__(self, nazwa, miasto, termin):
        self.nazwa = nazwa
        self.miasto = miasto
        self.termin = termin
        self.listaUczestnikow = []
        self.trener = ''

    def __str__(self):
        return f"Kurs: {self.nazwa.capitalize()} | Miasto: {self.miasto.capitalize()} | Termin: {self.termin} | Trener: [{self.trener}]"


class KursKontroler:
    def __init__(self):
        self.listaKursow = []
        self.listaTrenerow = []

    def pokazKursow(self):
        if bool(self.listaKursow) == False:
            print("\nNie ma Kursu na liscie\n")
        else:
            print(f"\n{'-' * 20}Lista Kursy{'-' * 20}")
            for kurs in self.listaKursow:
                print(kurs)
        print()

    def pokazTrenerow(self):
        if bool(self.listaTrenerow) == False:
            print("\nNie ma Trenerow na liscie")
        else:
            print(f"\n{'-'*20}Lista Trenerzy{'-'*20}")
            for trener in self.listaTrenerow:
                print(trener)
        print()

    def pokazListaUczestnikow(self, nazwaKursu):
        znaleziono = False
        for kurs in self.listaKursow:
            if kurs.nazwa == nazwaKursu:
                print(f"\n{'-' * 20}Lista Uczestnicy {kurs.nazwa.capitalize()}{'-' * 20}")
                for uczestnik in kurs.listaUczestnikow:
                    print(uczestnik)
                znaleziono = True
                print()

        if znaleziono == False:
            print("\nNie rozpoznana nazwa kursu\n")




class KursApp(KursKontroler):

    def __init__(self):
        super().__init__()

    def menu(self):
        while True:
            """
            MENU
            1 - KURS
                1 - dodaj kurs
                2 - lista kurs
                3 - menu
            2 - UCZESTNIK
                1 - dodaj uczestnik do kursu
                2 - lista uczestnik w kursie
            3 - TRENER
                1 - dodaj trenera
                2 - lista trenera
                3 - przypisz trener do kursu
                
            4 - KONIEC
            """
            opcji = "1 - KURSY, " \
                    "2 - UCZESTNICY, " \
                    "3 - TRENERZY, " \
                    "4 - KONIEC" \

            print(f"{'-'*20}MENU{'-'*20}")
            menu = input(f"{opcji}: ")

            if menu == '1':

                opcja = input(f"\n{'-'*20}KURSY{'-'*20}\n1 - Dodaj kurs, 2 - Lista kurs 3 - Menu: ")

                if opcja == '1':
                    print("\nPodaj Nazwa, Miasto i Termin kursu")
                    nazwa = input("Nazwa kursu: ")
                    miasto = input("Miasto kursu: ")
                    termin = input("Termin kursu: ")

                    if nazwa != '' and miasto != '' and termin != '':
                        kurs = Kurs(nazwa, miasto, termin)
                        self.listaKursow.append(kurs)
                        print("\nKurs zostal zapisane\n")
                    else:
                        print("\nPole wazne!!!\nKurs nie byl zapisane\n")

                elif opcja == '2':
                    self.pokazKursow()

                elif opcja == '3':
                    continue
                else:
                    print("\nNie rozpoznana opcja\n")

            elif menu == '2':

                opcja = input(f"\n{'-'*20}UCZESTNICY{'-'*20}\n1 - Dodaj uczestnik do kursu, 2 - Lista uczestnik w kursie, 3 - Menu: ")

                if opcja == '1':
                    nazwa = input("Podaj nazwa kursu: ")
                    znaleziono = False
                    for kurs in self.listaKursow:
                        if nazwa in kurs.nazwa:
                            print("Podaj Imie, Nazwisko, Telefon i Email Uczestnika")
                            imie = input("Imie: ")
                            nazwisko = input("Nazwisko: ")
                            telefon = input("Telefon: ")
                            email = input("Email: ")
                            if imie != '' and nazwisko != '' and telefon != '' and email != '':
                                uczestnik = Uczestnicy(imie, nazwisko, telefon, email)
                                kurs.listaUczestnikow.append(uczestnik)
                                print(f"\nUczestnik zostal zapisane do Kurs {kurs.nazwa.capitalize()}\n")

                            else:
                                print("\nPole Wazne!!\nUczestnik nie zostal zapisane\n")
                            znaleziono = True
                            break

                    if znaleziono == False:
                        print("\nNie rozpoznana nazwa kursu!!\n")

                elif opcja == '2':
                    nazwaKursu = input("Podaj nazwa kurs: ")
                    self.pokazListaUczestnikow(nazwaKursu)

                elif opcja == '3':
                    continue

            elif menu == '3':
                opcja = input(f"\n{'-'*20}TRENERZY{'-'*20}\n1 - Dodaj Trenera, 2 - Lista trenerow, 3 - Przypisz trener do kursu, 4 - Menu: ")
                if opcja == '1':
                    print("Podaj Imie, Nazwisko i Specjalizacja Trenera")
                    imie = input("Imie: ")
                    nazwisko = input("Nazwisko: ")
                    specjalizacja = input("Specjalizacja: ")
                    if imie != '' and nazwisko != '' and specjalizacja != '':
                        trener = Trenerow(imie, nazwisko, specjalizacja)
                        self.listaTrenerow.append(trener)
                        print("\nTrener zostal zapisany\n")
                    else:

                        print("\nPole wazne\nTrener nie zostal zapisany\n")

                elif opcja == '2':
                    self.pokazTrenerow()

                elif opcja == '3':
                    print("\nPodaj nazwa kursu do ktorej chcesz zapisac trenera")
                    nazwaKursu = input("Nazwa kursu: ")
                    znaleziono1 = False
                    znaleziono2 = False
                    for kurs in self.listaKursow:
                        if nazwaKursu in kurs.nazwa:
                            nazwiskoTrenera = input("Podaj nazwisko trenera: ")
                            znaleziono1 = True
                            for trener in self.listaTrenerow:
                                if nazwiskoTrenera == trener.nazwisko:
                                    kurs.trener = trener
                                    print(f"\nTrener {trener.nazwisko.capitalize()} zostal zapisany do Kurs {kurs.nazwa.capitalize()}\n")
                                    znaleziono2 = True
                                    break

                    if znaleziono1 == False:
                        print("\nNie rozpoznana nazwa kursu!!\n")
                    elif znaleziono2 == False:
                        print("\nNie rozpoznane nazwisko trenera\n")

                elif opcja == '4':
                    continue

            elif menu == '4':
                print(f"\n{'-'*20}KONIEC PROGRAMU!!!{'-'*20}\n")
                break

            else:
                print("\nNie rozpoznana opcja menu\n")

KursApp().menu()






