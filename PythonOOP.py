class Pacjenci:

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__lista_chorob = []

    def getImie(self):
        return self.__imie.capitalize()

    def getNazwisko(self):
        return self.__nazwisko.capitalize()

    def getListaChorob(self):
        return self.__lista_chorob

    def __str__(self):
        return f"Imie: {self.getImie()} | Nazwisko: {self.getNazwisko()}"

class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentach = []

    def __str__(self):
        return f"Przychodnia: {self.nazwa.capitalize()} | Miasto: {self.miasto.capitalize()}"

class PrzychodniaKontroler:

    def __init__(self):
        self.listaPrzychodni = []

    def dodajPrzychodnia(self, nazwa, miasto):
        if nazwa != '' and miasto != '':
            przychod = Przychodnia(nazwa, miasto)
            self.listaPrzychodni.append(przychod)
            print("\nPrzychodnia zostala zapisana\n")

        else:
            print("\nPole wazne, Przychodnia nie zostala zapisana\n")


    def pokazPrzychodni(self):
        print(f"\n{'-'*20}Lista Przychodni{'-'*20}")
        for przychodnia in self.listaPrzychodni:
            print(przychodnia)
        print()

    def pokazPacjentow(self, nazwa):
        znaleziono = False
        for przychodnia in self.listaPrzychodni:
            if przychodnia.nazwa == nazwa:
                znaleziono = True
                print(f"\n{'-'*20}Lista Pacjentow w Przychodni {przychodnia.nazwa.capitalize()}{'-'*20}")
                for pacjent in przychodnia.listaPacjentach:
                    print(pacjent)
                print()

        if znaleziono == False:
            print("\nNie rozpoznana nazwa Przychodni!\n")

    def pokazChorobe(self, nazwisko):
        znaleziono = False
        for przychodnia in self.listaPrzychodni:
            for pacjent in przychodnia.listaPacjentach:
                if pacjent.getNazwisko() == nazwisko:
                    print(f"\n{'-'*20}Lista Chorob Pacjenta {pacjent.getNazwisko()}{'-'*20}")
                    for choroba in pacjent.getListaChorob():
                        print(choroba)
                    print()
                    znaleziono = True
                    break
        if znaleziono == False:
            print("\nNie rozpoznan nazwisko pacjenta!\n")

class App(PrzychodniaKontroler):
    def __init__(self):
        super().__init__()

    def menu(self):
        while True:
            print(f"{'-'*20}MENU{'-'*20}")
            menu = input("1 - Przychodnia, 2 - Pacjent, 3 - Koniec: ")
            if menu == "1":
                print(f"\n{'-'*20}Przychodni{'-'*20}")
                przychodnia = input("1 - Dodaj przychodnie, 2 - Dodaj pacjenta, 3 - Lista przychodni, 4 - Lista pacjentow w przychodni, 5 - Menu: ")

                if przychodnia == "1":
                    nazwa = input("Podaj nazwa przychodni: ")
                    miasto = input("Podaj miasto przychodni: ")
                    self.dodajPrzychodnia(nazwa, miasto)

                elif przychodnia == "2":
                    nazwa = input("Podaj nazwa przychodnia: ")
                    znaleziono = False
                    for przychodnia in self.listaPrzychodni:
                        if przychodnia.nazwa == nazwa:
                            imie = input("Podaj imie pacjenta: ")
                            nazwisko = input("Podaj nazwisko pacjenta: ")
                            znaleziono = True
                            if imie != '' and nazwisko != '':
                                pacjent = Pacjenci(imie, nazwisko)
                                przychodnia.listaPacjentach.append(pacjent)
                                print("\nPacjent zostal dodany\n")
                            else:
                                print("\nPole wazne! Pacjent nie zostal dodany.\n")


                    if znaleziono == False:
                        print("\nNie rozpoznana nazwa przychodni\n")

                elif przychodnia == "3":
                    self.pokazPrzychodni()

                elif przychodnia == "4":
                    nazwa = input("Podaj nazwa przychodni: ")
                    self.pokazPacjentow(nazwa)

                elif przychodnia == "5":
                    continue

                else:
                    print("\nNie rozpoznana opcja menu\n")

            elif menu == "2":
                print(f"\n{'-'*20}Pacjent{'-'*20}")
                pacjent = input("1 - Dodaj chorobe, 2 - Lista chorob pacjenta, 3 - Menu: ")

                if pacjent == "1":
                    nazwisko = input("Podaj nazwisko pacjenta: ").capitalize()
                    znaleziono = False
                    for przychodnia in self.listaPrzychodni:
                        for pacjent in przychodnia.listaPacjentach:
                            if pacjent.getNazwisko() == nazwisko:
                                chorobe = input("Podaj chorobe: ")
                                pacjent.getListaChorob().append(chorobe)
                                print("\nChoroba zapisana\n")
                                znaleziono = True
                                break

                    if znaleziono == False:
                        print("\nNie rozpoznana nazwisko Pacjenta!\n")

                elif pacjent == "2":
                    nazwisko = input("Podaj nazwisko pacjenta: ").capitalize()
                    self.pokazChorobe(nazwisko)

                elif pacjent == "3":
                    continue

                else:
                    print("\nNie rozpoznana opcja menu\n")

            elif menu == "3":
                print("\nKoniec Programu!!!\n")
                break

            else:
                print("\nNie rozpoznana opcja menu\n")

x = App()
x.menu()


