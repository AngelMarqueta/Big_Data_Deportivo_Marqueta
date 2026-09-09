"""Basketball Reference para varias temporadas.

Automatiza el histórico y mantiene las claves de temporada y equipo.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def basketball_historico(equipo, anios):
    datos = [basketball_equipo(equipo, anio) for anio in anios]
    return pd.concat(datos, ignore_index=True, sort=False)
