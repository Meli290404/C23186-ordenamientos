import os
import random
import numpy as np
import matplotlib.pyplot as plt
from .algorithms import ALGORITHMS, Counter


def generar_vectores(num_vectores: int, tam: int) -> list[list[int]]:
    return [
        [random.randint(1, 100) for _ in range(tam)]
        for _ in range(num_vectores)
    ]


def main():
    NUM_VECTORES = 10
    TAM_VECTOR = 100

    resultados: dict[str, list[int]] = {nombre: [] for nombre in ALGORITHMS}

    # Probar cada algoritmo
    for nombre, algoritmo in ALGORITHMS.items():
        for _ in range(NUM_VECTORES):
            vector = [random.randint(1, 100) for _ in range(TAM_VECTOR)]
            counter = Counter()
            algoritmo(vector[:], counter)  # usamos copia con [:]
            resultados[nombre].append(counter.swaps)

    # Tabla de resultados
    print("\n=== Resultados de intercambios ===")
    print(f"{'Algoritmo':<12} {'Promedio':>10} {'Desv.Std.':>10}")
    for nombre, valores in resultados.items():
        promedio = np.mean(valores)
        desviacion = np.std(valores)
        print(f"{nombre:<12} {promedio:10.2f} {desviacion:10.2f}")

    # Crear carpeta results si no existe
    os.makedirs("results", exist_ok=True)

    # Gráfico boxplot
    plt.boxplot(resultados.values(), tick_labels=resultados.keys())  # tick_labels evita warning
    plt.title("Comparación de intercambios por algoritmo")
    plt.ylabel("Número de intercambios")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("results/boxplot.png", dpi=200)



if __name__ == "__main__":
    main()
