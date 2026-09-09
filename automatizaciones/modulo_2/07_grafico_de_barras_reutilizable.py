"""Gráfico de barras reutilizable.

Devuelve figura y eje para que el llamador pueda guardar, anotar o combinar el gráfico.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

import matplotlib.pyplot as plt

def grafico_barras(df, categoria, valor, titulo):
    resumen = df.groupby(categoria, as_index=False)[valor].sum()
    resumen = resumen.sort_values(valor, ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(resumen[categoria], resumen[valor], color='#1f77b4')
    ax.set(title=titulo, xlabel=categoria, ylabel=valor)
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig, ax
