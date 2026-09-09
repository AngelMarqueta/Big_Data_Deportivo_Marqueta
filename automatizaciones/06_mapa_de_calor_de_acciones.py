"""Mapa de calor de acciones.

Automatiza la densidad espacial con una malla constante para permitir comparaciones.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def mapa_calor(eventos, equipo, bins=(12, 8)):
    acciones = coordinates(eventos.query('team == @equipo')).dropna(subset=['x', 'y'])
    fig, ax = plt.subplots(figsize=(9, 6))
    mapa = ax.hist2d(acciones['x'], acciones['y'], bins=bins,
                    range=((0, 120), (0, 80)), cmap='magma')
    fig.colorbar(mapa[3], ax=ax, label='Acciones')
    ax.set(title=f'Densidad de acciones · {equipo}', ylim=(80, 0), aspect='equal')
    return fig, ax
