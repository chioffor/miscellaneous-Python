import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

try:
    conn = pymysql.connect('localhost', 'root', '', '')
    c = conn.cursor()
    print("Polaczenia ok")
except:
    print("Blad polaczenia")

root = Tk()
root.title("KLUB SPORTOWY")

notebook = ttk.Notebook(root, padding=10)
notebook.pack(fill=BOTH, expand=True)

frameDodajKlub = ttk.Frame(notebook)
frameDodajZawodnik = ttk.Frame(notebook)
framePokazZawodnik = ttk.Frame(notebook)
frameUsunKlub = ttk.Frame(notebook)
frameUsunZawodnik = ttk.Frame(notebook)
framePrzypiszZawodnik = ttk.Frame(notebook)

frameDodajKlub.pack()
frameDodajZawodnik.pack()
framePokazZawodnik.pack()
frameUsunZawodnik.pack()
frameUsunKlub.pack()
framePrzypiszZawodnik.pack()

notebook.add(frameDodajKlub, text="Dodaj Klub")
notebook.add(frameDodajZawodnik, text="Dodaj Zawodnik do Klubu")
notebook.add(framePokazZawodnik, text="Pokaz Zawodnikow w Klubie")
notebook.add(frameUsunZawodnik, text="Usun Zawodnik")
notebook.add(frameUsunKlub, text="Usun Klub")
notebook.add(framePrzypiszZawodnik, text="Przypisz Zawodnik")


# class Dodaj Klub
class DodajKlub:

    def __init__(self):
        nazwaKlubu = dkNazwaEntry.get()
        miastoKlubu = dkMiastoEntry.get()

        if nazwaKlubu != '' and miastoKlubu != '':
            c.execute("INSERT INTO klub(nazwa, miasto) VALUES(%s, %s)", (nazwaKlubu, miastoKlubu))
            msgbox = messagebox.askyesno(message="Potwierdzasz dane?")
            if msgbox:
                conn.commit()
                messagebox.showinfo(message="Dodane!")
                dkNazwaEntry.delete(0, END)
                dkMiastoEntry.delete(0, END)
                dkNazwaEntry.focus()
            else:
                conn.rollback()
                messagebox.showinfo(message="Nie Wykonane!")


        else:
            messagebox.showinfo(message="Wszystkie Pole sa wazne!!!")


# class Dodaj Zawodnik
class DodajZawodnik:

    def __init__(self):

        dzKlubLabel.configure(text='')
        dzIdEntry.delete(0, END)
        dzIdEntry.configure(state='disabled')

        dzImieEntry.delete(0, END)
        dzImieEntry.configure(state='disabled')

        dzNazwiskoEntry.delete(0, END)
        dzNazwiskoEntry.configure(state='disabled')

        dz1submitButton.configure(state='disabled')

        dzListbox.delete(0, END)
        self.fraza = dzKlubEntry.get()
        c.execute(f"SELECT nazwa, miasto FROM klub WHERE nazwa LIKE '%{self.fraza}%'")
        self.dane = c.fetchall()
        for values in self.dane:
            dzListbox.insert(ACTIVE, f"{values[0]}, {values[1]}")

        if dzListbox.size():
            dz1submitButton.configure(state='normal')
            dz1submitButton.configure(command=self.aktywujForm)
        else:
            dz1submitButton.configure(state='disabled')

    def aktywujForm(self):
        if dzListbox.curselection():
            #klub_listbox.get(ACTIVE)
            dane = dzListbox.get(ACTIVE)
            dane = dane.split(',')
            self.nazwa = dane[0]

            dzKlubLabel.configure(text=self.nazwa)
            dzIdEntry.focus()

            dzIdEntry.configure(state='normal')
            dzImieEntry.configure(state='normal')
            dzNazwiskoEntry.configure(state='normal')
            dz2submitButton.configure(state='normal', command=self.dz2submit)
        else:
            messagebox.showinfo(message="Prosze wybrac klub")

    def dz2submit(self):
        c.execute("SELECT klub_id FROM klub WHERE nazwa = %s", self.nazwa)
        dane = c.fetchall()

        klub_id = dane[0]

        id = dzIdEntry.get()
        imie = dzImieEntry.get()
        nazwisko = dzNazwiskoEntry.get()

        if dzKlubLabel['text'] == '':
            messagebox.showinfo(message="Prosze wybrac klub")

        if id.isdigit() == False:
            messagebox.showinfo(message="Prosze podac tylko integer jako ID")



        if self.nazwa != '' and id != '' and id.isdigit() == True and imie != '' and nazwisko != '':
            c.execute("INSERT INTO zawodnik(zawodnik_id, imie, nazwisko, klub_id, nazwa_klub) VALUES(%s, %s, %s, %s, %s)",
                      (id, imie, nazwisko, klub_id, self.nazwa))
            msgbox = messagebox.askyesno(message="Czy potwierdzasz dane?")
            if msgbox:
                conn.commit()
                messagebox.showinfo(message=f"{imie} {nazwisko} zostal dodane do {self.nazwa}")

                dzIdEntry.delete(0, END)
                dzIdEntry.configure(state='disabled')

                dzImieEntry.delete(0, END)
                dzImieEntry.configure(state='disabled')

                dzNazwiskoEntry.delete(0, END)
                dzNazwiskoEntry.configure(state='disabled')

                dz2submitButton.configure(state='disabled')

                dzKlubLabel.configure(text='')

            else:
                conn.rollback()
                messagebox.showinfo(message='Nie Wykonane!')
                # entry_id.delete(0, END)
                # entry_imie.delete(0, END)
                # nazwisko_entry.delete(0, END)
                # klub_display.configure(text='')

        else:
            messagebox.showinfo(message="Pole sa wazne!")

