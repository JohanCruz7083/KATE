
# Análisis de complejidad de algoritmos - K.A.T.E.

## 1. Búsqueda lineal

La búsqueda lineal recorre secuencialmente una lista de registros hasta encontrar la clave solicitada.

- Mejor caso: O(1), cuando el elemento está al inicio.
- Caso promedio: O(n).
- Peor caso: O(n), cuando está al final o no existe.
- Complejidad espacial auxiliar: O(1).

## 2. Construcción de tabla hash

Se utiliza un diccionario de Python para almacenar los registros mediante claves normalizadas.

- Complejidad temporal promedio: O(n).
- Complejidad espacial: O(n).

## 3. Búsqueda hash

La búsqueda hash utiliza acceso directo al diccionario para recuperar un registro.

- Mejor caso: O(1).
- Caso promedio: O(1).
- Peor caso teórico: O(n), debido a posibles colisiones.
- Complejidad espacial auxiliar: O(1).

## 4. Comparación de algoritmos

La búsqueda lineal no necesita estructuras adicionales, pero su tiempo de ejecución aumenta conforme crece la cantidad de registros.

La búsqueda hash requiere memoria adicional para construir el índice, pero permite realizar consultas mucho más rápidas en promedio.

## 5. Conclusión

Para K.A.T.E., la búsqueda lineal permite recuperar información mediante un recorrido secuencial, mientras que la búsqueda hash ofrece una alternativa más eficiente cuando se manejan grandes cantidades de recuerdos.

Ambos algoritmos fueron implementados y validados mediante cuatro pruebas automatizadas exitosas.

## 6. Resultados experimentales

Se realizaron pruebas de ejecución con diferentes cantidades de registros, buscando un elemento ubicado al final de la lista para evaluar el peor caso de la búsqueda lineal.

| Registros | Búsqueda lineal | Búsqueda hash |
|---:|---:|---:|
| 1,000 | 0.0986 ms | 0.0011 ms |
| 10,000 | 0.8193 ms | 0.0013 ms |
| 100,000 | 8.0302 ms | 0.0080 ms |

### Interpretación

Los resultados muestran que el tiempo de búsqueda lineal aumenta conforme crece la cantidad de registros.

En cambio, la búsqueda hash mantiene tiempos de consulta considerablemente menores en las pruebas realizadas.

Estos resultados son mediciones preliminares de una ejecución y pueden variar dependiendo del equipo y las condiciones de ejecución.

### Conclusión experimental

La experimentación respalda el análisis teórico: la búsqueda lineal presenta un crecimiento proporcional a la cantidad de registros, mientras que la búsqueda hash ofrece un rendimiento promedio cercano a O(1) para las consultas.
