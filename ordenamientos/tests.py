from ordenamientos.algorithms import Counter

# Algoritmos con contador de swaps integrado
def ordenar_insercion(a: list[int], counter: Counter) -> None:
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and clave < a[j]:
            a[j + 1] = a[j]
            counter.swaps += 1
            print(f"Insercion swap: {a[j+1]} <-> {a[j]}")  # mostrar intercambio
            j -= 1
        a[j + 1] = clave


def ordenar_seleccion(a: list[int], counter: Counter) -> None:
    n = len(a)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if a[j] < a[idx_min]:
                idx_min = j
        if idx_min != i:
            print(f"Seleccion swap: {a[i]} <-> {a[idx_min]}")
            a[i], a[idx_min] = a[idx_min], a[i]
            counter.swaps += 1


def ordenar_burbuja(a: list[int], counter: Counter) -> None:
    n = len(a)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - 1 - i):
            if a[j + 1] < a[j]:
                print(f"Burbuja swap: {a[j]} <-> {a[j+1]}")
                a[j], a[j + 1] = a[j + 1], a[j]
                counter.swaps += 1
                hubo_intercambio = True
        if not hubo_intercambio:
            break


# Vectores desordenados para pruebas
pruebas = [
    [3, 1, 2],
    [5, 4, 3, 2, 1],
    [2, 5, 1, 4, 3],
]

algoritmos = {
    "insercion": ordenar_insercion,
    "seleccion": ordenar_seleccion,
    "burbuja": ordenar_burbuja,
}

for nombre, algoritmo in algoritmos.items():
    print(f"\n=== Probando {nombre} ===")
    for i, vec in enumerate(pruebas, 1):
        vec_copy = vec[:]          
        counter = Counter()
        algoritmo(vec_copy, counter)
        print(f"Prueba {i}: original={vec} -> ordenado={vec_copy}, intercambios={counter.swaps}")
