
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.algorithms.search import (
    busqueda_lineal,
    construir_tabla_hash,
    busqueda_hash
)


def test_busqueda_lineal_encuentra_registro():
    datos = [
        {"clave": "nombre", "valor": "KATE"},
        {"clave": "proyecto", "valor": "Asistente virtual"}
    ]

    resultado = busqueda_lineal(datos, "nombre")
    assert resultado["valor"] == "KATE"


def test_busqueda_lineal_no_encuentra():
    datos = [{"clave": "nombre", "valor": "KATE"}]
    assert busqueda_lineal(datos, "inexistente") is None


def test_busqueda_hash_encuentra_registro():
    datos = [{"clave": "nombre", "valor": "KATE"}]
    tabla = construir_tabla_hash(datos)

    resultado = busqueda_hash(tabla, "nombre")
    assert resultado["valor"] == "KATE"


def test_busqueda_hash_no_encuentra():
    datos = [{"clave": "nombre", "valor": "KATE"}]
    tabla = construir_tabla_hash(datos)

    assert busqueda_hash(tabla, "inexistente") is None
