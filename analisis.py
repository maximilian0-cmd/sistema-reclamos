import csv
import matplotlib.pyplot as plt
from collections import Counter
categorias_reclamos = []
with open("reclamos.csv","r",encoding="utf-8") as archivo:
    lector=csv.DictReader(archivo)
    for fila in lector:
        categorias_reclamos.append(fila["categoria"])
#print(categorias_reclamos)
conteo=Counter(categorias_reclamos)
#print(conteo)
barras=plt.bar(conteo.keys(),conteo.values(),color="#7B2ABD",edgecolor="#2CC7A4")
plt.bar_label(barras, fontsize=11, weight="bold", padding=3)
plt.title("Cantidad de Reclamos por Categoría", fontsize=14, weight="bold", fontfamily="Cooper Black")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()