"""Competición, temporada y partidos de StatsBomb.

Encadena los identificadores hasta obtener el partido elegido. Corrige el nombre info_jason del material a info_json.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

from statsbombpy import sb

def info_json(competicion, temporada):
    competiciones = sb.competitions()
    fila = competiciones.loc[
        competiciones['competition_name'].eq(competicion)
        & competiciones['season_name'].eq(temporada)
    ]
    if fila.empty:
        raise ValueError('Competición o temporada inexistente')
    return sb.matches(
        competition_id=int(fila.iloc[0]['competition_id']),
        season_id=int(fila.iloc[0]['season_id']))
