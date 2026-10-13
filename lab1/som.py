#1. Przygotowanie środowiska
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#2. Wczytanie danych
iris = load_iris()
x = iris.data
y = iris.target
df = pd.DataFrame(x, columns=['Długość działki[cm]', 'Szerokość działki[cm]', 'Długość płatka[cm]', 'Szerokość płatka[cm]'])
df['gatunek'] = y

#3. Analiza danych
print("Liczba wierszy: ", df.shape[0])
print("Liczba cech: ", df.shape[1])
print("Podział na klasy:\n", df['gatunek'].value_counts())
print("Pierwsze 5 danych:\n", df.head())

#4. Normalizacja
print("Średnie kolumn przed standaryzacją:\n", np.mean(x, axis=0))
print("Odchylenia standardowe kolumn przed standaryzacją:\n", np.std(x, axis=0))
x_srednia = np.mean(x, axis=0)
x_odchylenie_standardowe = np.std(x, axis=0)
x_ustandaryzowane = (x - x_srednia) / x_odchylenie_standardowe
print("Średnie kolumn po standaryzacji:\n", np.mean(x_ustandaryzowane, axis=0))
print("Odchylenia standardowe kolumn po standaryzacji:\n", np.std(x_ustandaryzowane, axis=0))

#5. Utworzenie neuronów
neurony = np.random.randn(3, 4)

#6. Implementacja odległości
def oblicz_odleglosci(kwiatek, neurony):
    odleglosci_d = np.sqrt(np.sum((neurony - kwiatek) ** 2, axis=1))
    return odleglosci_d

#7. Znalezienie neuronu zwycięskiego
def znajdz_zwyciezce(kwiatek, neurony):
    indeks_zwyciezcy = np.argmin(oblicz_odleglosci(kwiatek, neurony))
    return indeks_zwyciezcy

#8. Implementacja aktualizacji wag
def przybliz_neuron(kwiatek, neurony, indeks_zwyciezcy, krok):
    neurony[indeks_zwyciezcy] = neurony[indeks_zwyciezcy] + krok * (kwiatek - neurony[indeks_zwyciezcy])
    return neurony

# OSTATECZNA FUNKCJA UPROSZCZONEGO ALGORYTMU SOM
def algorytm_som(przyklady, neurony, tempo_uczenia, liczba_epok):
    while(liczba_epok != 0):
        tempo_uczenia = tempo_uczenia * 0.95
        for przyklad in przyklady:
            zwyciezca = znajdz_zwyciezce(przyklad, neurony)
            neurony = przybliz_neuron(przyklad, neurony, zwyciezca, tempo_uczenia)
        liczba_epok -= 1
    return neurony

# testy
wytrenowane_neurony = algorytm_som(x_ustandaryzowane, neurony.copy(), tempo_uczenia=0.5, liczba_epok=100)
przypisane_etykiety = [znajdz_zwyciezce(kwiatek, wytrenowane_neurony) for kwiatek in x_ustandaryzowane]
ilosci_elementow = {0: 0, 1: 0, 2: 0}
for etykieta in przypisane_etykiety:
    ilosci_elementow[etykieta] += 1

print("WYNIKI UCZENIA ALGORYTMEM SOM")
print("Rozkład kwiatków w grupach:")
for neuron_i, ilosc in ilosci_elementow.items():
    print(f"Neuron {neuron_i} zgrupował {ilosc} sztuk")
print("\nOstateczne wagi neuronów (pozycje w 4-wymiarowej przestrzeni):")
print(np.round(wytrenowane_neurony, 2))