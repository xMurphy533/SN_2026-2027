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

zaszumiona_3 = wzorce_zaszumione_30[3]
odtworzona_3_pseudoinwersja = odtworz_obraz(zaszumiona_3, wagi_pseudoinwersja, 10)
odtworzona_3_hebb = odtworz_obraz(zaszumiona_3, wagi_hebba, 10)


if __name__ == '__main__':
    print("Czy macierz jest symetryczna?")
    print(np.allclose(wagi_pseudoinwersja, wagi_pseudoinwersja.T))

    fig, osie = plt.subplots(1, 3, figsize=(12, 4))
    osie[0].imshow(cyfra_3, cmap=moje_kolory)
    osie[0].set_title("Oryginał")
    osie[1].imshow(zaszumiona_3, cmap=moje_kolory)
    osie[1].set_title("Zaszumiony (30%)")
    osie[2].imshow(odtworzona_3_pseudoinwersja, cmap=moje_kolory)
    osie[2].set_title("Odtworzony (Pseudoinwersja)")

    for os in osie:
        os.axis('off')
    plt.show()

    print("===PORÓWNANIE METOD===")
    f, o = plt.subplots(1, 4, figsize=(12, 4))
    o[0].imshow(cyfra_3, cmap=moje_kolory)
    o[0].set_title("Oryginał")

    o[1].imshow(zaszumiona_3, cmap=moje_kolory)
    o[1].set_title("Zaszumiony (30% szumu)")

    o[2].imshow(odtworzona_3_hebb, cmap=moje_kolory)
    o[2].set_title("Wynik: Reguła Hebba")

    o[3].imshow(odtworzona_3_pseudoinwersja, cmap=moje_kolory)
    o[3].set_title("Wynik: Pseudoinwersja")

    for os in o:
        os.axis('off')
    plt.show()