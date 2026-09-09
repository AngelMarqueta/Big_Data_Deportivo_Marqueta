"""Creación automática de nuevas columnas.

Recibe fórmulas como funciones para crear métricas reproducibles sin repetir asignaciones.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def crear_metricas(df):
    df = df.copy()
    minutos_validos = df['Minutos'].where(df['Minutos'].gt(0))
    df['Goles_90'] = df['Goles'].div(minutos_validos).mul(90)
    df['Asistencias_90'] = df['Asistencias'].div(minutos_validos).mul(90)
    df['Contribuciones_90'] = df['Goles_90'] + df['Asistencias_90']
    return df
