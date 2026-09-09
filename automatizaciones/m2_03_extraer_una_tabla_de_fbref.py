"""Extraer una tabla de FBref.

Lee tablas HTML y selecciona la que contiene las columnas esperadas en lugar de asumir una posición fija.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def extraer_tabla_fbref(url, columnas_obligatorias=('Player',)):
    tablas = pd.read_html(url)
    for tabla in tablas:
        tabla.columns = [c[-1] if isinstance(c, tuple) else c for c in tabla.columns]
        if set(columnas_obligatorias).issubset(tabla.columns):
            return tabla
    raise ValueError('No se encontró la tabla esperada')
