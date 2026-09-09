"""Mapa automático de tiros.

Filtra tiros, escala su tamaño por xG y diferencia el resultado.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def mapa_tiros(eventos, equipo):
    tiros = coordinates(eventos.query("type == 'Shot' and team == @equipo"))
    fig, ax = plt.subplots(figsize=(9, 6))
    colores = tiros['shot_outcome'].eq('Goal').map({True: '#e63946', False: '#457b9d'})
    ax.scatter(tiros['x'], tiros['y'], s=40 + 500 * tiros['shot_statsbomb_xg'],
               c=colores, alpha=.75, edgecolor='white')
    ax.set(title=f'Mapa de tiros · {equipo}', xlim=(0, 120), ylim=(80, 0), aspect='equal')
    return fig, ax
