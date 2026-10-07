import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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