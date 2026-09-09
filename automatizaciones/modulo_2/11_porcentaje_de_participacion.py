"""Porcentaje de participación.

Calcula automáticamente la parte del total del equipo aportada por cada jugador y protege la división entre cero.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def porcentaje_participacion(df, valor, grupo='Equipo'):
    df = df.copy()
    total = df.groupby(grupo)[valor].transform('sum')
    df[f'pct_{valor}'] = df[valor].div(total.where(total.ne(0)))
    return df