# class Pokaz Zawodnik
class PokazZawodnik:

    def __init__(self):
        pzKlubListbox.delete(0, END)
        pzZawodListbox.delete(0, END)
        fraza = pzEntry.get()
        c.execute(f"SELECT nazwa, miasto FROM klub WHERE nazwa LIKE '%{fraza}%'")
        self.dane = c.fetchall()

        for values in self.dane:
            pzKlubListbox.insert(ACTIVE, f"{values[0]}, {values[1]}")

        if pzKlubListbox.size():
            pzPokazButton.configure(state='normal', command=self.pokazListZawod)

        else:
            pzPokazButton.configure(state='disabled')

    def pokazListZawod(self):
        pzZawodListbox.delete(0, END)
        index = pzKlubListbox.get(ACTIVE)
        pzLabel.configure(text=f"Zawodnicy w {index}")

        split_index = index.split(",")
        nazwa_klub = split_index[0]

        c.execute("SELECT imie, nazwisko FROM zawodnik WHERE nazwa_klub = %s", nazwa_klub)
        dane = c.fetchall()
        for i in dane:
            pzZawodListbox.insert(ACTIVE, f"{i[0].capitalize()} {i[1].capitalize()}")


# funkcji Usun Zawodnik
class UsunZawodnik:

    def __init__(self):
        uzListbox.delete(0, END)
        fraza = uzEntry.get()
        c.execute(f"SELECT zawodnik_id, imie, nazwisko FROM zawodnik "
                  f"WHERE zawodnik_id LIKE '%{fraza}%' "
                  f"OR nazwisko LIKE '%{fraza}%'")
        dane = c.fetchall()
        for data in dane:
            uzListbox.insert(ACTIVE, f"{data[0]} - {data[1]} {data[2]}")

        if uzListbox.size():
            uzUsunButton.configure(state='normal', command=self.usunZawodnik)
        else:
            uzUsunButton.configure(state='disabled')

    def usunZawodnik(self):
        index = uzListbox.get(ACTIVE)
        index_split = index.split(" ")
        index = index_split[0]
        c.execute("DELETE FROM zawodnik WHERE zawodnik_id = %s", index)
        msgbox = messagebox.askyesno(message = f"Czy potwierdzasz usunac {index_split[2].upper()} {index_split[3].upper()}")
        if msgbox:
            conn.commit()
            messagebox.showinfo(message="Wykonane!")
            uzListbox.delete(0, END)
            uzEntry.delete(0, END)

        else:
            conn.rollback()
            messagebox.showinfo(message="Nie Wykonane!")


