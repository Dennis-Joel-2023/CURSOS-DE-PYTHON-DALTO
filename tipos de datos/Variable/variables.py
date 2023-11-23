from typing import List, Dict

# Anotaciones de tipo para variables
edad: int = 25
altura: float = 1.75
nombre: str = "Juan"
es_estudiante: bool = True

# Anotaciones de tipo para listas y diccionarios
numeros: List[int] = [1, 2, 3, 4, 5]
precios: Dict[str, float] = {'manzana': 1.2, 'banana': 0.75, 'naranja': 1.0}

# Anotaciones de tipo para funciones
def suma(a: int, b: int) -> int:
    return a + b

def concatenar(cadena1: str, cadena2: str) -> str:
    return cadena1 + cadena2
