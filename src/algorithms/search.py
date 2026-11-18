"""
Módulo de algoritmos de búsqueda para K.A.T.E.
Implementa búsqueda lineal O(n) y búsqueda mediante tabla hash O(1) promedio
para recuperar recuerdos almacenados por el asistente.
"""

import time
from typing import Any, Dict, List, Optional


def busqueda_lineal(registros: List[Dict[str, Any]], clave_objetivo: str) -> Optional[Dict[str, Any]]:
    """
    Busca un registro recorriendo secuencialmente la lista de elementos.

    Complejidad:
        - Temporal: O(n) en el peor caso y caso promedio; O(1) en el mejor caso.
        - Espacial: O(1) adicional.
    """
    clave_normalizada = clave_objetivo.strip().lower()

    for registro in registros:
        if registro.get("clave", "").strip().lower() == clave_normalizada:
            return registro

    return None


def construir_tabla_hash(registros: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Construye una tabla hash (diccionario de Python) indexada por la clave normalizada.

    Complejidad:
        - Temporal: O(n) para insertar n registros.
        - Espacial: O(n) para almacenar las referencias en la tabla hash.
    """
    tabla_hash: Dict[str, Dict[str, Any]] = {}

    for registro in registros:
        clave_normalizada = registro.get("clave", "").strip().lower()
        if clave_normalizada:
            tabla_hash[clave_normalizada] = registro

    return tabla_hash


def busqueda_hash(tabla_hash: Dict[str, Dict[str, Any]], clave_objetivo: str) -> Optional[Dict[str, Any]]:
    """
    Busca un registro mediante acceso directo por clave en una tabla hash (dict).

    Complejidad:
        - Temporal: O(1) en caso promedio; O(n) en el peor caso teórico por colisiones.
        - Espacial: O(1) durante la consulta.
    """
    clave_normalizada = clave_objetivo.strip().lower()

    if clave_normalizada in tabla_hash:
        return tabla_hash[clave_normalizada]

    return None


def _ejecutar_demostracion() -> None:
    """
    Ejecuta una prueba funcional y una comparación preliminar de tiempos
    para validar ambos algoritmos en Checkpoint 1.
    """
    print("=== K.A.T.E. | Prueba de Algoritmo Base Funcional ===\n")

    recuerdos_ejemplo = [
        {"id": 1, "clave": "correo_profesor", "valor": "algoritmos@universidad.edu"},
        {"id": 2, "clave": "repo_proyecto", "valor": "https://github.com/equipo/KATE"},
        {"id": 3, "clave": "hora_entrega", "valor": "Jueves 23:59"},
    ]

    indice_hash = construir_tabla_hash(recuerdos_ejemplo)

    print("1) Búsqueda existente ('repo_proyecto'):")
    print("   Lineal ->", busqueda_lineal(recuerdos_ejemplo, "repo_proyecto"))
    print("   Hash   ->", busqueda_hash(indice_hash, "repo_proyecto"))

    print("\n2) Búsqueda inexistente ('dato_fantasma'):")
    print("   Lineal ->", busqueda_lineal(recuerdos_ejemplo, "dato_fantasma"))
    print("   Hash   ->", busqueda_hash(indice_hash, "dato_fantasma"))

    print("\n3) Comparación preliminar de tiempos (peor caso):")
    for n in [1_000, 10_000, 100_000]:
        datos = [{"id": i, "clave": f"recuerdo_{i}", "valor": f"valor_{i}"} for i in range(n)]
        tabla = construir_tabla_hash(datos)
        objetivo = f"recuerdo_{n - 1}"

        inicio_lineal = time.perf_counter()
        busqueda_lineal(datos, objetivo)
        tiempo_lineal = (time.perf_counter() - inicio_lineal) * 1000

        inicio_hash = time.perf_counter()
        busqueda_hash(tabla, objetivo)
        tiempo_hash = (time.perf_counter() - inicio_hash) * 1000

        print(f"   n = {n:>7} | Lineal: {tiempo_lineal:>8.4f} ms | Hash: {tiempo_hash:>8.4f} ms")


if __name__ == "__main__":
    _ejecutar_demostracion()
