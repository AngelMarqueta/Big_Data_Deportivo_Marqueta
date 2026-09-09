"""Crear e importar una librería propia.

Guarda las funciones estables en un módulo y reutilízalas con una importación normal.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

# archivo graficas_deportivas.py
def tasa_por_90(valor, minutos):
    return 0 if minutos == 0 else valor / minutos * 90

# cuaderno o programa principal
from graficas_deportivas import tasa_por_90
xg_90 = tasa_por_90(valor=4.2, minutos=900)