# funkcji Usun Klub
class UsunKlub:

    def __init__(self):
        ukListbox.delete(0, END)
        fraza = ukEntry.get()
        c.execute(f"SELECT nazwa, miasto FROM klub"
                  f" WHERE nazwa LIKE '%{fraza}%'"
                  f" OR miasto LIKE '%{fraza}%'")
        dane = c.fetchall()

        for i in dane:
            ukListbox.insert(ACTIVE, f"{i[0]}, {i[1].capitalize()}")

        if ukListbox.size():
            ukUsunButton.configure(state='normal', command=self.usunKlub)

        else:
            ukUsunButton.configure(state='disabled')

    def usunKlub(self):
        index = ukListbox.curselection()
        if index:
            details = ukListbox.get(index)
            details_split = details.split(', ')
            nazwa = details_split[0]
            miasto = details_split[1]
            c.execute("SELECT klub_id FROM klub WHERE nazwa = %s AND miasto = %s", (nazwa, miasto))
            dane = c.fetchone()
            klub_id = dane[0]

            c.execute("DELETE FROM klub WHERE klub_id = %s", klub_id)
            msgbox = messagebox.askyesno(message=f"Czy potwierdzasz usunac {nazwa}, {miasto}?")
            if msgbox:
                conn.commit()
                messagebox.showinfo(message=f"{nazwa} Usuniety!!")
                ukListbox.delete(0, END)
                ukEntry.delete(0, END)
                ukUsunButton.configure(state='disabled')
            else:
                conn.rollback()
                messagebox.showinfo(message="Nie Wykonane!")

        else:
            messagebox.showinfo(message="Wybierz klub")


# class Przypisz Zawodnik

class PrzypiszZawodnik:

    def __init__(self):
        przypiszListbox2.delete(0, END)
        for child in przypiszFrame3.winfo_children():
            child.configure(state='disabled')
        przypiszListbox1.delete(0, END)
        przypiszLabel2.configure(text=f"{(' ')*25}")
        fraza = przypiszZawodEntry.get()
        c.execute(f"SELECT imie, nazwisko FROM zawodnik"
                  f" WHERE zawodnik_id LIKE '%{fraza}%'"
                  f" OR nazwisko LIKE '%{fraza}%'")
        dane = c.fetchall()
        for i in dane:
            self.imie = i[0]
            self.nazwisko = i[1]
            przypiszListbox1.insert(ACTIVE, f"{self.imie} {self.nazwisko}")

        przypiszListbox1.bind('<<ListboxSelect>>', self.select)


    def select(self, event):
        self.index = przypiszListbox1.curselection()
        if self.index:
            self.dane = przypiszListbox1.get(self.index)
            dane = self.dane.split()
            self.imie = dane[0]
            self.nazwisko = dane[1]

            c.execute("SELECT nazwa_klub FROM zawodnik WHERE imie = %s AND nazwisko = %s", (self.imie, self.nazwisko))
            nazwa_klub = c.fetchall()
            for i in nazwa_klub:
                self.nazwa_klub = i[0]
                przypiszLabel2.configure(text=f"{self.nazwa_klub} {(' ') * 10}")

            for child in przypiszFrame3.winfo_children():
                child.configure(state='normal')

            przypiszSzukajButton2.configure(command=self.szukajKlub)


        else:
            messagebox.showinfo(message="Wybierz zawodnik i przycisk 'ok'")




    def szukajKlub(self):
        przypiszListbox2.delete(0, END)
        #listbox_przypiszSzukaj.configure(state='disabled')
        fraza = przypiszKlubEntry.get()
        c.execute(f"SELECT nazwa, miasto FROM klub "
                  f"WHERE nazwa LIKE '%{fraza}%' "
                  f"OR miasto LIKE '%{fraza}%'")
        dane = c.fetchall()

        for i in dane:
            przypiszListbox2.insert(ACTIVE, f"{i[0]}, {i[1]}")

        if przypiszListbox2.size():
            przypiszZmienButton.configure(state='normal', command=self.zmienKlub)

        else:
            przypiszZmienButton.configure(state='disabled')




    def zmienKlub(self):
        if przypiszListbox2.curselection():
            dane = przypiszListbox2.get(ACTIVE)
            dane = dane.split(',')
            nowy_klub = dane[0]

            c.execute("SELECT klub_id FROM klub WHERE nazwa = %s", nowy_klub)
            value = c.fetchone()
            klub_id = value[0]

            c.execute("UPDATE zawodnik SET nazwa_klub = %s, klub_id = %s WHERE imie = %s", (nowy_klub, klub_id, self.imie))

            msgbox = messagebox.askyesno(message=f"Czy potwierdzasz zmian?\n"
                                        f"{self.imie} {self.nazwisko} z "
                                        f"{self.nazwa_klub} do\n {nowy_klub}")
            if msgbox:
                conn.commit()
                messagebox.showinfo(message=f"{self.imie} {self.nazwisko} zostal przypisany do {nowy_klub}")
                przypiszListbox2.delete(0, END)
                przypiszKlubEntry.delete(0, END)
                przypiszLabel2.configure(text=f"{(' ') * 25}")

                for child in przypiszFrame3.winfo_children():
                    child.configure(state='disabled')
            else:
                conn.rollback()
                messagebox.showinfo(message="Nie Wykonane!")




        else:
            messagebox.showinfo(message="Wybierz Klub")



