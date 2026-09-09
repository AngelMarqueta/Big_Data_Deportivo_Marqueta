"""Flechas de pases.

Dibuja origen y destino de cada pase y distingue los incompletos.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def mapa_pases(eventos, jugador):
    pases = coordinates(eventos.query("type == 'Pass' and player == @jugador"))
    destinos = pases['pass_end_location'].apply(lambda p: p if isinstance(p, list) else [pd.NA, pd.NA])
    pases[['x_fin', 'y_fin']] = pd.DataFrame(destinos.tolist(), index=pases.index)
    fig, ax = plt.subplots(figsize=(9, 6))
    for fila in pases.itertuples():
        ax.annotate('', (fila.x_fin, fila.y_fin), (fila.x, fila.y),
                    arrowprops={'arrowstyle': '->', 'alpha': .45})
    ax.set(xlim=(0, 120), ylim=(80, 0), aspect='equal', title=f'Pases · {jugador}')
    return fig, ax
