import random
from lab3.wzorce_cyfr import (cyfra_0, cyfra_1, cyfra_2, cyfra_3, cyfra_4,
                              cyfra_5, cyfra_6, cyfra_7, cyfra_8, cyfra_9)
import numpy as np

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

def oblicz_pole_lokalne(i, wagi, stan_sieci):
    h_i = np.dot(wagi[i], stan_sieci)
    return h_i

def aktualizuj_neuron(i, wagi, stan_sieci):
    h_i = oblicz_pole_lokalne(i, wagi, stan_sieci)
    if h_i > 1e-7:
        stan_sieci[i] = 1
    elif h_i < -1e-7:
        stan_sieci[i] = -1
    return stan_sieci

def odtworz_obraz(zaszumiony_obraz, wagi, maks_iteracji):
    stan_sieci = zaszumiony_obraz.copy().flatten()
    liczba_neuronow = len(stan_sieci)
    for i in range(maks_iteracji):
        liczba_zmian = 0
        for i in range(liczba_neuronow):
            stary_stan = stan_sieci[i]
            stan_sieci = aktualizuj_neuron(i, wagi, stan_sieci)
            if stary_stan != stan_sieci[i]:
                liczba_zmian += 1
        if liczba_zmian == 0:
            break
    return stan_sieci.reshape((8, 8))