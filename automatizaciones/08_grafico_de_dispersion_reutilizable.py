"""Gráfico de dispersión reutilizable.

Representa la relación entre dos métricas y permite codificar una categoría deportiva.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

import seaborn as sns

def grafico_scatter(df, x, y, grupo=None, titulo=''):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=grupo, ax=ax)
    ax.set_title(titulo)
    fig.tight_layout()
    return fig, ax
