"""Dispersión tridimensional.

Reproduce la automatización 3D del curso; conviene usarla para exploración, no para comparaciones exactas.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def grafico_3d(df, x, y, z, color='#1f77b4'):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x], df[y], df[z], c=color, alpha=.7)
    ax.set(xlabel=x, ylabel=y, zlabel=z)
    return fig, ax
