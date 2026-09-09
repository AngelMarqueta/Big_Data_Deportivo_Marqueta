"""Función principal con funciones auxiliares.

Divide un proceso grande en lectura, limpieza y validación para poder probar cada parte.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def preparar_datos(ruta):
    def leer(ruta_archivo):
        return pd.read_csv(ruta_archivo)
    def limpiar(df):
        return df.drop_duplicates().rename(columns=lambda c: c.strip())
    df = limpiar(leer(ruta))
    if df.empty:
        raise ValueError('El archivo no contiene registros')
    return df
