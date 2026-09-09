"""Aplicar una función a varias columnas.

Encapsula la conversión de columnas y permite reutilizarla en nuevos conjuntos de datos.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def convertir_columnas(df, columnas):
    df = df.copy()
    for col in columnas:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
