import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import json

okno = tk.Tk()


def on_closing():
    """Zamyka okno i wychodzi z programu po kliknięciu przycisku zamknięcia."""
    if messagebox.askyesno("Wyjscie", "Na pewno chcesz wyjsc z programu?"):
        okno.destroy()


okno.resizable(False, False)

wysokosc_okna = 685
szerokosc_okna = 550

szerokosc_ekranu = okno.winfo_screenwidth()
wysokosc_ekranu = okno.winfo_screenheight()

polozenie_w_poziomie = int((szerokosc_ekranu / 2) - (szerokosc_okna / 2))
polozenie_w_pionie = int((wysokosc_ekranu / 2) - (wysokosc_okna / 2))

okno.geometry(
    "{}x{}+{}+{}".format(szerokosc_okna, wysokosc_okna, polozenie_w_poziomie,
                         polozenie_w_pionie))


class Labirynt(tk.Frame):
    """Generuje labirynt i wyświetla go w oknie interfejsu użytkownika za
    pomocą biblioteki Tkinter. """

    def __init__(self):
        """Inicjalizuje okno interfejsu użytkownika."""
        super().__init__()

        self.initUI()

    def initUI(self):
        """Ustawia tytuł okna i układ płótna dla labiryntu. Inicjuje akcje
        zwiazane z labiryntem. """
        self.master.title("Generowanie labiryntu")
        self.pack(fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(self)
        lewa_gora = 5, 5
        prawa_gora = 545, 5
        prawy_dol = 545, 545
        lewy_dol = 5, 545

        def ramka():
            """Rysuje ramkę, zewnętrzne ściany labiryntu."""
            canvas.create_line(lewa_gora, prawa_gora)
            canvas.create_line(prawa_gora, prawy_dol)
            canvas.create_line(prawy_dol, lewy_dol)
            canvas.create_line(lewy_dol, lewa_gora)

        ramka()

        # plansza(list): lista wszystkich komórek, które znajdują się na
        # planszy (szkielecie) labiryntu
        plansza = []
        # odwiedzone(list): lista komórek, które zostały odwiedzone.
        odwiedzone = []
        # stos(list): stosuje się do śledzenia ścieżki podczas przeszukiwania.
        stos = []
        # slownik_przejsc(dict): slownik, ktory jako klucz przyjmuje
        # nastepna komorke do ktorej sie przemieszcza, a jako wartosc
        # komorke w ktorej aktualnie sie znajduje
        slownik_przejsc = {}

        def zbuduj_szkielet_labiryntu(rozmiar):
            """Buduje szkielet labiryntu tworząc poziome i pionowe linie na
            płótnie.

            Parametry:
            rozmiar (int): rozmiar labiryntu, gdzie labirynt
            będzie miał (rozmiar x rozmiar) komórek.
            """
            wyczysc_plotno()
            rozm_komorki = (szerokosc_okna - 10) / rozmiar

            y = -rozm_komorki + 5
            for i in range(1, rozmiar + 1):
                x = 5
                y = y + rozm_komorki
                for j in range(1, rozmiar + 1):
                    canvas.create_line([x, y], [x + rozm_komorki, y])
                    canvas.create_line([x + rozm_komorki, y],
                                       [x + rozm_komorki, y + rozm_komorki])
                    canvas.create_line([x + rozm_komorki, y + rozm_komorki],
                                       [x, y + rozm_komorki])
                    canvas.create_line([x, y + rozm_komorki], [x, y])
                    plansza.append((x, y))
                    x = x + rozm_komorki

        def przesun(kierunek, x, y, rozmiar):
            """Przesuwa się do nowej komórki w labiryncie, usuwając ścianę
            między bieżącą a następną komórką.

            Parametry:
            kierunek (str): kierunek przesunięcia, "gora", "dol",
            "lewo" lub "prawo".
            x (int): współrzędna x bieżącej komórki.
            y (int): współrzędna y bieżącej komórki.
            rozmiar (int): rozmiar labiryntu, gdzie labirynt będzie miał (
            rozmiar x rozmiar) komórek.
            """
            rozm_komorki = (szerokosc_okna - 10) / rozmiar

            if kierunek == "gora":
                canvas.create_line(x, y, x + rozm_komorki, y, fill='#F0F0F0')

            if kierunek == "dol":
                canvas.create_line(x, y + rozm_komorki, x + rozm_komorki,
                                   y + rozm_komorki, fill='#F0F0F0')

            if kierunek == "lewo":
                canvas.create_line(x, y, x, y + rozm_komorki, fill='#F0F0F0')

            if kierunek == "prawo":
                canvas.create_line(x + rozm_komorki, y, x + rozm_komorki,
                                   y + rozm_komorki, fill='#F0F0F0')

            canvas.update()

        def labirynt(x, y, rozmiar):
            """Generuje labirynt, dokonując serii ruchów za
            pomocą algorytmu przeszukiwania w głąb z losowym wybieraniem
            następnej komórki.

            Parametry:
            pozycja_x (int): współrzędna x bieżącej komórki.
            pozycja_y (int): współrzędna y bieżącej komórki.
            rozmiar (int): rozmiar labiryntu, gdzie labirynt będzie miał (
            rozmiar x rozmiar) komórek.
            """
            zbuduj_szkielet_labiryntu(rozmiar)
            stos.append((x, y))
            odwiedzone.append((x, y))
            slownik_przejsc[0] = rozmiar

            while len(odwiedzone) != len(plansza):
                komorka = []
                rozm_komorki = (szerokosc_okna - 10) / rozmiar

                if (x, y - rozm_komorki) not in odwiedzone and (
                        x, y - rozm_komorki) in plansza:
                    komorka.append("gora")

                if (x + rozm_komorki, y) not in odwiedzone and (
                        x + rozm_komorki, y) in plansza:
                    komorka.append("prawo")

                if (x, y + rozm_komorki) not in odwiedzone and (
                        x, y + rozm_komorki) in plansza:
                    komorka.append("dol")

                if (x - rozm_komorki, y) not in odwiedzone and (
                        x - rozm_komorki, y) in plansza:
                    komorka.append("lewo")

                if len(komorka) > 0:
                    cell_chosen = (random.choice(komorka))

                    if cell_chosen == "prawo":
                        przesun(cell_chosen, x, y, rozmiar)
                        slownik_przejsc[(x + rozm_komorki, y)] = x, y
                        x = x + rozm_komorki
                        odwiedzone.append((x, y))
                        stos.append((x, y))

                    if cell_chosen == "lewo":
                        przesun(cell_chosen, x, y, rozmiar)
                        slownik_przejsc[(x - rozm_komorki, y)] = x, y
                        x = x - rozm_komorki
                        odwiedzone.append((x, y))
                        stos.append((x, y))

                    if cell_chosen == "dol":
                        przesun(cell_chosen, x, y, rozmiar)
                        slownik_przejsc[(x, y + rozm_komorki)] = x, y
                        y = y + rozm_komorki
                        odwiedzone.append((x, y))
                        stos.append((x, y))

                    if cell_chosen == "gora":
                        przesun(cell_chosen, x, y, rozmiar)
                        slownik_przejsc[(x, y - rozm_komorki)] = x, y
                        y = y - rozm_komorki
                        odwiedzone.append((x, y))
                        stos.append((x, y))
                else:
                    if len(stos) != 0:
                        x, y = stos.pop()

            else:
                koniec_generowania = tk.Label(okno,
                                           text='Skonczono generowanie '
                                                'labiryntu')
                canvas.create_window(szerokosc_okna // 2, 647, height=20,
                                     width=250, window=koniec_generowania)

                zapisz_obraz = tk.Button(text='Zapisz jako obraz',
                                      command=zapisz_obraz_do_png)
                canvas.create_window(szerokosc_okna // 2 - 100, 668,
                                     window=zapisz_obraz)

                zapisz_labirynt = tk.Button(text='Zapisz wzor labiryntu',
                                         command=zapisz_wzor_labiryntu)
                canvas.create_window(szerokosc_okna // 2 + 100, 668,
                                     window=zapisz_labirynt)

        def zapisz_obraz_do_png():
            """Akcja dla przycisku zapisu do obrazka. Zapisuje bieżące
            płótno labiryntu jako plik obrazu PNG. """
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[
                                                         ("PNG", "*.png")])

            if len(file_path) != 0:
                image = Image.new('RGB', (550, 550),
                                  (255, 255, 255))

                # wygenerowanie obrazka z płótna
                canvas.postscript(file=file_path, colormode='color')

                # otwarcie pliku PostScript i narysowanie go na obiekcie Image
                with open(f"{file_path}", "rb") as f:
                    image_ps = Image.open(f)
                    image.paste(image_ps, (0, 0))

                # zapisanie obiektu Image jako pliku png
                image.save(f'{file_path}', 'PNG')

        def zapisz_wzor_labiryntu():
            """Akcja dla przycisku zapisywania labiryntu. Zapisuje serie
            przejść bieżącego labiryntu jako plik JSON. """
            slownik_przejsc_do_zapisania = {str(klucz): str(wartosc) for
                                            klucz, wartosc in
                                            slownik_przejsc.items()}

            file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                     filetypes=[("JSON files",
                                                                 "*.json")])

            if len(file_path) != 0:
                with open(file_path, "w") as outfile:
                    # Zapisujemy słownik do pliku JSON
                    json.dump(slownik_przejsc_do_zapisania, outfile)

        def wczytaj_wzor_labiryntu():
            """Akcja dla przycisku wczytywania labiryntu. Ładuje zapisaną
            serie przejść labiryntu z pliku JSON. """
            file_path = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json")])

            if len(file_path) != 0:
                wyczysc_wszystko()
                with open(file_path, 'r') as f:
                    dane = json.load(f)
                rozmiar_wczytanego = int(dane.get('0'))

                zbuduj_szkielet_labiryntu(rozmiar_wczytanego)

                del dane['0']

                for klucz, wartosc in dane.items():
                    klucz = klucz.replace('(', '')
                    klucz = klucz.replace(')', '')
                    klucz = klucz.split(',')
                    klucz[0], klucz[1] = float(klucz[0]), float(klucz[1])
                    wartosc = wartosc.replace('(', '')
                    wartosc = wartosc.replace(')', '')
                    wartosc = wartosc.split(',')
                    wartosc[0], wartosc[1] = float(wartosc[0]), float(
                        wartosc[1])

                    if wartosc[0] < klucz[0] and wartosc[1] == klucz[1]:
                        przesun("prawo", wartosc[0], wartosc[1],
                                rozmiar_wczytanego)
                    if wartosc[0] > klucz[0] and wartosc[1] == klucz[1]:
                        przesun("lewo", wartosc[0], wartosc[1],
                                rozmiar_wczytanego)
                    if wartosc[0] == klucz[0] and wartosc[1] < klucz[1]:
                        przesun("dol", wartosc[0], wartosc[1],
                                rozmiar_wczytanego)
                    if wartosc[0] == klucz[0] and wartosc[1] > klucz[1]:
                        przesun("gora", wartosc[0], wartosc[1],
                                rozmiar_wczytanego)

                ramka()

                koniec_wczytywania = tk.Label(okno,
                                           text='Skonczono wczytywanie '
                                                'labiryntu')
                canvas.create_window(szerokosc_okna // 2, 647, height=20,
                                     width=250, window=koniec_wczytywania)

                zapisz_obraz = tk.Button(text='Zapisz jako obraz',
                                      command=zapisz_obraz_do_png)
                canvas.create_window(szerokosc_okna // 2, 668,
                                     window=zapisz_obraz)

        def wyczysc_plotno():
            """Czyści płótno, usuwając wszystkie na nim narysowane obiekty."""
            canvas.create_rectangle(lewa_gora, prawy_dol, fill='#F0F0F0')

        def wyczysc_napis():
            """Usuwa napis powstały po poprawnym wygenerowaniu lub wczytaniu
            labiryntu """
            canvas.create_window(szerokosc_okna // 2, 647, height=20,
                                 width=250,
                                 window=tk.Label(okno, text=''))

        def wyczysc_przyciski_po_generowaniu():
            """Usuwa przyciski akcji powstałe po poprawnym generowaniu
            labiryntu """
            canvas.create_window(szerokosc_okna // 2 - 100, 669, height=25,
                                 width=250, window=tk.Label(okno, text=''))
            canvas.create_window(szerokosc_okna // 2 + 100, 669, height=25,
                                 width=250, window=tk.Label(okno, text=''))

        def wyczysc_wszystko():
            """Czyści całe okno z elementów (labiryntu, przycisków, napisu)"""
            wyczysc_plotno()
            wyczysc_napis()
            wyczysc_przyciski_po_generowaniu()
            plansza.clear()
            odwiedzone.clear()
            stos.clear()
            canvas.update()
            slownik_przejsc.clear()

        def generuj():
            """Akcja dla przycisku generowania labiryntu. Jeżeli został
            wprowadzony prawidłowy rozmiar (int) generuje i rysuje labirynt,
            w przeciwnym wypadku pokazuje ostrzeżenie. """
            try:
                wyczysc_wszystko()
                if pole_do_wpisywania.get() == '':
                    rozmiar = 20
                    labirynt(5, 5, rozmiar)
                    ramka()
                else:
                    rozmiar = int(pole_do_wpisywania.get())
                    if rozmiar < 3:
                        messagebox.showinfo("Ostrzeżenie", "Rozmiar "
                                                                   "musi "
                                                                   "wynosić "
                                                                   "minimum "
                                                                   "3!")
                    else:
                        labirynt(5, 5, rozmiar)
                        ramka()

                okno.update()
                okno.update_idletasks()
            except ValueError:
                messagebox.showinfo("Ostrzeżenie",
                                            "Podaj rozmiar planszy w postaci "
                                            "liczby całkowitej!")

        def buduj_same_sciany():
            """Akcja dla przycisku rysowania samej planszy. Jeżeli został
            wprowadzony prawidłowy rozmiar (int) generuje szkielet
            labiryntu, w przeciwnym wypadku pokazuje ostrzeżenie. """
            wyczysc_wszystko()
            canvas.update()
            try:
                if pole_do_wpisywania.get() == '':
                    rozmiar = 20
                    zbuduj_szkielet_labiryntu(rozmiar)
                    ramka()
                else:
                    rozmiar = int(pole_do_wpisywania.get())
                    if rozmiar < 3:
                        messagebox.showinfo("Ostrzeżenie", "Rozmiar "
                                                                   "musi "
                                                                   "wynosić "
                                                                   "minimum "
                                                                   "3!")
                    else:
                        zbuduj_szkielet_labiryntu(rozmiar)
                        ramka()
            except ValueError:
                messagebox.showinfo("Ostrzeżenie",
                                            "Podaj rozmiar planszy w postaci "
                                            "liczby całkowitej!")

        pole_do_wpisywania = tk.Entry(okno)
        canvas.create_window(szerokosc_okna // 2, 580, height=20, width=50,
                             window=pole_do_wpisywania)

        napis_rozmiar = tk.Label(okno, text="Rozmiar planszy")
        canvas.create_window(szerokosc_okna // 2, 560, height=20, width=300,
                             window=napis_rozmiar)

        przycisk_generowania = tk.Button(text='Generuj labirynt',
                                       command=generuj)
        canvas.create_window(szerokosc_okna // 2 - 100, 600,
                             window=przycisk_generowania)

        przycisk_wczytania_lab = tk.Button(text='Wczytaj wzor labiryntu',
                                        command=wczytaj_wzor_labiryntu)
        canvas.create_window(szerokosc_okna // 2, 625,
                             window=przycisk_wczytania_lab)

        przycisk_budowania_scian = tk.Button(text='Narysuj sama sciany',
                                          command=buduj_same_sciany)
        canvas.create_window(szerokosc_okna // 2 + 100, 600,
                             window=przycisk_budowania_scian)

        canvas.pack(fill=tk.BOTH, expand=1)


def main():
    """Funkcja główna programu"""
    Labirynt()
    okno.protocol("WM_DELETE_WINDOW", on_closing)
    okno.mainloop()


if __name__ == '__main__':
    main()