# TABS

# Dodaj Klub "dk"

dkText = "Prosze podac nastepujace informacje:"
ttk.Label(frameDodajKlub, text=dkText, font=("arial", 9, "bold")).grid(row=0, column=0, columnspan=2, pady=10, padx=10)

ttk.Label(frameDodajKlub, text="Nazwa:").grid(row=1, column=0)
dkNazwaEntry = ttk.Entry(frameDodajKlub)
dkNazwaEntry.grid(row=1, column=1, sticky=W, pady=5)

ttk.Label(frameDodajKlub, text="Miasto:").grid(row=2, column=0)
dkMiastoEntry = ttk.Entry(frameDodajKlub)
dkMiastoEntry.grid(row=2, column=1, sticky=W)

dkSubmitButton = ttk.Button(frameDodajKlub, text="Submit", command=DodajKlub)
dkSubmitButton.grid(row=3, column=0, columnspan=2, pady=5)


# Dodaj Zawodnik 'dz'

dzFrame1 = ttk.Frame(frameDodajZawodnik)
dzFrame2 = ttk.Frame(frameDodajZawodnik)

dzFrame1.grid(row=0, column=0)
dzFrame2.grid(row=0, column=1)


# Dodaj Zawodnik frame1
dzText1 = "Wpisz fraza lub nazwa klub"
ttk.Label(dzFrame1, text=dzText1, font=("arial", 9, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

dzKlubEntry = ttk.Entry(dzFrame1)
dzKlubEntry.grid(row=1, column=0)
ttk.Button(dzFrame1, text="Pokaz", command=DodajZawodnik).grid(row=1, column=1)

dzListbox = Listbox(dzFrame1)
dzListbox.grid(row=2, column=0)

dz1submitButton = ttk.Button(dzFrame1, text="Submit", state='disabled')
dz1submitButton.grid(row=3, column=0, columnspan=2)


# Dodaj Zawodnik frame2
dzText2 = "Prosze podac nastepujace informacje:"
ttk.Label(dzFrame2, text=dzText2, font=("arial", 9, "bold")).grid(row=0, column=0, columnspan=2, pady=5, padx=5)

ttk.Label(dzFrame2, text="Klub:").grid(row=1, column=0, pady=3)
dzKlubLabel = ttk.Label(dzFrame2, text='')
dzKlubLabel.grid(row=1, column=1, pady=3)


ttk.Label(dzFrame2, text="ID:").grid(row=2, column=0, pady=3)
dzIdEntry = ttk.Entry(dzFrame2, state='disabled')
dzIdEntry.grid(row=2, column=1)

ttk.Label(dzFrame2, text="Imie:").grid(row=3, column=0, pady=3)
dzImieEntry = ttk.Entry(dzFrame2, state='disabled')
dzImieEntry.grid(row=3, column=1, pady=3)

ttk.Label(dzFrame2, text="Nazwisko:").grid(row=4, column=0, pady=3)
dzNazwiskoEntry = ttk.Entry(dzFrame2, state='disabled')
dzNazwiskoEntry.grid(row=4, column=1, pady=3)

dz2submitButton = ttk.Button(dzFrame2, text="Submit", state='disabled')
dz2submitButton.grid(row=5, column=0, columnspan=2, pady=5)


# Pokaz Zawodnik w Klubie 'pz'

pzText = "Wybierz klub zeby wyswietlac zawodnikow w klubie"
ttk.Label(framePokazZawodnik, text=pzText, font=("arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

pzText2 = "Prosze podac fraze lub nazwe klubu i szukaj:"
ttk.Label(framePokazZawodnik, text=pzText2, font=("arial", 10, 'bold')).grid(row=1, column=0, columnspan=2, pady=5)
pzEntry = ttk.Entry(framePokazZawodnik)
pzEntry.grid(row=2, column=0)
pzButton = ttk.Button(framePokazZawodnik, text="Szukaj", command=PokazZawodnik)
pzButton.grid(row=2, column=1)

ttk.Label(framePokazZawodnik, text="Wybierz klub.").grid(row=3, column=0)
pzKlubListbox = Listbox(framePokazZawodnik)
pzKlubListbox.grid(row=4, column=0)

pzPokazButton = ttk.Button(framePokazZawodnik, text="Pokaz", state='disabled')
pzPokazButton.grid(row=5, column=0)

pzLabel = ttk.Label(framePokazZawodnik, text="")
pzLabel.grid(row=3, column=1, columnspan=2)
pzZawodListbox = Listbox(framePokazZawodnik)
pzZawodListbox.grid(row=4, column=1)


# Usun Zawodnik frame 'uz'

uzText1 = "Szukaj zawodnik przez ID albo Nazwisko"
ttk.Label(frameUsunZawodnik, text=uzText1, font=("arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=10, padx=5)

uzText2 = "Podaj fraza Nazwisko lub ID zawodnika i szukaj:"
ttk.Label(frameUsunZawodnik, text=uzText2, font=("arial", 8, "bold")).grid(row=1, column=0, columnspan=2)

uzEntry = ttk.Entry(frameUsunZawodnik)
uzEntry.grid(row=2, column=0, sticky=W)

uzSzukajButton = ttk.Button(frameUsunZawodnik, text="Szukaj", command=UsunZawodnik)
uzSzukajButton.grid(row=2, column=1, sticky=W)

uzListbox = Listbox(frameUsunZawodnik)
uzListbox.grid(row=3, column=0, pady=10)

uzUsunButton = ttk.Button(frameUsunZawodnik, text="Usun", state='disabled')
uzUsunButton.grid(row=4, column=0)


# Usun Klub frame 'uk'

ukText = "Podaj fraza nazwa albo miasto klubu i szukaj"
ttk.Label(frameUsunKlub, text=ukText, font=("arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=10, padx=5)

ukEntry = ttk.Entry(frameUsunKlub)
ukEntry.grid(row=1, column=0)

ukSzukajButton = ttk.Button(frameUsunKlub, text="Szukaj", command=UsunKlub)
ukSzukajButton.grid(row=1, column=1)

ttk.Label(frameUsunKlub, text="Lista Klubow:").grid(row=2, column=0, pady=7)
ukListbox = Listbox(frameUsunKlub)
ukListbox.grid(row=3, column=0, pady=6)

ukUsunButton = ttk.Button(frameUsunKlub, text="Usun", state='disabled')
ukUsunButton.grid(row=4, column=0, pady=5)


# Przypisz Zawodnik Frame 'przypisz'

przypiszFrame1 = ttk.Frame(framePrzypiszZawodnik)
przypiszFrame2 = ttk.Frame(framePrzypiszZawodnik)
przypiszFrame3 = ttk.Frame(framePrzypiszZawodnik)

przypiszFrame1.grid(row=0, column=0)
przypiszFrame2.grid(row=0, column=1)
przypiszFrame3.grid(row=0, column=2)

# frame 1
przypiszFrame1_text = "Szukaj zawodnik przez ID albo Nazwisko"
ttk.Label(przypiszFrame1, text=przypiszFrame1_text).grid(row=0, column=0, columnspan=2, pady=10, padx=5)
przypiszZawodEntry = ttk.Entry(przypiszFrame1)
przypiszZawodEntry.grid(row=1, column=0)

przypiszSzukajButton1 = ttk.Button(przypiszFrame1, text="Szukaj", command=PrzypiszZawodnik)
przypiszSzukajButton1.grid(row=1, column=1)

ttk.Label(przypiszFrame1, text="Zawodnicy:").grid(row=2, column=0, pady=10)
przypiszListbox1 = Listbox(przypiszFrame1, exportselection=False)
przypiszListbox1.grid(row=3, column=0)

# frame 2
ttk.Label(przypiszFrame2, text='Klub:').grid(row=0, column=0)
przypiszLabel2 = ttk.Label(przypiszFrame2, text=f"{(' ')*25}")
przypiszLabel2.grid(row=0, column=1)

# frame 3
przypiszLabel3 = ttk.Label(przypiszFrame3, text="Napisz fraza nazwa lub miasto klubu")
przypiszLabel3.grid(row=0, column=0, columnspan=2, pady=10, padx=5)

przypiszKlubEntry = ttk.Entry(przypiszFrame3)
przypiszKlubEntry.grid(row=1, column=0)

przypiszSzukajButton2 = ttk.Button(przypiszFrame3, text="Szukaj")
przypiszSzukajButton2.grid(row=1, column=1)

ttk.Label(przypiszFrame3, text="Kluby:").grid(row=2, column=0, pady=10)
przypiszListbox2 = Listbox(przypiszFrame3)
przypiszListbox2.grid(row=3, column=0)

przypiszZmienButton = ttk.Button(przypiszFrame3, text="Zmien")
przypiszZmienButton.grid(row=4, column=0)

for child in przypiszFrame3.winfo_children():
    child.configure(state='disabled')




root.mainloop()