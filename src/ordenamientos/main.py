import os
import random
from statistics import mean, stdev
import pandas as pd
import matplotlib.pyplot as plt

from .algorithms import ALGORITHMS, Counter

def generar_vectores(num_vectores=10, n=100, low=1, high=100):
    rng = random.Random()
    return [[rng.randint(low, high) for _ in range(n)] for _ in range(num_vectores)]

def main():
    base = generar_vectores()
    resultados = {}
    resumen = []

    for nombre, algoritmo in ALGORITHMS.items():
        counts = []
        for vec in base:
            arr = vec.copy()
            c = Counter()
            algoritmo(arr, c)
            counts.append(c.swaps)
        resultados[nombre] = counts
        prom = mean(counts)
        desv = stdev(counts) if len(counts) > 1 else 0.0
        resumen.append({"Algoritmo": nombre, "Promedio": prom, "DesvEst": desv})

    df = pd.DataFrame(resumen)
    print(df.to_string(index=False, float_format=lambda x: f"{x:.2f}"))

    os.makedirs("results", exist_ok=True)
    df.to_csv("results/resumen.csv", index=False)

    # Boxplot
    plt.boxplot(resultados.values(), labels=resultados.keys())
    plt.title("Número de intercambios (10 vectores de 100 elementos)")
    plt.ylabel("Intercambios")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("results/boxplot.png", dpi=200)

if __name__ == "__main__":
    main()
