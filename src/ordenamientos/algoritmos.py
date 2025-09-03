from dataclasses import dataclass

@dataclass
class Counter:
    swaps: int = 0

def _swap(a, i, j, c: Counter):
    if i != j:
        a[i], a[j] = a[j], a[i]
        c.swaps += 1

def ordenar_insercion(a: list[int], c: Counter) -> None:
    """
    Ordena la lista 'a' en sitio usando inserción.
    Complejidad: O(n^2)
    Estable, in-place.
    """
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            _swap(a, j, j - 1, c)
            j -= 1

def ordenar_seleccion(a: list[int], c: Counter) -> None:
    """
    Ordena la lista 'a' en sitio usando selección.
    Complejidad: O(n^2)
    No estable, en sitio.
    Pocos intercambios: O(n).
    """
    n = len(a)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if a[j] < a[idx_min]:
                idx_min = j
        if idx_min != i:
            _swap(a, i, idx_min, c)

def ordenar_burbuja(a: list[int], c: Counter) -> None:
    """
    Ordena la lista 'a' en sitio usando burbuja con corte temprano.
    Complejidad: O(n^2)
    Estable.
    """
    n = len(a)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - 1 - i):
            if a[j + 1] < a[j]:
                _swap(a, j, j + 1, c)
                hubo_intercambio = True
        if not hubo_intercambio:
            break

# Diccionario para el programa principal
ALGORITHMS = {
    "Inserción": ordenar_insercion,
    "Selección": ordenar_seleccion,
    "Burbuja": ordenar_burbuja,
}
