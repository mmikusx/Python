# Generowanie labiryntu - projekt zaliczeniowy

## Autor: Mikołaj Szymański

## O projekcie:
Tematem projektu jest stworzenie programu do generowania labiryntów. Do tego 
celu stworzony został program z interfejsem użytkownika pozwalający w 
interaktywny sposób generować, zapisywać czy też wczytywać z pliku labirynty.
Do generowania labiryntów wykorzystywany jest algorytm przeszukiwania w głąb 
(DFS) z losowym wyborem następnej komórki. Do wizualizacji generowania
labiryntów w czasie rzeczywistym oraz stworzenia interaktywnego interfejsu 
wykorzystana została biblioteka Tkinter.
####
### Więcej o interfejsie i dostępnych w nim funkcjach:
Po uruchomieniu programu w dolnej części okna widzimy pole tekstowe w którym 
możemy wpisać rozmiar labiryntu który chcemy wygenerować, lub dla którego 
chcemy stworzyć sam 'szkielet' oraz trzy przyciski. Przycisk `generuj labirynt`
służy do wygenerowania labiryntu o podanym rozmiarze lub jeśli nic nie zostało 
wpisane domyślnie program przyjmuje wartość 20, natomiast przycisk `Narysuj 
same ściany` służący do narysowania samych ścian labiryntu. Trzeci przycisk
`Wczytaj wzor labiryntu` służy do wczytania zapisanego wcześniej labiryntu z 
pliku o formacie JSON.
####
> Funkcje pojawiające się po wygenerowaniu labiryntu

Po wygenerowaniu labiryntu wyświetla się informacja o pomyślnym zakończeniu
generowania i rysowania labiryntu. Pojawiają się również dwa dodatkowe 
przyciski `Zapisz jako obraz` pozwalający zapisać nasz wygenerowany labirynt
jako obraz PNG oraz `Zapisz wzor labiryntu`, który zapisuje do pliku JSON
informacje potrzebne programowi do ewentualnego wczytania wzoru labiryntu, 
takie jak rozmiar labiryntu oraz przejścia pomiędzy kolejnymi komórkami.

> Funkcje pojawiające się po wczytaniu labiryntu z pliku

Po wczytaniu labiryntu wyświetla się informacja o pomyślnym zakończeniu
rysowania wczytanego labiryntu, a pod nim pojawia się tak jak po generowaniu,
przycisk `Zapisz jako obraz` umożliwiający zapisanie naszego labiryntu jako
obrazu PNG.
####
## Uruchamianie:
### Do uruchomienia programu potrzebne są:
- Python >= 3.5
- biblioteka `Tkinter`
- biblioteka `json`
- biblioteka `PIL` (Python Imaging Library)
### Aby uruchomić program:
W terminalu przejdź do katalogu w którym znajduje się program, a następnie
wpisz komendę `python3 Labirynt.py`