import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target
df = pd.DataFrame(x, columns=['Długość działki[cm]', 'Szerokość działki[cm]', 'Długość płatka[cm]', 'Szerokość płatka[cm]'])
df['gatunek'] = y

print("Liczba wierszy: ", df.shape[0])
print("Liczba cech: ", df.shape[1])
print("Podział na klasy:\n", df['gatunek'].value_counts())
print("Pierwsze 5 danych:\n", df.head())

print("Średnie kolumn przed standaryzacją:\n", np.mean(x, axis=0))
print("Odchylenia standardowe kolumn przed standaryzacją:\n", np.std(x, axis=0))
x_srednia = np.mean(x, axis=0)
x_odchylenie_standardowe = np.std(x, axis=0)
x_ustandaryzowane = (x - x_srednia) / x_odchylenie_standardowe
print("Średnie kolumn po standaryzacji:\n", np.mean(x_ustandaryzowane, axis=0))
print("Odchylenia standardowe kolumn po standaryzacji:\n", np.std(x_ustandaryzowane, axis=0))

neurony = np.random.randn(3, 4)

def oblicz_odleglosci(kwiatek, neurony):
    odleglosci_d = np.sqrt(np.sum((neurony - kwiatek) ** 2, axis=1))
    return odleglosci_d

def znajdz_zwyciezce(kwiatek, neurony):
    indeks_zwyciezcy = np.argmin(oblicz_odleglosci(kwiatek, neurony))
    return indeks_zwyciezcy

def przybliz_neuron(kwiatek, neurony, indeks_zwyciezcy, krok):
    neurony[indeks_zwyciezcy] = neurony[indeks_zwyciezcy] + krok * (kwiatek - neurony[indeks_zwyciezcy])
    return neurony

# [LAB 2] możliwość określenia liczby epok
def algorytm_som(przyklady, neurony, tempo_uczenia, liczba_epok):
    T = liczba_epok
    while liczba_epok != 0:
        # [LAB 2] zmniejszanie współczynnika uczenia w miarę trwania algorytmu
        tempo = tempo_uczenia * (liczba_epok / T)

        # [LAB 2] wyświetlanie wartości współczynnika co 10 epok
        if liczba_epok % 10 == 0:
            print("Wartość współczynnika: ", tempo)

        for przyklad in przyklady:
            zwyciezca = znajdz_zwyciezce(przyklad, neurony)
            neurony = przybliz_neuron(przyklad, neurony, zwyciezca, tempo)

        liczba_epok -= 1

    return neurony

wytrenowane_neurony = algorytm_som(x_ustandaryzowane, neurony.copy(), tempo_uczenia=0.4, liczba_epok=80)
przypisane_etykiety = [znajdz_zwyciezce(kwiatek, wytrenowane_neurony) for kwiatek in x_ustandaryzowane]
ilosci_elementow = {0: 0, 1: 0, 2: 0}
for etykieta in przypisane_etykiety:
    ilosci_elementow[etykieta] += 1

print("WYNIKI UCZENIA ALGORYTMEM SOM")
# [LAB 2] przypisanie przykładów do każdego neuronu
print("Rozkład kwiatków w grupach:")
for neuron_i, ilosc in ilosci_elementow.items():
    print(f"Neuron {neuron_i + 1} zgrupował {ilosc} sztuk")
print("\nOstateczne wagi neuronów (pozycje w 4-wymiarowej przestrzeni):")
print(np.round(wytrenowane_neurony, 2))

# [LAB 2] Macierz rozkładu przykładów
macierz_wynikow = np.zeros((3, 3), dtype=int)
for nazwa_gatunku, przypisany_neuron in zip(y, przypisane_etykiety):
    macierz_wynikow[przypisany_neuron][nazwa_gatunku] += 1
print("\nMacierz rozkładu przykładów")
print("Neuron | Setosa | Versicolor | Virginica")
print("-" * 45)
for i in range(3):
    print(f"N{i+1}     | {macierz_wynikow[i][0]}     | {macierz_wynikow[i][1]}         | {macierz_wynikow[i][2]}")
