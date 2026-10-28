import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg
from lab3.hopfield import (cyfra_0,
                           cyfra_1,
                           cyfra_2,
                           cyfra_3,
                           cyfra_4,
                           cyfra_5,
                           cyfra_6,
                           cyfra_7,
                           cyfra_8,
                           cyfra_9,
                           wzorce_zaszumione_10,
                           wzorce_zaszumione_20,
                           wzorce_zaszumione_30,
                           moje_kolory)

from lab3.hopfield import odtworz_obraz


X = np.array([
    cyfra_0.flatten(),
    cyfra_1.flatten(),
    cyfra_2.flatten(),
    cyfra_3.flatten(),
    cyfra_4.flatten(),
    cyfra_5.flatten(),
    cyfra_6.flatten(),
    cyfra_7.flatten(),
    cyfra_8.flatten(),
    cyfra_9.flatten()
])

wagi_pseudoinwersja = X.T @ numpy.linalg.pinv(X @ X.T) @ X
wagi_hebba = (X.T @ X) / 64

np.fill_diagonal(wagi_pseudoinwersja, 0)
np.fill_diagonal(wagi_hebba, 0)

def storkey(X, liczba_neuronow = 64):
    w = np.zeros((liczba_neuronow, liczba_neuronow))
    for wzorzec in X:
        w_nowe = w.copy()
        h = w @ wzorzec
        for i in range(liczba_neuronow):
            for j in range(liczba_neuronow):
                if i != j:
                    h_ij = h[i] - w[i, j] * wzorzec[j]
                    h_ji = h[j] - w[j, i] * wzorzec[i]
                    w_nowe[i, j] += (wzorzec[i] * wzorzec[j] - wzorzec[i] * h_ji - wzorzec[j] * h_ij) / liczba_neuronow
        w = w_nowe
        np.fill_diagonal(w, 0)
    return w

wagi_storkey = storkey(X)

zaszumiona_3 = wzorce_zaszumione_30[3]
odtworzona_3_pseudoinwersja = odtworz_obraz(zaszumiona_3, wagi_pseudoinwersja, 10)
odtworzona_3_hebb = odtworz_obraz(zaszumiona_3, wagi_hebba, 10)
odtworzona_3_storkey = odtworz_obraz(zaszumiona_3, wagi_storkey, 10)

if __name__ == '__main__':
    print("Czy macierz jest symetryczna?")
    print(np.allclose(wagi_pseudoinwersja, wagi_pseudoinwersja.T))

    print("===PORÓWNANIE METOD===")
    f, o = plt.subplots(1, 5, figsize=(15, 3))
    o[0].imshow(cyfra_3, cmap=moje_kolory)
    o[0].set_title("Oryginał")

    o[1].imshow(zaszumiona_3, cmap=moje_kolory)
    o[1].set_title("Zaszumiony (30% szumu)")

    o[2].imshow(odtworzona_3_hebb, cmap=moje_kolory)
    o[2].set_title("Wynik: Reguła Hebba")

    o[3].imshow(odtworzona_3_pseudoinwersja, cmap=moje_kolory)
    o[3].set_title("Wynik: Pseudoinwersja")

    o[4].imshow(odtworzona_3_storkey, cmap=moje_kolory)
    o[4].set_title("Wynik: Storkey")

    for os in o:
        os.axis('off')
    plt.show()