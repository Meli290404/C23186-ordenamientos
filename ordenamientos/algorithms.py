import random
from dataclasses import dataclass
from typing import Callable


@dataclass
class Counter:
    swaps: int = 0


def ordenar_insercion(a: list[int], counter: Counter | None = None) -> None:
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and clave < a[j]:
            a[j + 1] = a[j]
            j -= 1
            if counter:
                counter.swaps += 1
        a[j + 1] = clave


def ordenar_seleccion(a: list[int], counter: Counter | None = None) -> None:
    n = len(a)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if a[j] < a[idx_min]:
                idx_min = j
        if idx_min != i:
            a[i], a[idx_min] = a[idx_min], a[i]
            if counter:
                counter.swaps += 1


def ordenar_burbuja(a: list[int], counter: Counter | None = None) -> None:
    n = len(a)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
                hubo_intercambio = True
                if counter:
                    counter.swaps += 1
        if not hubo_intercambio:
            break


# Diccionario de algoritmos
ALGORITHMS: dict[str, Callable[[list[int], Counter], None]] = {
    "insercion": ordenar_insercion,
    "seleccion": ordenar_seleccion,
    "burbuja": ordenar_burbuja,
}
