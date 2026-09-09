"""Basketball Reference por equipo y año.

Parametriza año y equipo y evita repetir manualmente la extracción.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def basketball_equipo(equipo, anio):
    url = f'https://www.basketball-reference.com/teams/{equipo}/{anio}.html'
    tablas = pd.read_html(url)
    candidatas = [t for t in tablas if 'Player' in t.columns]
    if not candidatas:
        raise ValueError(f'Sin tabla de jugadores para {equipo} {anio}')
    return candidatas[0].assign(equipo=equipo, temporada=anio)
