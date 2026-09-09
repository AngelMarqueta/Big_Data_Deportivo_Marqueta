"""Matriz o red de pases.

Calcula posiciones medias y conexiones; exige receptor y filtra enlaces débiles.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def matriz_pases(pases, minimo=3):
    pases = coordinates(pases).dropna(subset=['player', 'pass_recipient', 'x', 'y'])
    nodos = pases.groupby('player', as_index=False).agg(x=('x', 'mean'), y=('y', 'mean'), pases=('id', 'count'))
    enlaces = (pases.groupby(['player', 'pass_recipient']).size()
               .rename('peso').reset_index().query('peso >= @minimo'))
    return nodos, enlaces
