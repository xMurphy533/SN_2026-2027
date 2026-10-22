import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import  ListedColormap

moje_kolory = ListedColormap(['darkblue', 'yellow'])

cyfra_0 = np.array([
    [-1, -1,  1,  1,  1,  1, -1, -1],
    [-1,  1, -1, -1, -1, -1,  1, -1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [-1,  1, -1, -1, -1, -1,  1, -1],
    [-1, -1,  1,  1,  1,  1, -1, -1]
])

cyfra_1 = np.array([
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, 1, 1, 1, 1, -1, -1]
])

cyfra_2 = np.array([
    [-1, -1, 1, 1, 1, -1, -1, -1],
    [-1, 1, -1, -1, 1, 1, -1, -1],
    [1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, 1, 1, -1, -1],
    [-1, -1, -1, 1, 1, -1, -1, -1],
    [-1, -1, 1, 1, -1, -1, -1, -1],
    [-1, 1, 1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])

cyfra_3 = np.array([
    [-1, -1, 1, 1, 1, 1, -1, -1],
    [-1, 1, 1, 1, -1, -1, 1, 1],
    [1, 1, -1, -1, -1, -1, 1, 1],
    [-1, -1, -1, -1, -1, -1, 1, 1],
    [-1, -1, -1, -1, 1, 1, -1, -1],
    [1, 1, -1, -1, -1, -1, 1, 1],
    [-1, 1, 1, 1, -1, -1, 1, 1],
    [-1, -1, 1, 1, 1, 1, -1, -1]
])

cyfra_4 = np.array([
    [-1, -1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, 1, -1, -1],
    [-1, 1, 1, -1, 1, 1, -1, -1],
    [-1, 1, -1, -1, 1, 1, -1, -1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, 1, 1, -1, -1],
    [-1, -1, -1, -1, 1, 1, -1, -1]
])

cyfra_5 = np.array([
    [-1, -1, 1, 1, 1, 1, -1, -1],
    [-1, -1, 1, -1, -1, -1, -1, -1],
    [-1, -1, 1, -1, -1, -1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, -1, 1, -1, -1],
    [-1, 1, -1, -1, 1, -1, -1, -1],
    [-1, -1, 1, 1, -1, -1, -1, -1]
])

cyfra_6 = np.array([
    [-1, -1, -1, -1, 1, -1, -1, -1],
    [-1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, 1, -1, -1, -1, -1, -1],
    [-1, 1, -1, -1, -1, -1, -1, -1],
    [-1, 1, 1, 1, 1, -1, -1, -1],
    [-1, 1, -1, -1, -1, 1, -1, -1],
    [-1, 1, -1, -1, -1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1, -1]
])

cyfra_7 = np.array([
    [-1, -1, 1, 1, 1, 1, 1, -1],
    [-1, -1, -1, -1, -1, -1, 1, -1],
    [-1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, 1, -1, -1, -1],
    [-1, -1, -1, -1, 1, -1, -1, -1],
    [-1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, 1, -1, -1, -1, -1]
])

cyfra_8 = np.array([
    [-1, -1,  1,  1,  1,  1, -1, -1],
    [-1,  1, -1, -1, -1, -1,  1, -1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [-1,  1,  1,  1,  1,  1,  1, -1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [ 1, -1, -1, -1, -1, -1, -1,  1],
    [-1,  1, -1, -1, -1, -1,  1, -1],
    [-1, -1,  1,  1,  1,  1, -1, -1]
])

cyfra_9 = np.array([
    [-1, -1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, -1, -1, -1, 1, -1],
    [-1, -1, 1, -1, -1, -1, 1, -1],
    [-1, -1, -1, 1, 1, 1, 1, -1],
    [-1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, -1, -1, 1, -1, -1, -1],
    [-1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, 1, -1, -1, -1, -1, -1]
])

def dodajSzum(obraz, poziom_szumu):
    zaszumiony_obraz = obraz.copy().flatten()
    liczba_pikseli = len(zaszumiony_obraz)

    ile_zmienic = int(liczba_pikseli * (poziom_szumu / 100.0))
    indeksy_do_zepsucia = random.sample(range(liczba_pikseli), ile_zmienic)

    for i in indeksy_do_zepsucia:
        zaszumiony_obraz[i] *= -1

    return zaszumiony_obraz.reshape((8, 8))

wzorce = [cyfra_0, cyfra_1, cyfra_2, cyfra_3, cyfra_4,
          cyfra_5, cyfra_6, cyfra_7, cyfra_8, cyfra_9]

wzorce_zaszumione_10 = []
wzorce_zaszumione_20 = []
wzorce_zaszumione_30 = []

for wzorzec in wzorce:
    wzorzec_zaszumiony = dodajSzum(wzorzec, 10)
    wzorce_zaszumione_10.append(wzorzec_zaszumiony)

for wzorzec in wzorce:
    wzorzec_zaszumiony = dodajSzum(wzorzec, 20)
    wzorce_zaszumione_20.append(wzorzec_zaszumiony)

for wzorzec in wzorce:
    wzorzec_zaszumiony = dodajSzum(wzorzec, 30)
    wzorce_zaszumione_30.append(wzorzec_zaszumiony)

def wyswietlPrzedIPoZaszumieniu(wzorzec, poziomZaszumienia):
    fig, osie = plt.subplots(1, 2)
    osie[0].imshow(wzorzec, cmap=moje_kolory)
    osie[0].set_title("Oryginał")
    osie[1].imshow(dodajSzum(wzorzec, poziomZaszumienia), cmap=moje_kolory)
    osie[1].set_title(f"{poziomZaszumienia}% zaszumienia")
    for os in osie:
        os.axis('off')
    plt.show()

